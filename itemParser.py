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
    def get_skin_info(self):
        pass

    def get_wear_range_rarity(self, id):
        id = str(id)
        items_game = vdf.load(open("node-csgo-items-parser-master/data/items_game.txt"), mapper=vdf.VDFDict)

        skin = items_game['items_game']["paint_kits"][id]
        default = items_game['items_game']["paint_kits"]['0']
        name = skin['name']
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
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #Creates header row
            filewriter.writerow(['skin_name', 'info_name', 'paintkit_id', 'collection', 'rarity', 'min_wear', 'max_wear'])

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



    def skins_csv_sort(self):
        pass





#replaced with skin_parser. May have future use though, which is why it is temp left here.
# #loads csgo items_game file, truncated to remove "items_game" at the beginning. Current version pulled 11/19/2022.
#d = vdf.load(open('items_game.txt'))

#csgo item parser parses items_game.txt to find skin info.

#dict = d['items_game']
f = skin_parser()
d = vdf.load(open('node-csgo-items-parser-master/data/items_game.txt'))
#Take note of ['client_loot_lists']
print(d['items_game']['revolving_loot_lists']['3'])
#print(f.get_wear_range_rarity('10080'))


#f.gen_skins_csv()
