import json
import csv
from api_request import requester
from keyvalues import KeyValues
import vdf


class skin_parser:
    def __init__(self, ):
        self.file = open("node-csgo-items-parser-master/skins.json")

        # dict_keys(
        #     ['paintkit_names', 'paintkit_ids', 'stickerkit_names', 'stickerkit_ids', 'stickerkits', 'weapon_skins',
        #      'medals', 'medal_names', 'agents', 'agent_names', 'agent_models', 'agent_rarities'])

        self.item_dict = json.loads(self.file.read())
        self.keys = self.item_dict.keys()
        # numb = 6
        # skin = self.item_dict['weapon_skins']['4']['paintkit_names'][numb]
        # print(skin)
        # rarity = self.item_dict['weapon_skins']['4']['paintkit_rarities'][numb]
        # print(self.item_dict['paintkit_names'][skin])
        # print(self.item_dict['paintkit_ids'][skin])
        # print(rarity)

    def get_wear_range_rarity(self, id):
        id = str(id)
        items_game = vdf.load(open("node-csgo-items-parser-master/data/items_game.txt"), mapper=vdf.VDFDict)

        skin = items_game['items_game']["paint_kits"][id]
        name = skin['name']

        for element in skin:
            #print(element + ": ")
            #print(skin[element])
            pass

        sets = items_game['items_game']['item_sets']
        for set in sets:
            for element in sets[set]['items']:
                if name in element:
                    print(element)
                    print(set)

        default = items_game['items_game']["paint_kits"]['0']
        if name != 'default':
            rarity = items_game['items_game']["paint_kits_rarity"][name]
        else:
            rarity = 'default'

        if 'wear_remap_min' in skin.keys():
            min_wear = skin['wear_remap_min']
        else:
            min_wear = default['wear_remap_min']

        if 'wear_remap_max' in skin.keys():
            max_wear = skin['wear_remap_max']
        else:
            max_wear = default['wear_remap_max']

        #return rarity, min_wear, max_wear
        return items_game['items_game'].keys

    def gen_skins_csv(self):
        f = skin_parser()
        #creates api Req object
        api_req = requester()
        #info names, which appear like this: cu_m4a4_neo_noir
        info_names = self.item_dict['paintkit_ids'].keys()

        #creates csv file to write to
        with open('skins.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',')
            #Creates header row
            filewriter.writerow(['skin_name', 'info_name', 'paintkit_id', 'collection', 'rarity', 'min_wear', 'max_wear', 'sets'])

            for inf_name in info_names:
                #print(inf_name)
                id = self.item_dict['paintkit_ids'][inf_name]

                #get_collection returns item_name, collection
                collection_info = api_req.get_collection(id)

                while collection_info == 'retry':
                    collection_info = api_req.get_collection(id)

                print(collection_info[0],collection_info[1])
                info = f.get_wear_range_rarity(id)
                filewriter.writerow([collection_info[0], inf_name, id, collection_info[1], info[0], info[1], info[2]])
        update_skin_set()

def update_skin_set():

    csvLines = []
    with open('skins.csv', mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # retreiving the contents of the CSV file
        for lines in csvFile:
            csvLines.append(lines)

    #opens Items_game to look for item_set (which is not the same as collection name, frustratingly enough)
    items_game = vdf.load(open("node-csgo-items-parser-master/data/items_game.txt"), mapper=vdf.VDFDict)

    #skips header
    app_lines = csvLines[1:]
    update_lines = []
    for line in app_lines:
        #line: ['skin_name', 'info_name', 'paintkit_id', 'collection', 'rarity', 'min_wear', 'max_wear', 'set']

        id = line[2]
        skin = items_game['items_game']["paint_kits"][id]
        name = skin['name']
        newLine = line[:7]

        sets = items_game['items_game']['item_sets']
        for set in sets:
            for item in sets[set]['items']:
                read = False
                comparitor = ''

                for element in item:
                    if element == ']':
                        read = False
                    if read:
                        comparitor = comparitor + element
                    if element == '[':
                        read = True
                if name == comparitor:
                    newLine.append(set)

        update_lines.append(newLine)


    #overwrites with updated information
    with open('skins.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        filewriter.writerow(
            ['skin_name', 'info_name', 'paintkit_id', 'collection', 'rarity', 'min_wear', 'max_wear', 'sets'])

        for line in update_lines:
            print(line)
            filewriter.writerow(line)


#replaced with skin_parser. May have future use though, which is why it is temp left here.
# #loads csgo items_game file, truncated to remove "items_game" at the beginning. Current version pulled 11/19/2022.
#d = vdf.load(open('items_game.txt'))

#csgo item parser parses items_game.txt to find skin info.

#dict = d['items_game']
f = skin_parser()
update_skin_set()
#r = f.get_wear_range_rarity(259)
#d = vdf.load(open('node-csgo-items-parser-master/data/items_game.txt'))
#Take note of ['client_loot_lists']
#print(d['items_game']['revolving_loot_lists']['3'])
#print(f.get_wear_range_rarity('10080'))


#f.gen_skins_csv()
