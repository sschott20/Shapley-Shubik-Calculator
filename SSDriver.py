# from modules import compute_ssi
import itertools
from fractions import Fraction 
from math import factorial
import time
import powerindices as pi 



iterations = 0


def main():
    test = []
    start = 3
    amax = 100
    quota = 0    
    
    DataList = []
    # print('aya: ', pi.compute_ssi(2,[1,2]))
    for num in range(3, 20, 2):
        total_time = time.time()
        filename = 'SSoneIter' + str(num) + '.txt'
        # filename = "test.txt"
        # print ('lets get litty with it')
        DataFile = open(filename, 'a')
        DataFile.truncate(0)
        # DataFile.truncate(0)
        DataList = []
        # DataListFinal = []
        for i in range(amax):
            start_time = time.time()
            test = []
            quota = 0
            for j in range(num):
                test.append(i + j)
            # print("Start: ",test)

            for voter in test:
                quota += voter
            if quota % 2 == 1:
                quota = (quota / 2) + 1/2
            else: 
                quota = (quota / 2) 
            DataList.append( pi.compute_ssi(int(quota), test))
        
            # DataFile.write(str(pi.compute_ssi(int(quota), test)))
            # DataFile.write('\n')
            # print("--- {:f} secconds ---".format(time.time() - start_time))
            # print("data list: ", DataList)

        unit = '1/' + str(num)

        for data in DataList:
            for i in range(len(data)):
                if data[i] == 1 / num: 
                    data[i] = unit
                # i = Fraction(1, num)
            DataFile.write(str(data))
            DataFile.write('\n')

        print('\n')
        print('--- LENGTH: {:d} ---'.format(num))
        # print('--- CONVERGE: {:d} ---'.format(FlipDex))
        print("--- TOTAL TIME: {:f} secconds ---".format(time.time() - total_time))
        print('\n')
    # print(quota)
    # PowerIndex = compute_ssi(int(quota), test)

    # print (pi.compute_ssi(int(quota), test)[0])
    # print (1/num)

    # print ('Mebrary: ', compute_ssi(int(quota), test)[0][0])
    # print('power index: ', PowerIndex)
    # PowerFractions = []
    # for i in PowerIndex[1]:
    #     PowerFractions.append(str(Fraction(i[0],i[1])))
    # print ('power fractions: ', PowerFractions)
    
if __name__ == "__main__": 
    main()