#!/usr/bin/env python3

# Consider a heater with two possible unknown states, ON and OFF,
# placed in a room where the measurable temperature can be Hot, Warm, or Cold.
# The probability between two consecutive time instants of remaining
# in the same state is 0.7 (e.g. if ON at time t, there are 70%
# chances of being ON again at time t+1), while the probability of
# switching to a different state is 0.3.
# In state ON, the probability of measuring a Warm or Hot temperature
# is 0.4, while the probability of measuring Cold is 0.2.
# In state OFF, the probability of measuring a Warm or Cold temperature
# is 0.45, while the probability of measuring Hot is 0.1.

# Implement and explain in the report a software application that,
# given in input any sequence of the above temperatures
# (i.e. the sequence can have any length), returns the probability of
# observing such sequence. Without any prior information,
# you can assume the initial states of the system to be equiprobable

import numpy as np

initial_states = np.array([0.5, 0.5])
transision_vector = np.array([0.7, 0.3])
u_warm = np.array([0.4, 0.45])
u_cold = np.array([0.2, 0.45])
u_hot = np.array([0.4, 0.1])

sequence_prob = initial_states.transpose()

transision_matrix = np.concatenate(
    [[transision_vector], [1 - transision_vector]])

O_warm = np.diag(u_warm)
O_cold = np.diag(u_cold)
O_hot = np.diag(u_hot)

evidences = str(input("Input the evidences (comma seperated):"))
evidences = evidences.upper().split(",")

observed_sequence = {
    "WARM": O_warm,
    "HOT": O_hot,
    "COLD": O_cold
}

for item in evidences:
    sequence_prob = observed_sequence[item].dot(
        transision_matrix.transpose()).dot(sequence_prob)

print("The probability of observing such sequence is :", sum(sequence_prob))
