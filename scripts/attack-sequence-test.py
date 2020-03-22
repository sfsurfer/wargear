#!/usr/bin/python3

import argparse, random, statistics

runs = 10000

parser = argparse.ArgumentParser()
parser.add_argument("attack_troops", type=int)
parser.add_argument("defense_troops", type=int, nargs='+')

args = parser.parse_args()

print("Attacking troops: %i" % args.attack_troops)
print("Defenses: %s" % args.defense_troops)
print("Simulations: %i" % runs)

def attack(a, d):
    if a < 1 or a > 3:
        raise Exception("Invalid attack troops %i" % a)
    if d < 1 or d > 2:
        raise Exception("Invalid defense troops %i" % d)

    al = 0
    dl = 0

    ar = [random.randrange(1,7) for iter in range(a)]
    dr = [random.randrange(1,7) for iter in range(d)]
    ar.sort()
    dr.sort()
    #print("attack rolls: %s : defense rolls %s" % (ar, dr))
    while ar and dr:
        nexta = ar.pop()
        nextd = dr.pop()
        if nexta > nextd:
            dl += 1
        else:
            al += 1
    return([al, dl])


def attack_territory(at, dt):
    while dt > 0 and at > 1:
        r = attack(min([3, at - 1]), min([2, dt]))
        at -= r[0]
        dt -= r[1]
    return [at, dt]

# Use only 2 to attack when only 1 defense
def attack_territory_2v1(at, dt):
    while dt > 1 and at > 1:
        r = attack(min([3, at - 1]), min([2, dt]))
        at -= r[0]
        dt -= r[1]
    while dt > 0 and at > 1:
        r = attack(min([2, at - 1]), min([2, dt]))
        at -= r[0]
        dt -= r[1]
    return [at, dt]
    

def run():    
    at = args.attack_troops
    for d in args.defense_troops:
        r = attack_territory(at, d)
        #r = attack_territory_2v1(at, d)
        at = r[0]
        if r[1] == 0:  # Attacker won
            at -= 1  # leave one in won territory
            #print("Territory won, continuing to next, with %i troops" % at)
        elif at == 1:  # Defense won
            #print("Attacker out of troops")
            break
    return at

def multirun(n):
    v = []
    at = args.attack_troops
    for i in range(n):
        #r = attack_territory(args.attack_troops, args.defense_troops[0])
        r = run()
        #print(r[0])
        #v.append(r[0])
        v.append(r)

    #print(len(v))
    #print(v[0])
    print("Percent sequence won: %0.2f" % ((1 - v.count(1)/runs) * 100))
    print("Mean troops remaining: %0.2f" % statistics.mean(v))
    print("Standard Deviation: %0.2f" % statistics.stdev(v))
    
multirun(runs)
#r1 = attack(3,2)
#print(r1)
#r2 = attack(1,1)
#print(r2)
