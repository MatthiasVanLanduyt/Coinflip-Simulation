import random

class Coin:
    def __init__(self):
        pass

    def flip (self):
        sides = ['Heads', 'Tails']
        self.side = random.choice(sides)
        return self.side

    def __str__(self):
        return self.side

class Simulation:
    def __init__(self):
        self.sequence = []
        self.results = {'Heads': 0, 'Tails': 0}
        self.percentages = {'Heads': 0, 'Tails': 0}
        self.runs = 0

    def run (self, n):
        self.runs = n
        for index in range (n):
            coin = Coin()
            flip = coin.flip()
            self.sequence.append(flip)
            self.results[flip] += 1

        self.percentages['Heads'] = self.results['Heads'] / n * 100
        self.percentages['Tails'] = self.results['Tails'] / n *100

    def __str__(self):
        return (f'Simulation with {self.runs} coinflips.\nCounts: {self.results}.\n')


def play():
    while True:
        try:
            n = int(input('How many simulations do you want to run?'))
            simulation = Simulation()
            simulation.run(n)
            print(simulation)
            break
        except:
            print('Ooops....we have some errors.')
    
play ()

