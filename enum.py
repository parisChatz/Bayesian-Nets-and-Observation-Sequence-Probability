    # def enum_ask(self):
    #     X = self.X
    #     e = self.e
    #     dist = []
    #     print(X,e)
    #     # for x in [False, True]:
    #         # make a copy of the evidence set
    #         # e = copy.deepcopy(e)
    #         # extend e with value of X
    #         # e[X] = x
    #         # print(e)

    #     #     # topological sort
    #     #     variables = self.CPTs["order"]
    #     #     print(variables)

    #         # enumerate
    #         # dist.append(self.enum_all(variables, e))

    #     # normalize & return
    #     #return self.normalize(dist)
    #     print(self.CPTs['A']['+a|+b-e'])

    # def enum_all(self, variables, e):
    #     """
    #     Enumerate over variables.
    #     Args:
    #         variables:  List of variables, topologically sorted
    #         e:          Dictionary of the evidence set in form of 'var': True/False.
    #     Returns:
    #         probability as a real number
    #     """
    #     if len(variables) == 0:
    #         return 1.0
    #     Y = variables[0]
    #     if Y in e:
    #         ret = self.CPTs(Y, e) * self.enum_all(variables[1:], e)
