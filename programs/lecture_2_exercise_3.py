from __future__ import division
from random import uniform
from math import sqrt

def pi_approx(n):
    count = 0
    for i in range(n):
        x = uniform(0,1) - 0.5
        y = uniform(0,1) - 0.5
        z = sqrt(x*x+y*y)
        if z < 0.5:
            count +=1
    guess = 4*count/n
    return guess

pi_guess = pi_approx(1000000)
print pi_guess