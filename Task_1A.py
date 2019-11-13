#!/usr/bin/env python3
from PriorSampling import PriorSampling


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
        self.CPTs["D"] = {"+d": 0.1, "-d": 0.9}
        self.CPTs["T"] = {"+t|+d": 0.99, "-t|-d": 0.95,
                          "+t|-d": 0.01, "-t|+d": 0.05}
        self.CPTs["order"] = ["D", "T"]
        self.CPTs["parents"] = {"D": None, "T": "D"}

    def normalize(self, unormalized_probs):
        normalized = {}
        prob_sum = float(sum(unormalized_probs.values()))
        for sign, value in unormalized_probs.items():
            normalized[sign] = value / prob_sum

        return normalized

# X = query variable
# e = observed values for events
# reps = number of repetition
    def rej_sampling(self):  # , X, e, reps
        N = {"positive": 0, "negative": 0}
        X, e = parsing().parse_data("P(d|+t)")
        reps = 10000
        
        net = PriorSampling("des")
        for j in range(1, reps):
            random_query = net.sampleVariables()
            print(random_query[0], X[0], ":", random_query[1], e[0],
                  random_query[0] == X[0], random_query[1] == e[0])
            if (random_query[1] == e[0]):
                if("+" in random_query[0]):
                    N["positive"] += 1
                if("-" in random_query[0]):
                    N["negative"] += 1
        print(self.normalize(N))

        # print(random_query[0],X[0],random_query[0]==X[0])

    def bayes_eq(self):
        p_posd = self.CPTs["D"]["-d"]
        p_post_posd = self.CPTs["T"]["+t|+d"]
        p_negt_negd = self.CPTs["T"]["-t|-d"]

        unormalized_p_posd_post = p_post_posd * p_posd
        unormalized_p_posd_negt = 1 - unormalized_p_posd_post
        unormalized_probs = {
            "positive": unormalized_p_posd_post, "negative": unormalized_p_posd_negt}
        normalized_p_posd = self.normalize(unormalized_probs)
        print(normalized_p_posd)


if __name__ == "__main__":
    network().rej_sampling()
    network().bayes_eq()
