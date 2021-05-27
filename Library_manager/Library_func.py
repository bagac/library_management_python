from Library_class import *
import json


def write_json(data, filename):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def Extend_json(data_new, fileJson):
    with open(fileJson, encoding='utf-8') as f:
        temp_data = json.load(f)
        temp_data.append(data_new)
        write_json(temp_data, fileJson)
        print("Save Done")


def dict_filter(dictlist: list, key: str, value: str) -> list:
    print(f'Bắt đầu tìm kiếm {key}:{value}: ')
    return list(filter(lambda x: x.get(key) == value, dictlist))




