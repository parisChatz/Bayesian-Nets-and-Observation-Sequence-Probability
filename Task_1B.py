#!/usr/bin/env python3

from approximate_algorithms import Likelihood_Weighting_algorithm
from approximate_algorithms import Rejection_Sampling_algorithm
from networks import networks

# class create_cpt():
#     def __init__(self):

        # known_data = {
  #               'P(Smoking|Anxiety,Peer_Pressure)': None,
  #               'P(Smoking|Anxiety,-Peer_Pressure)': None,
  #               'P(Smoking|-Anxiety,Peer_Pressure)': None,
  #               'P(Smoking|-Anxiety,-Peer_Pressure)': None,
  #               'P(Yellow_Fingers|Smoking)': None,
  #               'P(Yellow_Fingers|-Smoking)': None,
  #               'P(Anxiety)': None,
  #               'P(LC|Genetics,Smoking)': None,
  #               'P(LC|Genetics,-Smoking)': None,
  #               'P(LC|-Genetics,Smoking)': None,
  #               'P(LC|-Genetics,-Smoking)': None,
  #               'P(Peer_Pressure)': None,
  #               'P(Genetics)': None,
  #               'P(Attention_Disorder|Genetics)': None,
  #               'P(Attention_Disorder|-Genetics)': None,
  #               'P(Born_an_Even_Day)': None,
  #               'P(Car_Accident|Fatigue,Attention_Disorder)': None,
  #               'P(Car_Accident|Fatigue,-Attention_Disorder)': None,
  #               'P(Car_Accident|-Fatigue,Attention_Disorder)': None,
  #               'P(Car_Accident|-Fatigue,-Attention_Disorder)': None,
  #               'P(Fatigue|Lung_cancer,Coughing)': None,
  #               'P(Fatigue|Lung_cancer,-Coughing)': None,
  #               'P(Fatigue|-Lung_cancer,Coughing)': None,
  #               'P(Fatigue|-Lung_cancer,-Coughing)': None,
  #               'P(AL)': None,
  #               'P(Coughing|Allergy,Lung_cancer)': None,
  #               'P(Coughing|Allergy,-Lung_cancer)': None,
  #               'P(Coughing|-Allergy,Lung_cancer)': None,
  #               'P(Coughing|-Allergy,-Lung_cancer)': None,
  #           }
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

    def parse_prob(self, data):

        data = data.replace("P(", "").replace(")", "").split("|")
        if len(data) > 1:
            query = data[0].split()
            evidence = data[1].split(",")
        return query, evidence

    def parse_children(self,children):
        new_children = []
        
        for child in children:
            if child == None:
                new_children.append(None)
            elif len(child) == 1:
                new_children.append(child)
            else:
                child = child.split(",")
                new_children.append(child)

        return new_children

if __name__ == "__main__":



    net = networks().initialiseNet("disease")

    lw = Likelihood_Weighting_algorithm(net)
    lw_result = lw.likelihood_weighting('D',['-t'])
    sr = Rejection_Sampling_algorithm(net)
    sr_result = lw.likelihood_weighting('D',['-t'])

    print(lw_result)
    print(sr_result)