import numpy as np
from randomCSGO import *
import random

class skin:
    def __init__(self, name, rarity, min_wear, max_wear, seed = None):
        self.name = name
        self.rarity = rarity
        self.min_wear = float(min_wear)
        self.max_wear = float(max_wear)
        self.stattrack = random.choices([True, False], weights = [1,9])

        if seed == None:
            self.seed = random.randint(-2147483648, 2147483647)
        else:
            self.seed = see

        self.wear =  sim_wear(self.seed, self.min_wear, self.max_wear)
        self.wear_name = self.wear_to_name(self.wear)
        if self.name[-1] == " ":
            self.hash = name + self.wear_to_name(self.wear)[0]
        else:
            self.hash = name + ' ' + self.wear_to_name(self.wear)[0]

    def wear_to_name(self, wear: float):
        #also returns range
        if 0.00 < wear < 0.07:
            return ['(Factory New)', '0.00', '0.07']
        if 0.07 < wear < 0.15:
            return ['(Minimal Wear)', '0.07', '0.15']
        if 0.15 < wear < 0.38:
            return ['(Field-Tested)', '0.15', '0.38']
        if 0.38 < wear < 0.45:
            return ['(Well-Worn)', '0.38', '0.45']
        if 0.45 < wear < 1.00:
            return ['(Battle-Scarred)', '0.45', '1.00']



    def __repr__(self):
        return self.hash

def sim_wear(seed, min, max):
    #FN: 0 - 0.07, MW: 0.07 - 0.15, FT: 0.15 - 0.38, WW: 0.38 - 0.45, BS: 0.45 - 1
    #Float values are NOT uniform in creation chance! As far as we can tell:
    # https://blog.csgofloat.com/analysis-of-float-value-and-paint-seed-distribution-in-cs-go/

    #This github repository created by them has what they aproximated as the way floats are generated.
    #https://github.com/Step7750/UniformRandom

    # finds full_range_float from 0,1, then truncates

    "What the game does is effectively try to generate a random integer within 0-2147483647"
    "(max signed 32-bit integer) and simply divides the result by 2147483647"
    "Then the max/min float of a skin is used as essentially a scalar to determine the true wear of a skin."

    #generates a random int

    floatGen = Stream()
    floatGen.SetSeed(seed)
    # RandomFloat(self, flLow: np.float32, flHigh: np.float32)-> np.float32
    float = floatGen.RandomFloat(min, max)
    #print(float)

    return float

# weapon = skin("AK", "Purple", 0, 1, seed = 1282125376)
# print(weapon.wear)
