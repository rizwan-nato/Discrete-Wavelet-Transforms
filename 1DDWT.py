import numpy as np
from math import sqrt


def one_DDWT(input):
    l = len(input) // 2
    while l != 0:
        output = np.copy(input)
        for i in range(l):
            sum = (input[2 * i] + input[2 * i + 1]) / sqrt(2)
            difference = (input[2 * i] - input[2 * i + 1]) / sqrt(2)
            output[i] = sum
            output[l + i] = difference
        input = np.copy(output)
        l = l // 2
    return output


def inverse_one_DDWT(input):
    N = int(len(input))
    l=0
    while l != N:
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

input = np.array([1, 4, -3, 0], dtype=float)
print(one_DDWT(input))
print(inverse_one_DDWT(one_DDWT(input)))
