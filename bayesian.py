#!/usr/bin/env python3

from collections import OrderedDict
import copy
import csv


class ParseInputs():

    def __init__(self):
        pass

    def get_test_data(self, netID):
        known_data = {}
        if netID == 'burglary':
            known_data = {
                'P(B)': 0.001,
                'P(E)': 0.002,
                'P(A|b,e)': 0.95,
                'P(A|b,-e)': 0.94,
                'P(A|-b,e)': 0.29,
                'P(A|-b,-e)': 0.001,
                'P(J|a)': 0.90,
                'P(J|-a)': 0.05,
                'P(M|a)': 0.7,
                'P(M|-a)': 0.01,
            }
        elif netID == 'sprinkler':
            known_data = {
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
        elif netID == 'disease':
            known_data = {
                'P(D)': None,
                'P(T|d)': None,
                'P(T|-d)': None,
            }
        elif netID == 'cancer':
            known_data = {
                'P(S|an,pp)': None,
                'P(S|an,-pp)': None,
                'P(S|-an,pp)': None,
                'P(S|-an,-pp)': None,
                'P(YF|s)': None,
                'P(YF|-s)': None,
                'P(AN)': None,
                'P(LC|g,s)': None,
                'P(LC|g,-s)': None,
                'P(LC|-g,s)': None,
                'P(LC|-g,-s)': None,
                'P(PP)': None,
                'P(G)': None,
                'P(AD|g)': None,
                'P(AD|-g)': None,
                'P(BED)': None,
                'P(CA|f,ad)': None,
                'P(CA|f,-ad)': None,
                'P(CA|-f,ad)': None,
                'P(CA|-f,-ad)': None,
                'P(F|lc,co)': None,
                'P(F|lc,-co)': None,
                'P(F|-lc,co)': None,
                'P(F|-lc,-co)': None,
                'P(AL)': None,
                'P(CO|al,lc)': None,
                'P(CO|al,-lc)': None,
                'P(CO|-al,lc)': None,
                'P(CO|-al,-lc)': None,
            }
            pairing = {
                'Smoking': 'S',
                'Yellow_Fingers': 'YF',
                'Anxiety': 'AN',
                'Peer_Pressure': 'PP',
                'Genetics': 'G',
                'Attention_Disorder': 'AD',
                'Born_an_Even_Day': 'BED',
                'Car_Accident': 'CO',
                'Fatigue': 'F',
                'Allergy': 'AL',
                'Coughing': 'CA',
                'Lung_cancer': 'LC',
            }
            allData = []
            with open('lucas0_train.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')

                title = csv_reader.next()
                for num, item in enumerate(title):
                    title[num] = pairing[item]

                for row in csv_reader:
                    row[:] = [True if x == '1' else False for x in row]
                    allData.append(dict(zip(title, row)))

            for inquery in known_data.keys():
                mycount = self._getCPTCounts(inquery, allData, True)
                mycount2 = self._getCPTCounts(inquery, allData, False)
                prob = float(mycount + 1) / float(mycount2 + 2)
                prob = round(prob, 2)
                known_data[inquery] = prob

        return known_data

    def _getCPTCounts(self, inquery, allData, useNode=True):
        node, query = self.get_query(inquery)
        valuesCheck = []
        if useNode:
            valuesCheck.append((node, True))
        for q_node, q_value in query.items():
            valuesCheck.append((q_node, q_value))

        count = 0
        for row in allData:
            foundit = True
            for check in valuesCheck:
                if row[check[0]] != check[1]:
                    foundit = False
            if foundit:
                count += 1

        return count


    def print_results(self, node, query, prob_results):
        for prob_result in prob_results:
            cond_nodes = []
            for cond_node, condition in query.items():
                cond_node = cond_node.lower()
                if not condition:
                    cond_node = '-{0}'.format(cond_node)
                cond_nodes.append(cond_node)

            pr_node = node.lower()
            if not prob_result['condition']:
                pr_node = '-{0}'.format(pr_node)
            print('P({0}|{1}) = {2:.4}'.format(
                pr_node,
                ','.join(cond_nodes),
                prob_result['norm'])
            )

    def get_query(self, query):
        conditions = OrderedDict()
        query = query.upper().replace(' ', '').replace('+', '')
        query = query.replace('P(', '').replace(')', '')
        query = query.split('|')
        name = query[0]
        if len(query) > 1:
            for par in query[1].split(','):
                condition = True
                if par[0] == '-':
                    condition = False
                    par = par[1:]
                conditions[par] = condition
        return name, conditions

    def get_graph(self, known_data):
        """
        Parses the input data to a graph
        Inputs:
            known_data: The data in dictionary format
        Returns:
            Graph data with each node as a dictionary key.
            The values contain the parent and children nodes,
            the probability of that node if it is not have any condition
            and the condition probability for each case.
        """
        self.graph = {}
        childrens = {}
        for key, prob in known_data.items():
            key = key.upper().replace(' ', '')
            key = key.replace('P(', '').replace(')', '')
            key = key.split('|')

            name = key[0]
            # Checks if graph[name] has been set
            if name not in self.graph:
                self.graph[name] = {
                    'parents': [],
                    'children': [],
                    'prob': prob,
                    'condition': {}
                }

            # Checks if it has conditions after '|'
            if len(key) >= 2:
                conditions = []
                # Sets prob to None because of the conditions
                self.graph[name]['prob'] = None
                for par in key[1].split(','):
                    # Sets the correct condition
                    condition = True
                    if par[0] == '-':
                        condition = False
                        par = par[1:]
                    conditions.append(condition)
                    # Adds the parrent nodes if they don't exist
                    if par not in self.graph[name]['parents']:
                        self.graph[name]['parents'].append(par)
                    # Fills the children dictionary
                    childrens.setdefault(par, [name])
                    if name not in childrens[par]:
                        childrens[par].append(name)
                # Adds the condition with the key value being a tupple of True/False
                self.graph[name]['condition'][tuple(conditions)] = prob

        # Fills the graph children
        for name, children in childrens.items():
            self.graph[name]['children'] = children

        # self.graph = self._add_missing_negative(self.graph)
        self.graph = self._sort_nodes(self.graph)
        return self.graph

    def _add_missing_negative(self, graph):
        negative = {}
        for node, node_options in graph.items():
            prob = None
            conditions = {}
            if node_options['prob'] is not None:
                prob = round(1 - node_options['prob'], 10)
            else:
                for cond, cond_prob in node_options['condition'].items():
                    conditions[cond] = round(1 - cond_prob, 10)
            negative = copy.deepcopy(node_options)
            negative['prob'] = prob
            negative['condition'] = conditions
            graph[node]['negative'] = negative
        return graph

    def _sort_nodes(self, graph):
        sortedGraph = OrderedDict()
        nodes = graph.keys()

        variables = list(nodes)
        variables.sort()

        sorted_nodes = []
        while len(sorted_nodes) < len(variables):
            for node in variables:
                hasNoParents = True
                for par in graph[node]['parents']:
                    hasNoParents = False
                    if par in sorted_nodes:
                        hasNoParents = True
                if node not in sorted_nodes and hasNoParents:
                    sorted_nodes.append(node)

        for node in sorted_nodes:
            sortedGraph[node] = graph[node]
        return sortedGraph


class BayesianClass():
    def __init__(self):
        pass

    def normalize(self, prob_results):
        normalized = []
        mysum = sum(item['prob'] for item in prob_results)
        for item in prob_results:
            if mysum != 0:
                item['norm'] = item['prob'] / mysum
            else:
                item['norm'] = 0
            normalized.append(item)
        return normalized

    def calc_query(self, node, query, graph):
        if len(self.graph[node]['parents']) == 0:
            prob = self.graph[node]['prob']
        else:
            # get the value of parents of node
            parents = tuple(query[par]
                            for par in self.graph[node]['parents'])
            prob = graph[node]['condition'][parents]

        if not query[node]:
            prob = round(1 - prob, 10)

        return prob


if __name__ == '__main__':
    parser = ParseInputs()
    known_data = parser.get_test_data('cancer')
    graph = parser.get_graph(known_data)
    # node, query = parser.get_query('P(B|j,m)')
    # print(node, query)
    for node, node_options in parser.graph.items():
        print(node, node_options)