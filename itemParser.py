import vdf

#loads csgo items_game file, truncated to remove "items_game" at the beginning. Current version pulled 11/19/2022.
d = vdf.load(open('items_game.txt'))

# print('keys\n')
#
# keys = d['paint_kits'].keys()
#
# print(keys)
#
# print(d['paint_kits']['500'])

trans = vdf.load(open('csgo_english.txt'))

#lang_keys = trans['lang']['Tokens'].keys()

#print(lang_keys)