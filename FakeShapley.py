from modules import compute_ssi
import itertools
from fractions import Fraction 
from math import factorial
import time


iterations = 0


def main():
    test = []
    start = 100
    num = 20
    quota = 0
    for i in range(start, start + num):
        test.append(i)
        quota += i

    if quota % 2 == 1:
        quota = (quota / 2) + 1/2
    else: 
        quota = (quota / 2) 
    print(quota)
    PowerIndex = compute_ssi(int(quota), test)
    # print('power index: ', PowerIndex)
    # PowerFractions = []
    # for i in PowerIndex[1]:
    #     PowerFractions.append(str(Fraction(i[0],i[1])))
    # print ('power fractions: ', PowerFractions)
        

if __name__ == "__main__": 
    main()