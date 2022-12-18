import random
import csv
import numpy as np
from weapon import skin
from keyvalues import KeyValues
import vdf
from case import *
import randomCSGO
from spectrum2 import *

class chroma(spectrum):
    def __init__(self, collection = None):
        #collection can be Chroma, Chroma 2, Chroma 3. default to Chroma
        #Chroma 2 is : The Chroma 2 Collection
        #Chroma 3 is : The Chroma 3 Collection
        if collection == None:
            self.collection = 'The Chroma Collection'
        else:
            self.collection = collection
        spectrum.__init__(self, self.collection)
        #uses the same finishes as the spectrum cases (or more technically, spectrum
        #uses chroma finishes). 
        self.knives = ['Bayonet', 'Flip Knife', 'Gut Knife', 'Karambit', 'M9 Bayonet']

class prisma(spectrum):
    def __init__(self, collection=None):
        # collection can be Prisma and Prisma 2. default to Prisma.
        if collection == None:
            self.collection = 'The Prisma Collection'
        else:
            self.collection = collection
        spectrum.__init__(self, self.collection)
        #Prisma cases also use spectrum finishes. 
        self.knives = ['Navaja Knife', 'Stiletto Knife', 'Talon Knife', 'Ursus Knife']

class horizon(spectrum):
    def __init__(self, collection=None):
        # collection can be Horizon and Danger Zone. default to Horizon.
        if collection == None:
            self.collection = 'The Horizon Collection'
        else:
            self.collection = collection
        spectrum.__init__(self, self.collection)
        #uses Arms deal Finishes. 
        self.finishes = ['Fade', 'Case Hardened', 'Slaughter', 'Crimson Web', 'Safari Mesh', 'Stained', 'Blue Steel',
                         'Scorched', 'Urban Masked', 'Night Stripe', 'Forest DDPAT', '★ (Vanilla)', 'Boreal Forest']
        #Prisma (?) Knives. I forgot where it originated.
        self.knives = ['Navaja Knife', 'Stiletto Knife', 'Talon Knife', 'Ursus Knife']

        #needs double checking later. CRIMSON WEB IS STUPID THERE IS 2 PATTERN TYPES AND NOT A CLEAR WAY TO DIFFERENTIATE
        #WHY DOES VALVE DO THIS BULLSHIT SO MUCH. it could be hy_webs or  hy_webs_darker, I need to check the database
        #Vanilla Knife is also a wierd one. Likely using 'default', also wear does nothing on it even though it has a value
        self.itemDict = {
            'Fade': ['aa_fade'],
            'Case Hardened': ['aq_oiled'],
            'Slaughter': ['am_zebra'],
            'Crimson Web': ['hy_webs'],
            'Safari Mesh': ['sp_mesh_tan'],
            'Stained': ['aq_forced'],
            'Blue Steel': ['aq_blued'],
            'Scorched': ['sp_dapple'],
            'Urban Masked': ['sp_tape_urban'],
            'Night Stripe': ['sp_nightstripe'],
            'Forest DDPAT': ['hy_ddpat'],
            '★ (Vanilla)': ['default'],
            'Boreal Forest': ['hy_forest_boreal']
    
        }