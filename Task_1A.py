#!/usr/bin/env python3

import sys
import random

class parsing():

    def __init__(self):
        pass

    def parse_data(self, data):

        data = data.replace("P(", "").replace(")", "").split("|")
        if len(data) > 1:
            query = data[0].split()
            evidence = data[1].split(",")
        return query, evidence


class network():
    CPTs = {}

    def __init__(self):
        
        # d = float(raw_input("P( d ) prior probability of having a disease: "))
        # pos_t = float(raw_input("P( t | d ) probability that the test is positive given the person has the disease : "))
        # neg_t = float(raw_input("P( -t | -d ) probability that the test is negative given the person does not have the disease : "))

        # self.CPTs["D"] = {"+d": d, "-d": 1-d}
        # self.CPTs["T"] = {"+t|+d": pos_t, "-t|-d": neg_t,
        #               "+t|-d": 1-pos_t, "-t|+d": 1-neg_t}

        # d = 0.1
        # self.CPTs["D"] = {"+d": d, "-d":1-d }
        # self.CPTs["T"] = {"+t|+d": 0.99, "-t|-d": 0.95,
        #                     "+t|-d": 0.01, "-t|+d": 0.05}
        
        # self.CPTs["order"] = ["D", "T"]
        # self.CPTs["parents"] = {"D": None, "T": "D"}
        self.CPTs["C"]={"+c":0.50, "-c":0.50}
        self.CPTs["S"]={"+s|+c":0.10, "-s|+c":0.90, 
                "+s|-c":0.50, "-s|-c":0.50}
        self.CPTs["R"]={"+r|+c":0.80, "-r|+c":0.20, 
                "+r|-c":0.20, "-r|-c":0.80}
        self.CPTs["W"]={"+w|+s+r":0.99, "-w|+s+r":0.01, 
                "+w|+s-r":0.90, "-w|+s-r":0.10,
                "+w|-s+r":0.90, "-w|-s+r":0.10,
                "+w|-s-r":0.00, "-w|-s-r":1.00}
        self.CPTs["order"]=["C", "S", "R", "W"]
        self.CPTs["parents"]={"C":None, "S":"C", "R":"C", "W":"S,R"}

    def sampleVariable(self, CPT, conditional):
        sampledValue=None
        randnumber=random.random()

        value1=CPT["+"+conditional]
        value2=CPT["-"+conditional]

        if randnumber<=value1:
            sampledValue="+"+conditional
        else:
            sampledValue="-"+conditional

        return sampledValue.split("|")[0]

    def sampleVariables(self, printEvent=False):
        event=[]
        sampledVars={}

        for variable in self.CPTs["order"]:
            evidence=""
            conditional=""
            parents=self.CPTs["parents"][variable]
            if parents==None:
                conditional=variable.lower()
            else:
                for parent in parents.split(","):
                    evidence+=sampledVars[parent]
                conditional=variable.lower()+"|"+evidence

            sampledValue=self.sampleVariable(self.CPTs[variable], conditional)
            event.append(sampledValue)
            sampledVars[variable]=sampledValue
                
        if printEvent: print(event)
        return event

    def normalize(self, unormalized_probs):
        normalized = {}
        prob_sum = float(sum(unormalized_probs.values()))
        for sign, value in unormalized_probs.items():
            normalized[sign] = value / prob_sum

        return normalized

    def is_consistent(self, evidence, random_query):
        k = []
        for i in evidence:
            if i in random_query:
                k.append(True)
            else:
                k.append(False)
        consistent=all(k)
        return consistent

    def rej_sampling(self,reps = 100000):  
        N = {"positive": 0, "negative": 0}
        X, e = parsing().parse_data("P(+w|+s,-r)")
        random_query = self.sampleVariables()
              
        for j in range(1, reps):
            random_query = self.sampleVariables()
            if self.is_consistent(e,random_query):
                if("+" in random_query[0]):
                    N["positive"] += 1
                if("-" in random_query[0]):
                    N["negative"] += 1

        k = self.normalize(N)
        print("rej_sampling P(d|t): ",k)
        

    def bayes_eq(self):
        p_posd = self.CPTs["D"]["+d"]
        p_post_posd = self.CPTs["T"]["+t|+d"]
        p_negt_negd = self.CPTs["T"]["-t|-d"]
        p_negt_posd = self.CPTs["T"]["-t|+d"]

        unormalized_p_posd_post = float(p_post_posd) * float(p_posd)
        unormalized_p_posd_negt = float(p_negt_posd) * float(p_posd)
        unormalized_probs = {
            "positive": unormalized_p_posd_post, "negative": unormalized_p_posd_negt}
        normalized_p_posd = self.normalize(unormalized_probs)
        k = normalized_p_posd
        print("bayes_eq P(d|t): ",k)


if __name__ == "__main__":

    net = network()

    net.rej_sampling()

    #net.bayes_eq()
