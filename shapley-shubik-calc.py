import itertools
def ShapleyShubik(voters):

    totalPivotal = 0;
    numPlayers = len(voters)
    quota = 0

    for voter in voters:
        quota += voter
    if quota % 2 == 0:
        quota = (quota / 2) + 1/2
    else: 
        quota = (quota / 2) 

    for i in range(0, numPlayers):
        voters[i] = [i + 1, voters[i]]

    votingPower = voters
    for i in range(numPlayers):
        votingPower[i][1] = [0]

    permutations = list(itertools.permutations(voters))

    # for permutation in permutations:
    #     runningSum = 0
    #     for i in range(numPlayers):
    #         runningSum += permutation[i][1]
    #         # if runningSum > quota:
                
test = [1,2,3,4,5]
ShapleyShubik(test)