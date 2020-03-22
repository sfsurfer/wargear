#!/usr/bin/python3

import random

startTroops = 1000

winPct3v1 = 0.584
winPct4v1 = 0.877
losePct3v1 = 0.416
losePct4v1 = 1.0

##
# Which better when attacking against a single
# defensive troop and you only need to take the
# one territory and you need to conserve troops,
# attacking with 3 or 2?
#
# Win and loss percentages calculated from the other
# script in the repo
#
def run(startTroops, winPct, losePct):
    wins = 0
    while startTroops > 0:
        r = random.random()
        if r < losePct:
            startTroops -= 1
        if r < winPct:
            wins += 1
    return wins

res3v1 = run(startTroops, winPct3v1, losePct3v1)
res4v1 = run(startTroops, winPct4v1, losePct4v1)

print("3v1 got %i wins with %i start troops" % (res3v1, startTroops))
print("4v1 got %i wins with %i start troops" % (res4v1, startTroops))


