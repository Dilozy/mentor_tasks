data = {'a': 1, 'b': { 'c': 2, 'd': { 'e': 3 } }, 'f': 4}
res = []

def get_dict_items(data):
    for item in data.items():
        if isinstance(item[1], dict):
            get_dict_items(item[1])
        else:
            res.append(item)
get_dict_items(data)
print(res)