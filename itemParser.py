import json
import csv
from api_request import requester



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
    def get_skin_info(self):
        pass

    def gen_skins_csv(self):
        #creates api Req object
        api_req = requester()
        #info names, which appear like this: cu_m4a4_neo_noir
        info_names = self.item_dict['paintkit_ids'].keys()

        #creates csv file to write to
        with open('skins.csv', 'w') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #Creates header row
            filewriter.writerow(['skin_name', 'info_name', 'paintkit_id', 'collection'])

            for inf_name in info_names:
                #print(inf_name)
                id = self.item_dict['paintkit_ids'][inf_name]

                #get_collection returns item_name, collection
                collection_info = api_req.get_collection(id)
                while collection_info == 'retry':
                    collection_info = api_req.get_collection(id)
                print(collection_info[0],collection_info[1])
                filewriter.writerow([collection_info[0], inf_name, id, collection_info[1]])


#replaced with skin_parser. May have future use though, which is why it is temp left here.
# #loads csgo items_game file, truncated to remove "items_game" at the beginning. Current version pulled 11/19/2022.
#d = vdf.load(open('items_game.txt'))

#csgo item parser parses items_game.txt to find skin info.

#dict = d['items_game']

f = skin_parser()
f.gen_skins_csv()
