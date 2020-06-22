## NUMERICAL INTEGRATION - PARAMETERS FILE
#### Based on excercise from file *1_aproximacion_a_derivadas_e_integrales*
#### Author: Rob (GitHub: Roberto919)
#### Date: 19 June 2020





'--------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries
import math





'--------------------------------------------------------------------------------'
################
## Parameters ##
################


## Function whose first and second derivatives will be calculated
f = math.sin

## Left point of interval
a = 0

## Right point of interval
b = math.pi

## Number of intervals
n = 10**4

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
