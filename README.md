# Artificial Intelligence (CMP9132M) Assessment Item 1

This is the the repository for the A.I. Assessment Item 1. Every task was implemented using python3. In this asignment there were three tasks presented bellow. 

## Task 1.A
Using the most appropriate AI methods and a suitable programming language, implement a software application to solve the Rare Disease and test problem.

The program has as input the following probabilities:
* P( d ) : prior probability of having a disease
* P( t | d ) : probability that the test is positive given the person has the disease
* P( ¬t | ¬d) : probability that the test is negative given the person does not have the disease

Where the meaning of the variables are:
1. d: the person has the disease.
2. t: the test is positive.

The result is the  probability of having the disease given the test was positive. (P(d|t))

For the solution the Bayes equation was calculated and for comparison purposes the rejection sampling was also implemented.

## Task 1.B
Using the most appropriate AI methods, implement a software application to solve a Medical Diagnosis problem similar to the Burglary problem explained during the lectures. The program should have as input the dataset and the Bayes Network structure shown in the link below.
http://www.causality.inf.ethz.ch/data/LUCAS.html

The implementation presented in this report, first learns its parameters from data (svs file) and then use inference method, specificaly sampling rejection and likelyhood weighting, to calculate the wanted probability distributions.

As an input the program first asks for the name of the wanted variable that needs to be claculated and then prompts the user to give the names of the evidences. The program print the calculated probabilities with the two aformentioned inference methods.

## Task 2
Implement a software application that, given in input any sequence of the bellow temperatures (i.e. the sequence can have any length), returns the probability of observing such sequence. Without any prior information, you can assume the initial states of the system to be equiprobable.

### Problem presentation 
Consider a heater with two possible unknown states, ON and OFF, placed in a room where the measurable temperature can be Hot, Warm, or Cold.
The probability between two consecutive time instants of remaining in the same state is 0.7 (e.g. if ON at time t, there are 70% chances of being ON again at time t+1), while the probability of switching to a different state is 0.3.
In state ON, the probability of measuring a Warm or Hot temperature is 0.4, while the probability of measuring Cold is 0.2.
In state OFF, the probability of measuring a Warm or Cold temperature is 0.45, while the probability of measuring Hot is 0.1.

### Problem formalisation
Initially the transition matrix and the emission matrix was coded. Then the program promts the user to give a sequence of any observations (eg. warm,hot,cold). Then using the sequence observation algorithm the probability of observing such a sequence is calculated.

` St = P(et|xt)* Σxt-1(P(xt|xt-1)*st-1)`
