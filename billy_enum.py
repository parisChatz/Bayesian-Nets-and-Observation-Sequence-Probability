#!/usr/bin/env python3

import copy
from bayesian import BayesianClass, ParseInputs


class Enumeration(BayesianClass):

    def __init__(self, graph):
        self.graph = graph

    def enum_ask(self, node, query):
        sorted_nodes = self.sort_nodes(self.graph.keys())
        prob_results = []
        for cond in [False, True]:
            query_copy = copy.deepcopy(query)
            query_copy[node] = cond

            # print(node, query_copy, cond)
            prob = self.enum_all(sorted_nodes, query_copy)
            prob_results.append({'condition': cond, 'prob': prob})

        return self.normalize(prob_results)

    def enum_all(self, sorted_nodes, query):
        if len(sorted_nodes) == 0:
            return 1.0
        if sorted_nodes[0] in query:
            ret = self.calc_query(
                sorted_nodes[0], query, self.graph) * self.enum_all(sorted_nodes[1:], query)
        else:
            probs = []
            query_copy = copy.deepcopy(query)
            for cond in [True, False]:
                query_copy[sorted_nodes[0]] = cond
                probs.append(self.calc_query(sorted_nodes[0], query_copy, self.graph) *
                             self.enum_all(sorted_nodes[1:], query_copy))
            ret = sum(probs)

        # print("%-14s | %-20s = %.8f" % (
        #     ' '.join(sorted_nodes),
        #     ' '.join('%s=%s' % (v, 't' if query[v] else 'f') for v in query),
        #     ret
        # ))
        return ret


if __name__ == '__main__':
    parser = ParseInputs()
    known_data = parser.get_test_data()
    # known_data = {
    #     'P(C)': 0.5,
    #     'P(S|c)': 0.1,
    #     'P(S|-c)': 0.5,
    #     'P(R|c)': 0.8,
    #     'P(R|-c)': 0.2,
    #     'P(W|s,r)': 0.99,
    #     'P(W|s,-r)': 0.9,
    #     'P(W|-s,r)': 0.9,
    #     'P(W|-s,-r)': 0,
    # }

    graph = parser.get_graph(known_data)
    node, query = parser.get_query('P(B|a,-j)')
    print(node, query)

    for key, value in parser.graph.items():
        print(key, value)
    print('---------------')

    enum = Enumeration(graph)
    enum_results = enum.enum_ask(node, query)
    parser.print_results(node, query, enum_results)