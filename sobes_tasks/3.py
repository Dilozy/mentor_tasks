dict_ = {
    "a": {
        "b": {
            "c":1
        }
    },
    "d": 2
}


def get_value_by_key(data, keys):
    for key in keys.split("."):
        value = data.get(key)
        if isinstance(value, dict):
            data = value
        else:
            return value


print(get_value_by_key(dict_, "a.b.c")) # 1
print(get_value_by_key(dict_, "a.d.e")) # None
