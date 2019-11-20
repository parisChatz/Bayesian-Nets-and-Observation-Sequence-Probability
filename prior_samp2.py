import random

class PriorSampling():
    
    def __init__(self, net):
        self.net=net

    def sampleVariable(self, CPT, conditional):
        sampledValue=None
        randnumber=random.random()

        value1=CPT["+"+conditional]
        value2=CPT["-"+conditional]

        if randnumber<=value1:
            sampledValue="+"+conditional
        else:
            sampledValue="-"+conditional

        return sampledValue.split("|")[0]

    def sampleVariables(self, printEvent=False):
        event=[]
        sampledVars={}

        for variable in self.net["order"]:
            evidence=""
            conditional=""
            parents=self.net["parents"][variable]
            if parents==None:
                conditional=variable.lower()
            else:
                for parent in parents.split(","):
                    evidence+=sampledVars[parent]
                conditional=variable.lower()+"|"+evidence

            sampledValue=self.sampleVariable(self.net[variable], conditional)
            event.append(sampledValue)
            sampledVars[variable]=sampledValue
                
        if printEvent: print(event)
        return event

