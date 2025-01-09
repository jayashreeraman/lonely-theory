"""

Problem:

Assume you have access to a function toss_biased() which returns 0 or 1 with a
probability that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of
the coin.

Write a function to simulate an unbiased coin toss.
"""

from random import random
import matplotlib.pyplot as plt

def toss_biased():
    # toss with 30-70 bias
    r = random()

    if r < 0.3:
        return 0
    return 1

def toss_unbiased():
    # getting the biased toss value twice
    toss1 = toss_biased()
    toss2 = toss_biased()

    # as long as we dont get different values, we keep tossing
    while toss1 ==toss2:
        toss1 = toss_biased()
        toss2 = toss_biased()
    return toss1



