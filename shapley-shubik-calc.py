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
    print("players: ", voters)
    for voter in voters:
        # print(voter, "  voters: ",voters)
        quota += int(voter)
    if quota % 2 == 1:
        quota = (quota / 2) + 1/2
    else: 
        quota = (quota / 2) 
    print("Quota: ", quota)

    totalPower = 0
    for i in range(0, numPlayers):
        totalPower += voters[i]
        players.append([i + 1, voters[i]])
        votingPower.append([i + 1, voters[i], 0])

    print("Total power: ", totalPower)
    print("player:", players)
    # print("power", votingPower)

    permutations = list(itertools.permutations(players))

    for permutation in permutations:
        # print(permutation)
        runningSum = 0
        # print(permutation)
        for i in range(0,numPlayers):
            # print("i: ",i)
            runningSum += int(permutation[i][1])
            # print(runningSum)
            if runningSum > quota:
                # print("perm:", permutation[i][0])
                votingPower[permutation[i][0] - 1][2] += 1
                break
    for power in votingPower:
        # power[2] = str(Fraction(power[2], totalPivotal))
        power[2] = power[2] / totalPivotal

    for element in votingPower:
        element.pop(0)

    print("Final Power: ", votingPower)


    runtime = (time.time() - start_time)
    print("--- {:f} secconds ---".format(runtime))

    for i in range(numPlayers):
        votingPower[i] =  votingPower[i][1]

    return (votingPower)

def fixedPoint(power):
    old_list = list(power)
    new_list = ShapleyShubik(power)
    # for voter in new_list:
    #     voter = int(voter)
    print("Old:",  old_list)
    print("New:",  new_list)

    print("\n")
    if new_list == old_list:
        print("FIXED POINT: ", new_list)
    else: 
        fixedPoint(new_list)
    
test = [1,1,1,1,1,1]
fixedPoint(test)