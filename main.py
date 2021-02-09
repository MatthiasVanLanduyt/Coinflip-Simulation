import random


def coinflip():
    sides = ['Heads', 'Tails']
    
    random.random()
    flip = random.choice(sides)
    
    # print('Flip: ' + flip)

    return flip

def simulate_coinflips (n):
    results_sequence = []
    results = {'Heads': 0, 'Tails': 0}
    for index in range (n):
        flip = coinflip()
        results_sequence.append(flip)
        results[flip] += 1
        
  
    heads_percentage = results['Heads'] / n * 100

    print(f'Summarized data: {results}')
    print(f'Heads percentage: {heads_percentage}%')

def play():
    while True:
        try:
            n = int(input('How many simulations do you want to run?'))
            print(n)
            simulate_coinflips(n)
            print('All done')
            break
        except:
            print('Ooops....we have some errors.')
    
play ()

