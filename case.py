import random
import numpy as np
class case:
    def __init__(self):
        #case skin rarity tiers for basic cs:go cases. They have proper names, but these address them by color
        self.rarities = ['blue','purple','pink','red','yellow']

        #2 yellow per 5 red, 1 red per 5 pinks, 1 pink per 5 purples, 1 purple per 5 blues.
        self.odds = [625/782, 125/782, 25/782, 5/782, 2/782]

        #Normal range that the wear value of the skin can be. This is very skin dependent.
        self.wear_range = [0,1]


    def simRarity(self, amount):
        return random.choices(self.rarities, self.odds, k = amount)

    
fal = case()
print(fal.simRarity(25))
print(fal.simFloat())
