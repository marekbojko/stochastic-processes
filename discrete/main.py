# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:41:01 2019

@author: Marek
"""

from bernoulli import *
from plot import *
from random_walk import *
import os
os.chdir('C://Users//Marek//Documents//Stochastic processes//discrete')

def main():
    n_samples = 10
    n = 10**4
    
    process = BernoulliProcess(p=0.5)
    c_samples, pol = get_cumulative_samples(n_samples,process,{"n":n},pooled = True)
    make_plot("Bernoulli process", "cumulative_bernoulli", list(range(n)), c_samples)
    plot_hist("Histogram Bernoulli process", "hist_bernoulli", pol)
    
    walk = RandomWalk(p=0.5)
    samples, pol = get_samples(n_samples,walk,{"n":n},pooled = True)
    make_plot("Random Walk", "random_walk", list(range(n+1)), samples)
    plot_hist("Histogram of the random walk", "hist_rw", pol)
    
if __name__ == '__main__':
    main()