#!/usr/bin/env python3

import sys
import random

class create_cpt():
	def __init__(self):
		known_data = {
                'P(Smoking|Anxiety,Peer_Pressure)': None,
                'P(Smoking|Anxiety,-Peer_Pressure)': None,
                'P(Smoking|-Anxiety,Peer_Pressure)': None,
                'P(Smoking|-Anxiety,-Peer_Pressure)': None,
                'P(Yellow_Fingers|Smoking)': None,
                'P(Yellow_Fingers|-Smoking)': None,
                'P(Anxiety)': None,
                'P(LC|Genetics,Smoking)': None,
                'P(LC|Genetics,-Smoking)': None,
                'P(LC|-Genetics,Smoking)': None,
                'P(LC|-Genetics,-Smoking)': None,
                'P(Peer_Pressure)': None,
                'P(Genetics)': None,
                'P(Attention_Disorder|Genetics)': None,
                'P(Attention_Disorder|-Genetics)': None,
                'P(Born_an_Even_Day)': None,
                'P(Car_Accident|Fatigue,Attention_Disorder)': None,
                'P(Car_Accident|Fatigue,-Attention_Disorder)': None,
                'P(Car_Accident|-Fatigue,Attention_Disorder)': None,
                'P(Car_Accident|-Fatigue,-Attention_Disorder)': None,
                'P(Fatigue|Lung_cancer,Coughing)': None,
                'P(Fatigue|Lung_cancer,-Coughing)': None,
                'P(Fatigue|-Lung_cancer,Coughing)': None,
                'P(Fatigue|-Lung_cancer,-Coughing)': None,
                'P(AL)': None,
                'P(Coughing|Allergy,Lung_cancer)': None,
                'P(Coughing|Allergy,-Lung_cancer)': None,
                'P(Coughing|-Allergy,Lung_cancer)': None,
                'P(Coughing|-Allergy,-Lung_cancer)': None,
            }
            # pairing = {
            #     'Smoking': 'S',
            #     'Yellow_Fingers': 'YF',
            #     'Anxiety': 'AN',
            #     'Peer_Pressure': 'PP',
            #     'Genetics': 'G',
            #     'Attention_Disorder': 'AD',
            #     'Born_an_Even_Day': 'BED',
            #     'Car_Accident': 'CO',
            #     'Fatigue': 'F',
            #     'Allergy': 'AL',
            #     'Coughing': 'CA',
            #     'Lung_cancer': 'LC',
            # }

class parsing():

    def __init__(self):
        pass

    def parse_data(self, data):

        data = data.replace("P(", "").replace(")", "").split("|")
        if len(data) > 1:
            query = data[0].split()
            evidence = data[1].split(",")
        return query, evidence

class PriorSampling:
    CPTs={}

    def __init__(self):
    	pass

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

        for variable in self.CPTs["order"]:
            evidence=""
            conditional=""
            parents=self.CPTs["parents"][variable]
            if parents==None:
                conditional=variable.lower()
            else:
                for parent in parents.split(","):
                    evidence+=sampledVars[parent]
                conditional=variable.lower()+"|"+evidence

            sampledValue=self.sampleVariable(self.CPTs[variable], conditional)
            event.append(sampledValue)
            sampledVars[variable]=sampledValue
                
        if printEvent: print(event)
        return event

