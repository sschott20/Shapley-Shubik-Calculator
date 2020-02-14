import powerindices

import itertools
from fractions import Fraction 
from math import factorial
import time

iterations = 0


def main():
    test = [.2,.2,.2,.2,.2]
    quota = 0

    # for i in range(15, 15+9):
        # test.append(i)

    for voter in test:
        # print(voter, "  voters: ",voters)
        quota += voter
    if quota == 1:
        quota /= 2
    elif quota % 2 == 1:
        quota = (quota / 2) + 1/2
    else: 
        quota = (quota / 2) 

    quota = 1
    print(powerindices.compute_ssi(quota, test))

if __name__ == "__main__": 
    main()