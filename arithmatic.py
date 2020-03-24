# from modules import compute_ssi
import itertools
from fractions import Fraction
from math import factorial
import time
import powerindices as pi


iterations = 0


def main():

    PowerArray = []
    start_num = 1
    end_num = 5

    start_step = 1
    end_step = 4

    start_length = 1
    end_length = 5

    for length in range(start_length, end_length + 1):
        print("\n")
        print("length = ", length)
        # print('\n')

        for step_size in range(start_step, end_step + 1):
            print("\n")
            print("d = ", step_size)

            for a in range(start_num, end_num + 1):

                PowerArray = [a]
                for i in range(1, length):
                    PowerArray.append((i) * step_size + a)
                # just need to get power of PowerArray and print it
                print(PowerArray)


if __name__ == "__main__":
    main()
