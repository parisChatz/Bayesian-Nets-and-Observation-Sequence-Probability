#!/usr/bin/env python3

from approximate_algorithms import normalize
from approximate_algorithms import RejectionSamplingAlgorithm
from collections import OrderedDict
from networks import Networks


def bayes_eq(pd, ptd, neg_ptd):
    p_posd = pd
    p_post_posd = ptd
    p_negt_posd = 1 - neg_ptd

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
    net = Networks().initialiseNet("disease")

    # conditional distirbution table value import/calculation
    net['D']['+d'] = Pd
    net['D']['-d'] = 1 - Pd
    net['T']['+t|+d'] = Ptd
    net['T']['+t|-d'] = 1 - Ptd
    net['T']['-t|-d'] = neg_Ptd
    net['T']['-t|+d'] = 1 - neg_Ptd

    # rejection sampling initialisation and call
    rs = RejectionSamplingAlgorithm(net)
    rs_result = rs.rej_sampling(*query)

    # bayes equation call
    be_result = bayes_eq(Pd, Ptd, neg_Ptd)

    # result print
    print('rejection Sampling: ', rs_result)
    print('Bayes eq: ', be_result)
