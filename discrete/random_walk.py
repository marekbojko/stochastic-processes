# -*- coding: utf-8 -*-
"""
Random walks

@author: Marek
"""

import numpy as np
from utils import *

class RandomWalk(Checks):
    def __init__(self,  p = 0.5, steps=[-1, 1], weights=None):
        self.steps = steps
        length = len(steps)
        if length < 1:
            raise ValueError("Steps must have at least one element.")
        if weights is None:
            self.weights = [1 for s in steps]
            self.p = [p for s in steps]
        else:
            if len(weights) != length:
                raise ValueError(
                    "Steps and probabilities must have same length.")
            self.weights = weights
            total = sum(weights)
            self.p = [1.0 * w / total for w in weights]

    @property
    def p(self):
        """Step probabilities, normalized from :py:attr:`weights`."""
        return self._p

    @p.setter
    def p(self, values):
        values = np.array(values, copy=True)
        self._p = values

    @property
    def steps(self):
        """Possible steps."""
        return self._steps

    @steps.setter
    def steps(self, values):
        for value in values:
            if not isinstance(value, int) and not isinstance(value, float):
                raise TypeError("Step values must be numeric.")
        values = np.array(values, copy=True)
        self._steps = values

    @property
    def weights(self):
        """Step weights provided."""
        return self._weights

    @weights.setter
    def weights(self, values):
        for value in values:
            if not isinstance(value, (int, float)):
                raise TypeError("Weight values must be numeric.")
            if value < 0:
                raise ValueError("Weight values must be nonnegative.")
        values = np.array(values, copy=True)
        self._weights = values

    def __str__(self):
        return "Random walk steps = {s} and p = {p}".format(
            s=str(self.steps),
            p=str(self.p)
        )

    def __repr__(self):
        return "RandomWalk(steps={s}, p={p})".format(
            s=str(self.steps),
            p=str(self.p)
        )

    def _sample_random_walk(self, n, zero=True):
        """Generate a random walk."""
        if zero:
            return np.array(
                [0] + list(np.cumsum(self._sample_random_walk_increments(n)))
            )
        else:
            return np.cumsum(self._sample_random_walk_increments(n))

    def sample(self, n, zero=True):
        return self._sample_random_walk(n, zero)

    def _sample_random_walk_increments(self, n):
        """Generate a sample of random walk increments."""
        self._check_increments(n)
        return np.random.choice(self.steps, p=self.p, size=n)

    def sample_increments(self, n):
        """Generate a sample of random walk increments.
        """
        return self._sample_random_walk_increments(n)