## CENTRAL FINITE DIFFERENCES EXCERCISE - MAIN EXECUTION FILE
#### Based on excercise from file *1_aproximacion_a_derivadas_e_integrales*
#### Author: Rob (GitHub: Roberto919)
#### Date: 19 June 2020





'--------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries
import numpy as np

## Ancillary modules
# from CentralFiniteDerivative_ex3_functions import approx_first_derivative \
#                                                   approx_second_derivative
from central_finite_derivative_functions import *
from central_finite_derivative_parameters import fun, x, h





'--------------------------------------------------------------------------------'
#################################
## Definition of main function ##
#################################


## Main module's function
def main_function():
    """
    Main module's function
        args:
            -
        returns:
            -
    """


    ## Obtain the first derivative approximation
    print(approx_first_derivative(fun, x, h))

    ## Obtain the second derivative approximation
    print(approx_second_derivative(fun, x, h))


    return()





'--------------------------------------------------------------------------------'
#################################
## Excecution of main function ##
#################################


if __name__ == '__main__':

    main_function()
