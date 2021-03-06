# from modules import compute_ssi
import itertools
from fractions import Fraction
from math import factorial
import time

# import powerindices as pi
from modules import compute_pbi

iterations = 0


def main():

    test = []
    start = 3
    amax = 200
    limit = 25
    quota = 0

    DataList = []
    FirstConverge = []
    total_time = time.time()

    for num in range(2, limit, 2):
        converged = False
        start_time = time.time()
        filename = "BanEvenOneIterFrac" + str(num) + ".txt"

        DataFile = open(filename, "a")
        DataFile.truncate(0)
        DataList = []

        for i in range(1, amax):
            test = []
            quota = 0
            for j in range(num):
                test.append(i + j)
            # print("Start: ",test)

            for voter in test:
                quota += voter
            if quota % 2 == 1:
                quota = (quota / 2) + 1 / 2
            else:
                quota = quota / 2

            pbi = compute_pbi(int(quota), test)

            cumsum = pbi[1]
            pbi = pbi[0]
            final = []
            if i == amax - 1:
                FirstConverge.append(str(cumsum) + str(pbi))
            # if pbi[0]/cumsum == 1/num and converged == False:
            #     # print('converge:', num, i)
            #     FirstConverge.append([num, i + 1])
            #     converged = True

            for i in pbi:
                final.append(str(Fraction(i, cumsum)))
            # final.append(str(cumsum) + str(pbi))
            # print(final)
            DataList.append(final)
            # if converged == True:
            # break

        # unit = '1/' + str(num)

        for data in DataList:
            DataFile.write(str(data))
            DataFile.write("\n")
        print("\n")
        print("--- LENGTH: {:d} ---".format(num))
        # print('--- CONVERGE: {:d} ---'.format(FlipDex))
        print("--- TIME: {:f} secconds ---".format(time.time() - start_time))
        print("\n")
    ConvergeFile = open("EvenBanConverge.txt", "a")
    ConvergeFile.truncate(0)
    for i in FirstConverge:
        ConvergeFile.write(str(i))
        ConvergeFile.write("\n")

    print("\n")
    print("--- TOTAL TIME: {:f} secconds ---".format(time.time() - total_time))
    print("\n")


if __name__ == "__main__":
    main()
