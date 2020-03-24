import math
import itertools
from collections import Counter


def summer(tuple):
    total = 0
    for i in tuple:
        total += i
    return total


voters = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
iterations = 0

print("\nInput voters:")
print(voters)
print("\nFixed point:")

while True:
    proportions = []
    winners = []
    coalitions = []
    if iterations == 0:
        quota = sum(voters) / 2
    else:
        quota = 0.5

    for L in range(0, len(voters) + 1):
        for subset in itertools.combinations(voters, L):
            coalitions.append(subset)

    for i in coalitions:
        sum = 0
        for j in i:
            sum += j
        if sum > quota:
            winners.append(i)

    for i in winners:
        for j in i:
            if summer(i) - j <= quota:
                proportions.append(j)

    okay = Counter(proportions)
    repeats = Counter(voters)

    oldVoters = voters.copy()
    voters.clear()

    for i in repeats:
        if repeats[i] > 1:
            for j in range(0, repeats[i]):
                voters.append((okay[i] / repeats[i]) / len(proportions))
                # print(((okay[i] / repeats[i])/len(proportions)))
        else:
            voters.append(okay[i] / len(proportions))
            # print(okay[i]/ len(proportions))

    # print(winners)
    # print(proportions)
    # print(voters)
    # print(oldVoters)
    iterations += 1

    if voters == oldVoters:
        print(voters)
        print("\niterations: ", iterations, "\n\n", end="")
        break
