import random


def coinflip():
    sides = ['Heads', 'Tails']
    
    random.random()
    flip = random.choice(sides)
    
    print('Flip: ' + flip)

    return flip

def simulate_coinflips (n):
    results_sequence = []
    results = {'Heads': 0, 'Tails': 0}
    results_percentage = 
    for index in range (n):
        flip = coinflip()
        results_sequence.append(flip)
        results[flip] += 1
        print (results)

def play():
    while True:
        try:
            n = int(input('How many simulations do you want to run?'))
            simulate_coinflips(n)
            break
        except:
            print('Ooops....we have some errors.')
    
play ()

