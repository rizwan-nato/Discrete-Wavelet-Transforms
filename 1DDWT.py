import numpy as np
from math import sqrt

def one_DDWT(input,l = -1):
    if (l==-1):
        l = int(len(input) / 2)
    if(l==0):
        return input
    else:
        output = np.copy(input)
        for i in range(l):
            sum = (input[2*i] + input[2*i+1])/sqrt(2)
            difference = (input[2*i] - input[2*i+1])/sqrt(2)
            print(sum,difference)
            output[i] = sum
            output[l+i] = difference
    return one_DDWT(output,int(l/2))

input = np.array([1,4,-3,0],dtype=float)
print(one_DDWT(input))

def inverse_one_DDWT(input):

    return input
