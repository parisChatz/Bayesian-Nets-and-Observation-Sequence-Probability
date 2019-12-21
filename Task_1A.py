#!/usr/bin/env python3

from approximate_algorithms import normalize
from approximate_algorithms import Rejection_Sampling_algorithm
from collections import OrderedDict
from networks import networks


def bayes_eq(Pd, Ptd, neg_Ptd):

    p_posd = Pd
    p_post_posd = Ptd
    p_negt_posd = 1 - neg_Ptd

    k = OrderedDict()
    unormalized_probs = OrderedDict()
    unormalized_probs["+"] = 0
    unormalized_probs["-"] = 0

    unormalized_p_posd_post = float(p_post_posd) * float(p_posd)
    unormalized_p_posd_negt = float(p_negt_posd) * float(p_posd)
    unormalized_probs["+"] = unormalized_p_posd_post
    unormalized_probs["-"] = unormalized_p_posd_negt

    k = normalize(unormalized_probs)
    return k


if __name__ == "__main__":

    # query initialisation
    query = ('D', ['+t'])

    # wanted probabilities import
    Pd = float(input("Input P(d): "))
    Ptd = float(input("Input P(+t|+d): "))
    neg_Ptd = float(input("Input P(-t|-d): "))

    # net initialisation
    net = networks().initialiseNet("disease")

    # conditional distirbution table value import/calculation
    net['D']['+d'] = Pd
    net['D']['-d'] = 1 - Pd
    net['T']['+t|+d'] = Ptd
    net['T']['+t|-d'] = 1 - Ptd
    net['T']['-t|-d'] = neg_Ptd
    net['T']['-t|+d'] = 1 - neg_Ptd

    # rejection sampling initialisation and call
    rs = Rejection_Sampling_algorithm(net)
    rs_result = rs.rej_sampling(*query)

    # bayes equation call
    be_result = bayes_eq(Pd, Ptd, neg_Ptd)

    # result print
    print('rejection Sampling: ', rs_result)
    print('Bayes eq: ', be_result)
