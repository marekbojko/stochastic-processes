# -*- coding: utf-8 -*-
"""
Bernoulli process

@author: Marek
"""


"""Bernoulli process."""

import numpy as np
from utils import *


class BernoulliProcess(Checks):
    def __init__(self, p=0.5):
        self.p = p

    def __str__(self):
        return "Bernoulli process with p={p}.".format(p=str(self.p))
    
    def __repr__(self):

        return "BernoulliProcess({p})".format(p=str(self.p))

    @property
    def p(self):
        """Probability of success."""
        return self._p

    @p.setter
    def p(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(
                "Probability of success must be a number between 0 and 1.")

        if value < 0 or value > 1:
            raise ValueError(
                "Probability of success p must be between 0 and 1.")
        self._p = value

    def _sample_bernoulli(self, n):
        """Generate a Bernoulli process realization."""
        self._check_increments(n)
        return np.array([1 if trial > self.p else 0 for trial in np.random.uniform(size=n)])

    def sample(self, n):
        """Generate a Bernoulli process realization.
        :param int n: the number of steps to simulate.
        """
        return self._sample_bernoulli(n)
    
    def cumulative_sample(self,n):
        """Generate a Bernoulli process and output sum of Bernoulli rand vars
        """
        sequence = self.sample(n)
        return np.array([np.sum(sequence[:j]) for j in range(n)])
    