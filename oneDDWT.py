import numpy as np
from math import sqrt

## Supposition: lenght of the input N = 2^J

def one_DDWT(list,scale):
    input = np.copy(list)
    l = len(input) // 2
    while (l != 0 ):
        output = np.copy(input)
        for i in range(l):
            sum = (input[2 * i] + input[2 * i + 1]) / sqrt(2)
            difference = (input[2 * i] - input[2 * i + 1]) / sqrt(2)
            output[i] = sum
            output[l + i] = difference
        input = np.copy(output)
        l = l // 2
        scale -= 1
        if scale == 0:
            break
    return output


def inverse_one_DDWT(list,scale):
    input = np.copy(list)
    N = int(len(input))
    max_scale = np.log(N)/np.log(2)
    nb_to_skip = max_scale - scale
    l=0
    while l != N:
        if nb_to_skip >= 0:
            nb_to_skip-=1


        else:
            output = np.copy(input)
            for i in range(l):
                sum = input[i] * sqrt(2)
                difference = input[l+i] * sqrt(2)
                output[2*i] = (sum + difference)/2
                output[2*i+1] = (sum - difference)/2

            input = np.copy(output)

        if l == 0:
            l =1
        else:
            l = l * 2

    return output