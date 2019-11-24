#!/usr/bin/env python3

from approximate_algorithms import Likelihood_Weighting_algorithm
from approximate_algorithms import Rejection_Sampling_algorithm
from networks import networks

if __name__ == "__main__":



    net = networks().initialiseNet("disease")

    lw = Likelihood_Weighting_algorithm(net)
    lw_result = lw.likelihood_weighting('D',['-t'])
    sr = Rejection_Sampling_algorithm(net)
    sr_result = lw.likelihood_weighting('D',['-t'])

    print(lw_result)
    print(sr_result)