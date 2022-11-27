import vdf
import json


class skin_parser:
    def __init__(self, ):
        self.file = open("node-csgo-items-parser-master/skins.json")

        # dict_keys(
        #     ['paintkit_names', 'paintkit_ids', 'stickerkit_names', 'stickerkit_ids', 'stickerkits', 'weapon_skins',
        #      'medals', 'medal_names', 'agents', 'agent_names', 'agent_models', 'agent_rarities'])

        self.item_dict = json.loads(self.file.read())
        self.keys = self.item_dict.keys()
        #print(self.keys)
        print(self.item_dict['paintkit_names']['cu_m4a4_neo_noir'])
        print(self.item_dict['paintkit_ids']['cu_m4a4_neo_noir'])
    def get_skin_info():
        pass



#replaced with skin_parser. May have future use though, which is why it is temp left here.
# #loads csgo items_game file, truncated to remove "items_game" at the beginning. Current version pulled 11/19/2022.
#d = vdf.load(open('items_game.txt'))

#csgo item parser parses items_game.txt to find skin info.

#dict = d['items_game']

f = skin_parser()