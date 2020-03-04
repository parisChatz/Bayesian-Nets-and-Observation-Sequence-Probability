# Bayesian Nets and Observation Sequence Probability

This is the the repository for the A.I. Assessment Item 1. Every task was implemented using python3. In this asignment there were three tasks presented bellow. 
* __Task 1.A (Task on probabilities and Bayes equation)__
Using the most appropriate AI methods and a suitable programming language, implement a software application to solve the Rare Disease and test problem.The result is the  probability of having the disease given the test was positive. (P(d|t)). For the solution the Bayes equation was calculated and for comparison purposes the rejection sampling was also implemented.
* __Task 1.B (Task on probabilities, parameter learning, approximate algorithms and Bayesian network)__
Using the most appropriate AI methods, implement a software application to solve a Medical Diagnosis problem similar to the Burglary problem explained during the lectures. The program should have as input the dataset and the Bayes Network structure shown in the link.
http://www.causality.inf.ethz.ch/data/LUCAS.html. The implementation presented, first learns its parameters from data (csv file) and then use inference method, specificaly sampling rejection and likelyhood weighting, to calculate the wanted probability distributions.
As an input the program first asks for the name of the wanted variable that needs to be claculated and then prompts the user to give the names of the evidences. The program print the calculated probabilities with the two aformentioned inference methods.
* __Task 2 (Task on Markov models and Observation Sequence)__
Implement a software application that, given in input any sequence of the bellow temperatures (i.e. the sequence can have any length), returns the probability of observing such sequence. Without any prior information, you can assume the initial states of the system to be equiprobable.
Consider a heater with two possible unknown states, ON and OFF, placed in a room where the measurable temperature can be Hot, Warm, or Cold.
The probability between two consecutive time instants of remaining in the same state is 0.7 (e.g. if ON at time t, there are 70% chances of being ON again at time t+1), while the probability of switching to a different state is 0.3.
In state ON, the probability of measuring a Warm or Hot temperature is 0.4, while the probability of measuring Cold is 0.2.
In state OFF, the probability of measuring a Warm or Cold temperature is 0.45, while the probability of measuring Hot is 0.1.
Initially the transition matrix and the emission matrix was coded. Then the program promts the user to give a sequence of any observations (eg. warm,hot,cold). Then using the sequence observation algorithm the probability of observing such a sequence is calculated.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
* pandas
* numpy
* collections
```

### Installing

A step by step series of examples that tell you how to get a development env running.

* Open a terminal and do
`git clone https://github.com/parisChatz/Bayesian-Nets-and-Observation-Sequence-Probability.git`
* Make sure to install the prerequisites.

To test that everything works right open a new terminal and do `python3 your_home/Bayesian-Nets-and-Observation-Sequence-Probability/Task_1A.py`. 
This should run the first task that solves the Rare Disease and test problem.
## Running 

The code of this project was segmented for better code management.
Each algorithm has each own script with apropriate naming (e.g. parameter learning). 
To run each task run the apropriate python scripts with python 3 (e.g. `python3 Task1_A.py`).

## Authors

 **Paraskevas Chatzithanos**  - [GitHub](https://github.com/parisChatz)


## License

This project is licensed under the "blank" License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used

