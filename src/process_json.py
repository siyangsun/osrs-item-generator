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
