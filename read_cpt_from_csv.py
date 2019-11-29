import pandas as pd
from networks import networks
from parsing import parsing

class read_cpts_from_csv():
    def __init__(self,net):
        self.net = net

    def read_cpts(self):
        variables = []
        evidences = []
        var_nosign = []
        evid_nosign = []
        new_evid = []
        df = pd.read_csv('lucas0_train.csv')
        for node in self.net["order"]:
            keylist = list(self.net[node].keys())
            for cond_prob in range(len(keylist)):
                variable, evidence = parsing().parse_querry(keylist[cond_prob])
                variables.append(variable)
                evidences.append(evidence)
                var_nosign.append(variable[1:].upper())

                if evidence==None:
                    evid_nosign.append(str([variable]))
                else:
                    evid_nosign.append(parsing().parse_evidence(evidence))
        
        new_evid = evid_nosign
        for i in range(len(evid_nosign)):
            for k in range(len(evid_nosign[i])):
                if evidences[i] is not None:
                    result = evidences[i].find(evid_nosign[i][k])
                    new_evid[i][k]=evidences[i][result-1]+evid_nosign[i][k]
                    # print(result,evidences[i],evid_nosign[i][k])

            print(var_nosign[i],evid_nosign[i])
        

if __name__ == '__main__':
    read_cpts_from_csv(networks().initialiseNet("cancer")).read_cpts()