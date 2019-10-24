# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:56:26 2019

@author: Marek
"""

import numpy as np
import itertools


class Checks(object):
    """Mix-in class containing input value checking functions."""

    def _check_increments(self, n):
        if not isinstance(n, int):
            raise TypeError("Number of increments must be an integer.")
        if n <= 0:
            raise ValueError("Number of increments must be positive.")

    def _check_number(self, value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(name + " value must be a number.")

    def _check_positive_number(self, value, name):
        self._check_number(value, name)
        if value <= 0:
            raise ValueError(name + " value must be positive.")

    def _check_nonnegative_number(self, value, name):
        self._check_number(value, name)
        if value < 0:
            raise ValueError(name + " value must be nonnegative.")

    def _check_zero(self, zero):
        if not isinstance(zero, bool):
            raise TypeError("Zero inclusion flag must be a boolean.")
            

def concat_arrays(l):
    """Concatenate a list of numpy arrays"""
    pol = []
    [pol.append(list(j)) for j in l]
    pol = list(itertools.chain.from_iterable(pol))
    return np.array(pol)
