#!/usr/bin/env python3

# from numpy import random
from collections import OrderedDict
import sys
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler())

transitions = {
    'feelings': ['WARM', 'WARM', 'HOT', 'WARM', 'COLD'],
    'hidden_states': ['ON', 'OFF'],
    'observations': ['HOT', 'WARM', 'COLD'],
    'ON': {
        'init': 1.0 / 2,
        'trans': {
            'ON': 0.7,
            'OFF': 0.3,
            'HOT': 0.4,
            'WARM': 0.4,
            'COLD': 0.2,
        },
    },
    'OFF': {
        'init': 1.0 / 2,
        'trans': {
            'ON': 0.3,
            'OFF': 0.7,
            'HOT': 0.1,
            'WARM': 0.45,
            'COLD': 0.45,
        },
    },
}

# transitions = {
#     'feelings': ['mama', 'mama', 'peepee', 'peepee'],
#     'hidden_states': ['CLEAN', 'DIRTY'],
#     'observations': ['mama', 'papa', 'peepee', 'poopoo'],
#     'CLEAN': {
#         'init': 1.0 / 2,
#         'trans': {
#             'CLEAN': 0.5,
#             'DIRTY': 0.8,
#             'mama': 0.4,
#             'papa': 0.4,
#             'poopoo': 0.1,
#             'peepee': 0.1,
#         },
#     },
#     'DIRTY': {
#         'init': 1.0 / 2,
#         'trans': {
#             'CLEAN': 0.5,
#             'DIRTY': 0.2,
#             'mama': 0.1,
#             'papa': 0.1,
#             'poopoo': 0.4,
#             'peepee': 0.4,
#         },
#     },
# }



# Calculate path for each of the hidden states
path = [[transitions[hidden_state]['init'] for hidden_state in transitions['hidden_states']]]

for num, feel in enumerate(transitions['feelings']):
    probs_max = OrderedDict()
    for hidden_state in transitions['hidden_states']:
        for tmp_hidden in transitions['hidden_states']:
            yesterday_probs = dict(zip(transitions['hidden_states'], path[-1]))
            p1 = transitions[hidden_state]['trans'][feel]
            p2 = transitions[hidden_state]['trans'][tmp_hidden]
            p3 = yesterday_probs[tmp_hidden]

            reslt = p1 * p3 * p2
            logger.debug('  {} - {}: {} * {} * {} = {}'.format(
                hidden_state,
                tmp_hidden,
                p1,
                p2,
                round(p3, 3),
                round(reslt, 3),
            ))
            probs_max.setdefault(hidden_state, []).append(reslt)

    # logger.debug(dict(probs_max))
    probs_fixed = OrderedDict()
    prob_sum = 0
    for key, probs in probs_max.items():
        probs_fixed[key] = max(probs)
        prob_sum += max(probs)

    if num == 0:
        path = []
        for key, prob in probs_fixed.items():
            probs_fixed[key] = prob / prob_sum

    path.append([prob for prob in probs_fixed.values()])
    logger.debug('{}, {}'.format(feel, dict(probs_fixed)))

# Calculate the probability and most likely path
logger.debug('\n')
prob = 1
most_likely_path = []
for num, hidden_probabilities in enumerate(path, start=1):
    likelihood = dict(zip(transitions['hidden_states'], hidden_probabilities))
    most_likely = max(likelihood, key=likelihood.get)
    most_likely_path.append(most_likely)
    logger.info('{}) {}: {}'.format(num, most_likely, likelihood))
    prob *= likelihood[most_likely]

logger.info('most likely path: {0}'.format(most_likely_path))
logger.info('most likely probability: {0:.10f}'.format(prob))
