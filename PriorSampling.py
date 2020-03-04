# prior sampling algorithm
# developed by Dr Heriberto Cuayahuitl Portilla University of Lincoln


import random


class PriorSampling:

    def __init__(self, net):
        self.net = net

    @staticmethod
    def sampleVariable(CPT, conditional):
        sampled_value = None
        randnumber = random.random()
        value1 = CPT["+" + conditional]

        if randnumber <= value1:
            sampled_value = "+" + conditional
        else:
            sampled_value = "-" + conditional

        return sampled_value.split("|")[0]

    def sampleVariables(self, evidences=None, printEvent=False):
        event = []
        sampled_vars = {}

        for variable in self.net["order"]:
            evidence = ""
            conditional = ""
            parents = self.net["parents"][variable]
            if parents is None:
                conditional = variable.lower()
            else:
                for parent in parents.split(","):
                    evidence += sampled_vars[parent]
                conditional = variable.lower() + "|" + evidence

            if evidences is not None:
                evid_pos = [e[1:] for e in evidences]

                if variable.lower() not in evid_pos:
                    sampled_value = self.sampleVariable(
                        self.net[variable], conditional)
                else:
                    indx_evid = evid_pos.index(variable.lower())
                    sampled_value = evidences[indx_evid]
            else:
                sampled_value = self.sampleVariable(
                    self.net[variable], conditional)
            event.append(sampled_value)
            sampled_vars[variable] = sampled_value

        if printEvent:
            print(event)
        return event
