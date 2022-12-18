import random
import csv
import numpy as np
from weapon import skin
from keyvalues import KeyValues
import vdf
from case import *
import randomCSGO
class spectrum(case):
    #To be honest this should be named like "Knife Case" and use that to create the Spectrum 2 Case, but It's too late
    #to do it like that.
    def __init__(self, collection = None):
        if collection == None:
            self.collection = 'The Spectrum 2 Collection'
        else:
            self.collection = collection
        case.__init__(self, self.collection)

        #market hash before udi example: ★ Bayonet | Tiger Tooth (Factory New)
        #has to be hard coded bc of how knives work
        self.knives = ['Bowie Knife', 'Shadow Daggers', 'Huntsman Knife', 'Falchion Knife', 'Butterfly Knife']

        #Chroma Finishes
        self.finishes = ['Tiger Tooth', 'Doppler', 'Ultraviolet', 'Damascus Steel', 'Rust Coat', 'Marble Fade']


        #Chroma finishes
        self.itemDict = {
            'Tiger Tooth': ['an_tiger_orange'], 
            'Doppler': ['am_ruby_marbleized', 'am_sapphire_marbleized', 'am_blackpearl_marbleized','am_doppler_phase1',
                        'am_doppler_phase2', 'am_doppler_phase3', 'am_doppler_phase4'],
            'Ultraviolet': ['so_purple'],
            'Damascus Steel': ['aq_damascus_90'],
            'Rust Coat': ['aq_steel_knife'],
            'Marble Fade': ['am_marble_fade']
        }
        #, 'cu_purple_huntsman', 'so_purple_falchion'

    def knife_unbox(self):
        knife = random.choice(self.knives)
        finish = random.choice(self.finishes)

        infoName = ''
        infoArray = self.itemDict[finish]

        skins = []
        # gets info about skin finishes
        with open('skins.csv', mode='r') as file:
            # reading the CSV file
            csvFile = csv.reader(file)
            # displaying the contents of the CSV file
            for lines in csvFile:
                for inf_name in infoArray:
                    if lines[1] == inf_name:
                        # info_name in column 1 (count from 0).
                        # info provided: skin_name info_name	paintkit_id	collection	rarity	min_wear	max_wear
                        skins.append(lines)

        if len(infoArray) != 1:
            names = []
            odds = []
            for inf_name in infoArray:
                for kf in skins:
                    if kf[1] == inf_name:
                        names.append(inf_name)
                        odds.append(rarity_to_odds(kf[4]))

            # info_name
            infoName = random.choices(names, odds, k=1)
            infoName = infoName[0]
        else:
            infoName = infoArray[0]


        #def __init__(self, name, rarity, min_wear, max_wear, seed = None):

        #GAVIN YOU CAN EDIT HOW THIS NAME IS GENERATED, TO MAKE IT EASIER FOR HASH NAME
        #'★ Gut Knife | Doppler'
            
        name = '★ '
        name += str(knife) + ' | ' + str(finish)
        #print(knife)
        #print(finish)

        #print(infoName)
        for line in skins:
            if line[1] == infoName:
                kInfo = line
        #def __init__(self, name, rarity, min_wear, max_wear, seed = None):
        newSkin = skin(name, kInfo[4], kInfo[5], kInfo[6])
        self.simInventory.append(newSkin)

def rarity_to_odds(rarity):
    #self.odds = [625, 125, 25, 5, 2]

    if rarity == 'rare':
        return 625
    if rarity == 'mythical':
        return 125
    if rarity == 'legendary':
        return 25
    if rarity == 'ancient':
        return 5

def float_to_wear(flt):
    if (flt >= 0) and (flt < 0.07):
        return 'Factory New'
    elif flt < 0.15:
        return 'Minimal Wear'
    elif flt < 0.38:
        return 'Field-Tested'
    elif flt < 0.45:
        return 'Well-Worn'
    elif flt <= 1:
        return 'Battle-Scarred'
    else:
        return 'error'

#spect.sim_case_opens(100)


# Bowie Knives on float DB count:
# 10,064 Damascus Steel exist
# 934 Doppler Ruby
# 2,036 Phase 4
# 2,038 Phase 1
# 2,178 Phase 3
# 2,091 Phase 2
# 973 Doppler Sapphire
# 186 Black Pearl
# 10,144 Rust Coat
# Dopplers seem to share the same 'drop chance', as it rolls for a finish, which if doppler goes for a specific one.
#I.E, all finishes are rolled with an equal chance first. Importantly, the finishes have different rarity tiers in the
#file yet they have similar quantities on float db (which is by far and away the largest database of steam items).
# unfortunately we do not have officially stated odds for knives so guesses based on the datasheet are all that can be done.
#knives do seem to fit the distribution it is supposed to though.
