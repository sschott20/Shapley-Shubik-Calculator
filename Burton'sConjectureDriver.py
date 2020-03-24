# from modules import compute_ssi
import itertools
from fractions import Fraction
from math import factorial
import time

# import powerindices as pi
from modules import compute_pbi

iterations = 0


def main():
    amax = 15
    pairs = 7
    DataList = []

    for a in range(1, amax):
        for b in range(1, amax):
            for c in range(1, amax):

                voters = create_list([a, b, c])
                quota = 0
                final = []

                for voter in voters:
                    quota += voter
                if quota % 2 == 1:
                    quota = (quota / 2) + 1 / 2
                else:
                    quota = quota / 2

                pbi = compute_pbi(int(quota), voters)

                cumsum = pbi[1]
                pbi = pbi[0]

                for i in pbi:
                    final.append(str(Fraction(i, cumsum)))
                print(voters, final)


def create_list(arr):
    final = []
    for i in arr:
        final.append(i)
        final.append(i)
    return final


if __name__ == "__main__":
    main()
