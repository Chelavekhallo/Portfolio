def beeramid(bonus, price):
    run = True
    cn = 1
    cans = bonus//price
    complete_levels = 0
    while run:
        if cans<(cn**2):
            run = False
        else:
            cans = cans - (cn**2)
            cn+=1
            complete_levels+=1
    return complete_levels
# Original problem: https://www.codewars.com/kata/51e04f6b544cf3f6550000c1