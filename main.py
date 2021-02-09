import random


def coinflip():
    sides = ['Heads', 'Tails']
    
    random.random()
    flip = random.choice(sides)
    
    print('Flip: ' + flip)

    return flip

def simulation(n):
    results = {'Heads': 0, 'Tails': 0}
    for index in range (n):
        
        results[coinflip()] += 1
        print (results)

simulation(50)
