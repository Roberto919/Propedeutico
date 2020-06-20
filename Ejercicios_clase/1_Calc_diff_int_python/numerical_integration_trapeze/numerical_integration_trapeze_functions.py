## NUMERICAL INTEGRATION - FUNCTIONS FILE
#### Based on excercise from file *1_aproximacion_a_derivadas_e_integrales*
#### Author: Rob (GitHub: Roberto919)
#### Date: 19 June 2020





'--------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries
import numpy as np
import math





'--------------------------------------------------------------------------------'
###############
## Functions ##
###############


## Tcf: composite trapezoidal method for f
def Tcf(f, a, b, n):
    """
    Compute numerical approximation using trapezoidal method in
    an interval.
    Nodes are generated via formula: x_i = a+i*h_hat for i=0,1,...,n and h_hat=(b-a)/n; h = (b - a)
        args:
            f (function): function expression of integrand
            a (int): left point of interval
            b (int): right point of interval
            n (int): number of subintervals
        returns:
            sum_res (float): numerical approximation to integral of f in the interval a,b
    """

    ## Constants
    h = (b - a)
    h_hat = (b - a)/n
    x_0 = 0
    x_n = math.pi


    ## Finding sum of x_i
    sum_fxi = 0
    for i in np.linspace(1, (n - 1), (n - 1)):

        x_i = a + i*h_hat

        sum_fxi += f(x_i)


    ## Estimating integral value
    approx_area_trapeze = h/(2*n)*(f(x_0) + f(x_n) + 2*sum_fxi)


    return approx_area_trapeze
