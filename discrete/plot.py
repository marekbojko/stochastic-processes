# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 12:04:29 2019

@author: Marek
"""
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from bernoulli import *
from utils import *

plt.style.use('bmh')
sns.set_style('darkgrid')

def make_plot_draws(title, fname, x, ys, xlabel="Time", ylabel="Value", scatter=False, alt=False):
    fig, ax = plt.subplots(1, 2, figsize=(8, 4))
    if alt:
        for y in ys:
            if scatter:
                ax.scatter(y, range(len(y)))
            else:
                ax.plot(y, range(len(y)))
    else:
        for y in ys:
            if scatter:
                ax.scatter(x, y)
            else:
                ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig("figures/{}.jpg".format(fname))
    print(title + " saved")
    plt.close()
    
def plot_hist(title, fname, vals, xlabel="Values", ylabel="Frequency"):
    fig = sns.distplot(vals)
    fig.set_title(title)
    fig.set_xlabel(xlabel)
    fig.set_ylabel(ylabel)
    plt.tight_layout()
    plt.savefig("figures/{}.jpg".format(fname))
    print(title + " saved")
    print('Mean %f; sd: %f' %(np.mean(vals),math.sqrt(np.var(vals))))
    plt.close()

def get_samples(num, process, args, pooled = False):
    samples = []
    for k in range(num):
        samples.append(process.sample(**args))
    if pooled:
        pol = concat_arrays(samples)
        return samples, pol
    return samples

def get_cumulative_samples(num,process, args, pooled = False):
    c_samples = []
    for k in range(num):
        c_samples.append(process.cumulative_sample(**args))
    if pooled:
        pol = concat_arrays(c_samples)
        return c_samples, pol
    return c_samples