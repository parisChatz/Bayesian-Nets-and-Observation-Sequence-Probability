#!/usr/bin/env python3

from collections import OrderedDict
import copy


class input_processing():

    def __init__(self):
        network = collections.OrderedDict()
        network = {
            'P(C)': 0.5,
            'P(S|c)': 0.1,
            'P(S|-c)': 0.5,
            'P(R|c)': 0.8,
            'P(R|-c)': 0.2,
            'P(W|s,r)': 0.99,
            'P(W|s,-r)': 0.9,
            'P(W|-s,r)': 0.9,
            'P(W|-s,-r)': 0,
        }
