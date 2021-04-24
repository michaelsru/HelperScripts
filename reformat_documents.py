import json

input_file = input('input file:')
output_file = 'formatted_{}'.format(input_file)

# read json file
f = open(input_file, 'r', encoding="utf8")
lines = f.read()
# print(lines)
json_lines = json.loads(lines)
new_json = []

for user in json_lines:
    if 'bank' in user:
        continue
# parse line
# reformat line
    stocks = {'doge':{}, 'amog':{}, 'pewd':{}, 'mark':{}, 'jack':{}, 'fart':{}, 'robb':{}}
    stocks['doge']['quantity'] = user['dogestock']
    stocks['amog']['quantity'] = user['amogusdrip']
    stocks['pewd']['quantity'] = user['pewdiepies']
    stocks['mark']['quantity'] = user['markspliers']
    stocks['jack']['quantity'] = user['jacksepticeyes']
    stocks['fart']['quantity'] = user['fartnite']
    stocks['robb']['quantity'] = user['robblocks']
    user.pop('dogestock')
    user.pop('amogusdrip')
    user.pop('pewdiepies')
    user.pop('markspliers')
    user.pop('jacksepticeyes')
    user.pop('fartnite')
    user.pop('robblocks')
    # add other stocks
    user['stock'] = stocks

new_lines = json.dumps(json_lines)
f.close()

# write to output file

fw = open(output_file, 'w')
fw.write(new_lines)
fw.close()