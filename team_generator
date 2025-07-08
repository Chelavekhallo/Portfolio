# project- mixing and creating teams
import random

amount = int(input())
teams = int(input())

tems = [x for x in range(1, teams + 1)]
res_teams = []
b = amount // teams
while amount != 0:
    name = input("what is your name?")
    a = random.choice(tems)
    print(a)
    res_teams.append(name) 
    res_teams.append(a)
    if res_teams.count(a) > b:
        tems.remove(a)
    amount = amount - 1
