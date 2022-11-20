import numpy as np
class skin:
    def __init__(self, name, rarity, min_wear, max_wear):
        #name is inputted as a array.
        self.name = name[0]
        self.rarity = rarity
        self.min_wear = min_wear
        self.max_wear = max_wear

    def wearName(self, wear):
        #FN: 0 - 0.07, MW: 0.07 - 0.15, FT: 0.15 - 0.38, WW: 0.38 - 0.45, BS: 0.45 - 1
        #Float values are NOT uniform in creation chance! As far as we can tell:
        # https://blog.csgofloat.com/analysis-of-float-value-and-paint-seed-distribution-in-cs-go/
        pass


    def simWear(self):
        #FN: 0 - 0.07, MW: 0.07 - 0.15, FT: 0.15 - 0.38, WW: 0.38 - 0.45, BS: 0.45 - 1
        #Float values are NOT uniform in creation chance! As far as we can tell:
        # https://blog.csgofloat.com/analysis-of-float-value-and-paint-seed-distribution-in-cs-go/

        #This github repository created by them has what they aproximated as the way floats are generated.
        #https://github.com/Step7750/UniformRandom

        # finds full_range_float from 0,1, then truncates

        "What the game does is effectively try to generate a random integer within 0-2147483647"
        "(max signed 32-bit integer) and simply divides the result by 2147483647"
        "Then the max/min float of a skin is used as essentially a scalar to determine the true wear of a skin."
        full_range_float = np.random.uniform(0, 1)

        #obtained from csgofloat.com
        final_float = full_range_float * (self.max_wear - self.min_wear) + self.min_wear
        return final_float

    def __repr__(self):
        return self.name
