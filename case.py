import random
import csv
import numpy as np
from weapon import skin
from keyvalues import KeyValues
import vdf
class case:
    def __init__(self, collection, rarities = None):
        #case skin rarity tiers for basic cs:go cases. They have proper names, but these address them by color,
        #which is a common short hand in the community

        self.collectionName = collection
        self.collectionSkins = obtain_collection(collection)
        self.simInventory = []
        if rarities == None:
            #use default rarities: this is typical for normal cases, with the notable exception being souvenir cases
            self.rarities = ['blue','purple','pink','red','yellow']
        else:
            self.rarities = rarities

        #skin Array in each rarity tier
        self.rarDict = self.sort_rarity()
        self.blue = []
        self.purple = []
        self.pink = []
        self.red = []
        self.yellow = []
        

        #2 yellow per 5 red, 1 red per 5 pinks, 1 pink per 5 purples, 1 purple per 5 blues.
        self.odds = [625/782, 125/782, 25/782, 5/782, 2/782]

    def sim_rarity(self, amount):
        return random.choices(self.rarities, self.odds, k = amount)

    def sort_rarity(self):
        collection = self.collectionSkins
        # Skin as defined by a line in the csv file:
        # info provided: skin_name info_name	paintkit_id	collection	rarity	min_wear	max_wear, sets (all collumns after)
        # assuming only 1 because cases, which is all we are interested in, have only 1 collection

        case = collection[0][7]

        items_game = vdf.load(open("node-csgo-items-parser-master/data/items_game.txt"), mapper=vdf.VDFDict)

        #naming scheme in client loot list is like this: "crate_community_12_rare"
        crates = items_game["items_game"]["client_loot_lists"]

        words = ret_words(case)
        sentence = []
        for word in words:
            if word == 'set':
                sentence.append('crate')
            else:
                sentence.append(word)
        #each rarity needs it's own key
        r_dictionary = {}
        for short in self.rarities:
            rarity = short_to_rarity(short)
            sentence.append(rarity)
            key = create_sent(sentence)

            if short != 'yellow':
                vArray = []
                for name in crates[key]:
                    value = ''
                    read = False
                    for element in name:
                        if element == ']':
                            read = False
                        if read:
                            value = value + element
                        if element == '[':
                            read = True
                    vArray.append(value)
                r_dictionary.update({short : vArray})
            sentence.pop()
        return r_dictionary

    def sim_case_opens(self,amount):
        rarities = self.sim_rarity(amount)
        #simulated inventory holds the "skins" unboxed.

        for rarity in rarities:
            if rarity != 'yellow':
                outcomes = self.rarDict[rarity]
                info_name = random.choices(outcomes)
            else:
                pass
                

            # info provided: skin_name info_name	paintkit_id	collection	rarity	min_wear	max_wear, sets
            for sInfo in self.collectionSkins:
                if sInfo[1] == info_name[0]:
                    newSkin = skin(sInfo[0], sInfo[4], sInfo[5], sInfo[6])
                    self.simInventory.append(newSkin)


def rarity_to_short(rarity):
    #cases do not include greys and light blues
    if rarity == 'common':
        return 'grey'
    if rarity == 'uncommon':
        return 'light_blue'
    if rarity == 'rare':
        return 'blue'
    if rarity == 'mythical':
        return 'purple'
    if rarity == 'legendary':
        return 'pink'
    if rarity == 'ancient':
        return 'red'
    if rarity == 'knife':
        return 'yellow'
    return 'rarity not found'

def short_to_rarity(rarity):
    #the opposite as I have realized I need this too.
    if rarity == 'grey':
        return 'common'
    if rarity == 'light_blue':
        return 'uncommon'
    if rarity == 'blue':
        return 'rare'
    if rarity == 'purple':
        return 'mythical'
    if rarity == 'pink':
        return 'legendary'
    if rarity == 'red':
        return 'ancient'
    if rarity == 'yellow':
        return 'knife'
    return 'rarity not found'


def obtain_collection(collection):
    # opening the CSV file
    skins = []
    with open('skins.csv', mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        for lines in csvFile:
            if lines[3] == collection:
                #collection name in collumn 3 (count from 0).
                #info provided: skin_name info_name	paintkit_id	collection	rarity	min_wear	max_wear, sets (all collumns after)
                update = lines
                update[4] = rarity_to_short(lines[4])
                skins.append(update)
    return skins

def ret_words(string):
    #removes underscores, and seperates words into their own indexes in a array
    words = []
    current_word = ''
    for element in string:
        if element != '_':
            current_word = current_word + element
        else:
            words.append(current_word)
            current_word = ''
    if current_word != '':
        words.append(current_word)
    return words

def create_sent(array):
    sentence = ''
    for word in array:
        if sentence != '':
            sentence += '_'
        sentence += word
    return sentence

if not (ret_words('Jeff_beany_is_big') == ['Jeff', 'beany', 'is', 'big']):
    raise 'ret_word Error!'
if not (create_sent(['Jeff', 'beany', 'is', 'big']) == 'Jeff_beany_is_big'):
    raise 'create_sent Error!'

# for skin in col:
#     print(skin)

phan = case('The Gamma 2 Collection')
phan.sort_rarity()
phan.sim_case_opens(100)

for skin in phan.simInventory:
    print(skin)




















