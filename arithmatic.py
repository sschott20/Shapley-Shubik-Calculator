# from modules import compute_ssi
import itertools
from fractions import Fraction
from math import factorial
import time
import powerindices as pi


iterations = 0


def main():

    PowerArray = []
    # filename = "arithmatic_data/"

    start_num = 1
    end_num = 50

    start_step = 1
    end_step = 30

    start_length = 4
    end_length = 10

    quota = 0 
    for length in range(start_length, end_length + 1):
        print("length = ", length)

        for step_size in range(start_step, end_step + 1):
            # print("\n")
            # print("d = ", step_size)

            filename = "arithmatic_data/" + str(length)+ "-"+str(step_size) + ".txt"
            file = open(filename, "a")
            file.truncate(0)

            for a in range(start_num, end_num + 1):

                PowerArray = [a]
                for i in range(1, length):
                    PowerArray.append((i) * step_size + a)

                for voter in PowerArray:
                    quota += voter
                    if quota % 2 == 1:
                        quota = (quota / 2) + 1 / 2
                    else:
                        quota = quota / 2

                file.write("\n")
                file.write(str(pi.compute_ssi(int(quota), PowerArray)))
                file.write("\n")
                file.write(str(pi.compute_pbi(int(quota), PowerArray)))
                file.write("\n")

                # print("\n")
                # print(PowerArray)        
                # print(pi.compute_ssi(int(quota), PowerArray))
                # print(pi.compute_pbi(int(quota), PowerArray))
                # print("\n")

                



if __name__ == "__main__":
    main()
