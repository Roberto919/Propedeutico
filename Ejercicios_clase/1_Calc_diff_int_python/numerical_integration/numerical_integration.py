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



# GLf: Gauss-Legendre quadrature for f
def GLf(f, a, b, n):
    """
    Compute numerical approximation using quadrature Gauss-Legendre.
    Weights and nodes are obtained with table for n=0,1,2,3,4
    Args:
        f (function): function expression of integrand
        a (int): left point of interval
        b (int): right point of interval
        n (int): number of subintervals
    Returns:
        sum_res (float): numerical approximation to integral of f in the interval a,b
    """


    ## List of calculated weights and node values (n = keys)
    wn_vals = {

        0: {
            'grade': 1,
            'vars': 2,
            'w': [2],
            'n': [0]
        },

        1: {
            'grade': 3,
            'vars': 4,
            'w': [1, 1],
            'n': [-np.sqrt(1/3), np.sqrt(1/3)]
        },

        2: {
            'grade': 5,
            'vars': 6,
            'w': [5/9, 8/9, 5/9],
            'n': [-np.sqrt(3/5), 0, np.sqrt(3/5)]
        },

        3: {
            'grade': 7,
            'vars': 8,
            'w': [0.347855, 0.652145, 0.652145, 0.347855],
            'n': [-0.861136, -0.339981, 0.339981, 0.861136]
        },

        4: {
            'grade': 9,
            'vars': 10,
            'w': [0.236927, 0.478629, 0.568889, 0.478629, 0.236927],
            'n': [-0.90618, -0.538469, 0, 0.538469, 0.90618]
        },
    }


    ## Approximation of the sum term
    sum_term = 0
    vals = len(wn_vals[n]['w'])
    for v in range(0, vals):
        sum_term += wn_vals[n]['w'][v]*f(0.5*((b - a)*wn_vals[n]['n'][v] + a + b))


    ## Obtaining final approximation result
    sum_res = (b - a)/2*sum_term


    return sum_res



## GHf: Gauss-Hermite quadrature for f
def GHf(f, mu, sigma):
    """
    Compute numerical approximation using quadrature Gauss-Hermite.
    Weights and nodes are obtained with table in Kiusalaas for n=6
        args:
            f (function): function expression of integrand
            mu (float): mean
            sigma (float): standard deviation
        returns:
            sum_res (float): numerical approximation to integral of f in the interval a,b
    """

    ## Default "n" value
    n = 5


    ## Nodes and weights for numerical approximation
    gausshermite_values = { ## Dict keys correspond to the value of "n"
        1: {
            'A_xs': {
                0.886227: [0.707107, -0.707107],
            }
        },
        2: {
            'A_xs': {
                1.181636: [0, -0],
                0.295409: [1.224745, -1.224745],
            }
        },
        3: {
            'A_xs': {
                0.804914: [0.524648, -0.524648],
                0.813128e-1: [1.650680, -1.650680],
            }
        },
        4: {
            'A_xs': {
                0.945308: [0, -0],
                0.393619: [0.958572, -0.958572],
                0.199532e-1: [2.020183, -2.020183],
            }
        },
        5: {
            'A_xs': {
                0.724629: [0.436077, -0.436077],
                0.157067: [1.335849, -1.335849],
                0.453001e-2: [2.350605, -2.350605]
            }
        },
    }


    ## Calculation of area approximate
    sum_res = 0 
    for weight in gausshermite_values[n]['A_xs']:
        for node in gausshermite_values[n]['A_xs'][weight]:
            sum_res += weight*f(node)



    return sum_res
