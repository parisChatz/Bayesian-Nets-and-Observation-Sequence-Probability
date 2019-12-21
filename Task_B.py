#!/usr/bin/env python3

import numpy as np

u0 = np.array([0.5, 0.5])
transision_vector = np.array([0.7, 0.3])
u_warm = np.array([0.4, 0.45])
u_cold = np.array([0.2, 0.45])
u_hot = np.array([0.4, 0.1])

s0 = u0.transpose()

transision_matrix = np.concatenate(
    [[transision_vector], [1 - transision_vector]])

O_warm = np.diag(u_warm)
O_cold = np.diag(u_cold)
O_hot = np.diag(u_hot)

evidences = str(input("Input the evidences (comma seperated):"))
evidences = evidences.upper().split(",")

evid_to_obs = {
    "WARM": O_warm,
    "HOT": O_hot,
    "COLD": O_cold
}

for item in evidences:
    s0 = evid_to_obs[item].dot(transision_matrix.transpose()).dot(s0)

print("The probability of observing such sequence is :", sum(s0))
