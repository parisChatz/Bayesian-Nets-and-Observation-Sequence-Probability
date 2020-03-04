#!/usr/bin/env python3

# Your program should first learn its parameters from data
# and then use inference to calculate the probability
# distribution of Smoking given Coughing and Fatigue.
# Network topology and parameter values downloaded from the following link
# http://www.causality.inf.ethz.ch/data/LUCAS.html
from typing import Dict, Any

from approximate_algorithms import LikelihoodWeightingAlgorithm
from approximate_algorithms import RejectionSamplingAlgorithm
from networks import Networks
from parameterlearningfromcsv import ParameterLearningFromCsv

if __name__ == "__main__":
    Variable = str(
        input("Input the wanted Variable name (eg. LC all caps no sign): "))
    evidence = str(input("Input the evidences name (eg. +s,+g): "))
    evidence = evidence.split(",")

    query = (Variable, evidence)
    network = Networks().initialiseNet("cancer")  # type dictionary with empty network topology
    net = ParameterLearningFromCsv(network).read_cpts()

    lw = LikelihoodWeightingAlgorithm(net)
    lw_result = lw.likelihood_weighting(*query)

    rs = RejectionSamplingAlgorithm(net)
    rs_result = rs.rej_sampling(*query)

    print('Likelihood Weighting: ', lw_result)
    print('Rejection Sampling: ', rs_result)
