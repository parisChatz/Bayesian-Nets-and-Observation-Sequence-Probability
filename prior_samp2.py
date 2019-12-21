# prior sampling algorithm
# developed by Dr Heriberto Cuayahuitl Portilla University of Lincoln


import random


class PriorSampling():

    def __init__(self, net):
        self.net = net

    def sampleVariable(self, CPT, conditional):
        sampledValue = None
        randnumber = random.random()
        value1 = CPT["+" + conditional]

        if randnumber <= value1:
            sampledValue = "+" + conditional
        else:
            sampledValue = "-" + conditional

        return sampledValue.split("|")[0]

    def sampleVariables(self, evidences=None, printEvent=False):
        event = []
        sampledVars = {}

        for variable in self.net["order"]:
            evidence = ""
            conditional = ""
            parents = self.net["parents"][variable]
            if parents is None:
                conditional = variable.lower()
            else:
                for parent in parents.split(","):
                    evidence += sampledVars[parent]
                conditional = variable.lower() + "|" + evidence

            if evidences is not None:
                evid_pos = [e[1:] for e in evidences]

                if variable.lower() not in evid_pos:
                    sampledValue = self.sampleVariable(
                        self.net[variable], conditional)
                else:
                    indx_evid = evid_pos.index(variable.lower())
                    sampledValue = evidences[indx_evid]
            else:
                sampledValue = self.sampleVariable(
                    self.net[variable], conditional)
            event.append(sampledValue)
            sampledVars[variable] = sampledValue

        if printEvent:
            print(event)
        return event
