import numpy as np
from math import sqrt

## Supposition: lenght of the input N = 2^J
## The scale is determined by N

def one_DDWT(input,scale):
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


def inverse_one_DDWT(input,scale):
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

# list = np.array([1,4,-3,0,1,4,-3,0],dtype=float)
# transform = one_DDWT(list,scale=3)
# inverse = inverse_one_DDWT(transform,scale=3)
# print(list,transform,inverse)