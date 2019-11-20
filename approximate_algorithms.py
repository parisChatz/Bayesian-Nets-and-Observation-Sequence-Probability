from prior_samp2 import PriorSampling
from collections import OrderedDict

def normalize( unormalized_probs):
    normalized = OrderedDict()
    prob_sum = float(sum(unormalized_probs.values()))
    for sign, value in unormalized_probs.items():
        if prob_sum != 0:
            normalized[sign] = value / prob_sum
        else:
            normalized[sign] = 0
            print('unormalized probs are zero!')

    return normalized

class Likelihood_Weighting_algorithm():
    
    def __init__(self,net):
        self.net=net

    def likelihood_weighting(self,X,evidences,samples = 10000):
        
        W = OrderedDict()
        W["+"]=0
        W["-"]=0

        for i in range(1,samples+1):
            events, weight = self.weighted_sample(evidences)
            x = X.lower()
            k = [event[0] for event in events if x in event][0]
            W[k]+=weight
        
        normalized_probabilities = normalize(W)
        return normalized_probabilities

    def weighted_sample(self,evidences):
        e = evidences 
        evid_pos = [e[1:] for e in evidences]
        w = 1
        nodes = [node.lower() for node in self.net["order"]]
        events = PriorSampling(self.net).sampleVariables()

        for Xi in nodes:
            if Xi in evid_pos:
                indx = evid_pos.index(Xi)
                idx_node = nodes.index(Xi)
                if evidences[indx] in events:
                    if self.net["parents"][Xi.upper()] is None:
                        w *= self.net[Xi.upper()][evidences[indx]]
                    else:    
                        parents = self.net["parents"][Xi.upper()].lower().split(',')
                        for event in events:
                            if event[1:] in parents:
                                parents[parents.index(event[1:])] = event
                        parents="".join(parents)
                        inside_prob = evidences[indx]+"|"+parents
                        w *= self.net[Xi.upper()][inside_prob]

        return events,w

class Rejection_Sampling_algorithm():

    def __init__(self,net):
        self.net=net

    def rej_sampling(self,X,evidences,reps = 10000):  
        
        N = OrderedDict()
        N["+"]=0
        N["-"]=0
        
        for j in range(1, reps+1):
            random_query = PriorSampling(self.net).sampleVariables()
            #print(random_query,X,e,self.is_consistent(e,random_query))
            if self.is_consistent(evidences,random_query):
                if('+'+X[0] in random_query):
                    N["+"] += 1
                else:
                    N["-"] += 1

        normalized_probabilities = self.normalize(N)

        
    def is_consistent(self, evidences, random_query):
        k = []
        for evidence in evidences:
            if evidence in random_query:
                k.append(True)
            else:
                k.append(False)
        consistent=all(k)
        return consistent