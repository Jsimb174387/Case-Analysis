import random
import numpy as np
from weapon import skin
from keyvalues import KeyValues
class case:
    def __init__(self):
        #case skin rarity tiers for basic cs:go cases. They have proper names, but these address them by color
        self.rarities = ['blue','purple','pink','red','yellow']

        #skin names in each rarity tier
        self.blue = ["AWP | Corticera", "AK-47 | Fire Serpent"]
        self.purple = []
        self.pink = []
        self.red = []
        self.yellow = []
        

        #2 yellow per 5 red, 1 red per 5 pinks, 1 pink per 5 purples, 1 purple per 5 blues.
        self.odds = [625/782, 125/782, 25/782, 5/782, 2/782]

    def sim_rarity(self, amount):
        return random.choices(self.rarities, self.odds, k = amount)

    def sim_case_opens(self,amount):
        rarities = self.sim_rarity(amount)
        #simulated inventory holds the "skins" unboxed.
        simInventory = []


        for rarity in rarities:
            if rarity == 'blue':
                name = random.choices(self.blue)
                #smin_wear and max_wear values temporary
                min_wear = 0
                max_wear = 1
                newSkin = skin(name, rarity, min_wear, max_wear)
                simInventory.append(newSkin)
            elif rarity == 'purple':
                pass
            elif rarity == 'pink':
                pass
            elif rarity == 'red':
                pass
            elif rarity == 'yellow':
                pass

            
        return simInventory


    
phantom = case()
print(phantom.sim_case_opens(1))


