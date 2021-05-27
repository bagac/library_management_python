import json

str = [{'Document_Name': 'tài liệu đầu ', 'Serial': 'tiên ', 'Company': 'nè ', 'Reissue': 'hau'}]
str_two = {'Book_Name': 'sách 1 ', 'Author': 'một 2', 'Paper_number': '20'}
str_three = [{'Magazine_Name': 'thanh niên d', 'Reissue_number': '200', 'Reissue_month': '03'}]
def write_json(data, filename):
    with open(filename,"w",encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def Extend_json(data_new, fileJson):
    with open(fileJson, encoding='utf-8') as f:
        temp_data = json.load(f)
        temp_data.append(data_new)
        write_json(temp_data,fileJson)

def dict_filter(dictlist: list, key: str, value: str) -> list:
    print(f'Bắt đầu tìm kiếm {key}:{value}: ')
    return list(filter(lambda x: x.get(key) == value, dictlist))


with open('library_data.json', 'r', encoding='utf-8') as f:
    Load_data = json.load(f)
    Temp_find = dict_filter(Load_data,"Serial","123421")
    print(Temp_find)