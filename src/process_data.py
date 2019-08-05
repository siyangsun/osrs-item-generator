import json


def get_itemlist():
    names = []
    with open('../data/raw/items-summary.json') as json_file:
        data = json.load(json_file)
        for i in data.keys():
            item = data[str(i)]
            names.append(item['name'])
    json_file.close()
    return(names)

def split_names(names):
    processed_names = []
    for name in names:
        processed_names.append(name.split(' '))
    return(processed_names)

items = get_itemlist()
print(split_names(items))
