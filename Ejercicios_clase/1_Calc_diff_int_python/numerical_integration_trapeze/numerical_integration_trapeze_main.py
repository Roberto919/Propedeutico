## NUMERICAL INTEGRATION - MAIN EXECUTION FILE
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
from numerical_integration_trapeze_functions import *
from numerical_integration_trapeze_parameters import *





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
    print(Tcf(f, a, b, n))


    return





'--------------------------------------------------------------------------------'
#################################
## Excecution of main function ##
#################################


if __name__ == '__main__':

    main_function()
