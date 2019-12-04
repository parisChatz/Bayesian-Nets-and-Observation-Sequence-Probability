#!/usr/bin/env python3

from approximate_algorithms import Likelihood_Weighting_algorithm
from approximate_algorithms import Rejection_Sampling_algorithm
from networks import networks
from read_cpt_from_csv import read_cpts_from_csv

if __name__ == "__main__":

    query = ('S', ['-c'])
    net = networks().initialiseNet("sprinkler")
    # query = ('LC', ['+s', '-g'])
    # net = read_cpts_from_csv(networks().initialiseNet("cancer")).read_cpts()
    lw = Likelihood_Weighting_algorithm(net)
    lw_result = lw.likelihood_weighting(*query)

    rs = Rejection_Sampling_algorithm(net)
    rs_result = rs.rej_sampling(*query)

    print('Likelihood Weighting: ', lw_result)
    print('Rejection Sampling: ', rs_result)
