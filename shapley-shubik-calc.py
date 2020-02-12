import itertools
from fractions import Fraction 
from math import factorial
import time

iterations = 0
def ShapleyShubikFast(voters):

    # start_time = time.time()

    numPlayers = len(voters)
    totalPivotal = factorial(numPlayers)
    quota = 0
    players = []
    votingPower = []
    # print("players: ", voters)
    for voter in voters:
        # print(voter, "  voters: ",voters)
        quota += voter
    if quota == 1:
        quota /= 2
    elif quota % 2 == 1:
        quota = (quota / 2) + 1/2
    else: 
        quota = (quota / 2) 
    # print("Quota: ", quota)

    totalPower = 0
    for i in range(0, numPlayers):
        totalPower += voters[i]
        players.append([i + 1, voters[i]])
        votingPower.append([i + 1, voters[i], 0])

    permutations = list(itertools.permutations(players))
    j = 0
    while j < len(permutations):
        # print('New iteration: ', j)
        # print(permutations)
        runningSum = 0
        for i in range(numPlayers):
            # print("i: ",i)
            runningSum += permutations[j][i][1]
            # print(runningSum)
            if runningSum > quota:  
                # print(j,i, quota, runningSum, permutations[j])
                numInconsequential = numPlayers - 1 - i        
                numInconsequentialFactorial = factorial(numInconsequential)               
                votingPower[permutations[j][i][0] - 1][2] += numInconsequentialFactorial

                # print(j,i, permutations[j], numInconsequential)               
                j = j + numInconsequentialFactorial
                break
        
                
    powerFractions = []
    for power in votingPower:
        powerFractions.append( str(Fraction(power[2], totalPivotal)))
        power[2] = power[2] / totalPivotal

    for element in votingPower:
        element.pop(0)

    # print("Final Power: ", votingPower)
    # runtime = (time.time() - start_time)
    # print("--- {:f} secconds ---".format(runtime))

    for i in range(numPlayers):
        votingPower[i] =  votingPower[i][1]

    return ([votingPower, powerFractions])
def fixedPoint(power, iterations):
    # start_time = time.time()
    old_list = list(power)
    # print("Old:",  old_list)
    
    new_list = ShapleyShubikFast(power)
    # print("New:",  new_list[0], new_list[1])
    # print("\n")

    if new_list[0] == old_list:
        print("FIXED POINT: ", new_list[1])
        print("Iterations: ", iterations)
        # runtime = (time.time() - start_time)
        # print("+++ {:f} secconds +++".format(runtime))
    else: 
        fixedPoint(new_list[0], iterations + 1)
    
num = 9
for i in range(1, 30):
    test = []
    for j in range(num):
        test.append(i + j)
    print("Start: ",test)
    fixedPoint(test,0)
    print("\n")



def ShapleyShubik(voters):

    start_time = time.time()

    numPlayers = len(voters)
    totalPivotal = factorial(numPlayers)
    quota = 0
    players = []
    votingPower = []
    # print("players: ", voters)
    for voter in voters:
        # print(voter, "  voters: ",voters)
        quota += voter
    if quota == 1:
        quota /= 2
    elif quota % 2 == 1:
        quota = (quota / 2) + 1/2
    else: 
        quota = (quota / 2) 
    # print("Quota: ", quota)

    totalPower = 0
    for i in range(0, numPlayers):
        totalPower += voters[i]
        players.append([i + 1, voters[i]])
        votingPower.append([i + 1, voters[i], 0])

    # print("Total power: ", totalPower)
    # print("player:", players)
    # print("power", votingPower)

    permutations = list(itertools.permutations(players))

    for permutation in permutations:
        # print(permutation)
        runningSum = 0
        # print(permutation)
        for i in range(0,numPlayers):
            # print("i: ",i)
            runningSum += permutation[i][1]
            # print(runningSum)
            if runningSum > quota:
                # print("perm:", permutation[i][0])
                votingPower[permutation[i][0] - 1][2] += 1
                break
    powerFractions = []
    for power in votingPower:
        powerFractions.append( str(Fraction(power[2], totalPivotal)))
        power[2] = power[2] / totalPivotal

    for element in votingPower:
        element.pop(0)

    print("Final Power: ", votingPower)


    runtime = (time.time() - start_time)
    print("--- {:f} secconds ---".format(runtime))

    for i in range(numPlayers):
        votingPower[i] =  votingPower[i][1]

    return ([votingPower, powerFractions])