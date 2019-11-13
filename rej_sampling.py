#!/usr/bin/env python3

from PriorSampling import PriorSampling
from collections import OrderedDict
import copy


class input_processing():

    def __init__(self):
        
        network = OrderedDict()
        network2 = {}
        network["C"] = {"+c": 0.50, "-c": 0.50}
        network["S"] = {"+s|+c": 0.10, "-s|+c": 0.90,
                        "+s|-c": 0.50, "-s|-c": 0.50}
        network["R"] = {"+r|+c": 0.80, "-r|+c": 0.20,
                        "+r|-c": 0.20, "-r|-c": 0.80}
        network["W"] = {"+w|+s+r": 0.99, "-w|+s+r": 0.01, "+w|+s-r": 0.90, "-w|+s-r": 0.10,
                        "+w|-s+r": 0.90, "-w|-s+r": 0.10, "+w|-s-r": 0.00, "-w|-s-r": 1.00}
        network2["parents"] = {"C": None, "S": "C", "R": "C", "W": "S,R"}
        network2["nodes"] = network
        print network2["nodes"].keys()
    # def network_topology(self, network):


if __name__ == "__main__":
    input_processing()
