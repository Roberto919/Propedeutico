## CENTRAL FINITE DIFFERENCES EXCERCISE - FUNCTIONS FILE
#### Based on excercise from file *1_aproximacion_a_derivadas_e_integrales*
#### Author: Rob (GitHub: Roberto919)
#### Date: 19 June 2020





'--------------------------------------------------------------------------------'
###############
## Functions ##
###############


## Function to approximate the first derivative through central differences
def approx_first_derivative(fun, x, h):
    """
    Function to approximate the first derivative through central differences
        args:
            fun (function): function that will be approximated
            x (float): value where the function will be centered
            h (float): finite step that will be taken to evaluate de function
    """

    df = (fun(x + h) - fun(x - h))/(2*h)

    return df



## Function to approximate the second derivative through central differences
def approx_second_derivative(fun, x, h):
    """
    Function to approximate the second derivative through central differences
        args:
            fun (function): function that will be approximated
            x (float): value where the function will be centered
            h (float): finite step that will be taken to evaluate de function
    """

    ddf = (fun(x + 2*h) - 2*fun(x + h) + fun(x))/h**2

    return ddf
