import itertools
from fractions import Fraction 
from math import factorial
import time

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
def ShapleyShubikFast(voters):

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

    permutations = list(itertools.permutations(players))

    for j in range(len(permutations)):
        print('New iteration: ', j)
        # print(permutations)
        runningSum = 0

        for i in range(0, numPlayers):
            # print("i: ",i)
            runningSum += permutations[j][i][1]
            # print(runningSum)
            if runningSum > quota:
                votingPower[permutations[j][i][0] - 1][2] += 1

                check = permutations[j][:i]

                while j < len(permutations) -1:
                    if permutations[j+1][:i] == check:
                        votingPower[permutations[j][i][0] - 1][2] += 1
                        j+=1
                    else: 
                        break
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
def fixedPoint(power):
    old_list = list(power)
    # print("Old:",  old_list)
    
    new_list = ShapleyShubik(power)
    # print("New:",  new_list[0], new_list[1])
    # print("\n")

    if new_list[0] == old_list:
        print("FIXED POINT: ", new_list[1])
    else: 
        fixedPoint(new_list[0])

# for i in range(10):
#     print(i)
#     test = [i, i+1, i+2,i+3,i+4,i+5,i+6, i+7, i+8]
#     ShapleyShubik(test)
#     print("\n")
# # 
# test = [3,4,5]
# fixedPoint(test)

# def permutationTest(baseList):
#     permutations = list(itertools.permutations(baseList))
#     for j in range(len(permutations)):
#         check = permutations[j][:4]
#         if permutations[j+1][:4] == check:
#             print(permutations[j]) 
#             print(permutations[j+1])
#             j+=1
#             print("\n")
# permutationTest([1,2,3,4,5,6,7])


for i in range(1):
    print(i)
    test = [i, i+1, i+2,i+3,i+4,i+5]
    ShapleyShubik(test)
    ShapleyShubikFast(test)
    print("\n")

# permutationTest([1,2,3,4])
