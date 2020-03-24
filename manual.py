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
        quota = (quota / 2) + 1 / 2
    else:
        quota = quota / 2
    # print("Quota: ", quota)

    permutations = list(itertools.permutations(players))

    for i in range(len(permutations)):
        j = 0
        for q in range(len(permutations[i])):
            j += permutations[i][j]
            if j > quota:
                return [votingPower, powerFractions]
