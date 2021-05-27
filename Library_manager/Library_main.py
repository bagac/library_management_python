from Library_func import *
from Library_class import *

while True:
    typeData = int(input('''
    Add Document  = 1
    Add Book      = 2
    Add Magazine  = 3
    Add Newspaper = 4
    Tìm kiếm thông tin = 5
    Nhập vào chế độ theo mẫu trên:

    '''))
    if typeData == 1:
        Data_Document = Document.Add_infor(Document)
        print(Data_Document)
        Extend_json(Data_Document, 'library_data.json')
    elif typeData == 0:
        break
    elif typeData == 2:
        Data_Book = Book.Add_infor(Book)
        print(Data_Book)
        Extend_json(Data_Book, 'library_data.json')
    elif typeData == 3:
        Data_Magazine = Magazine.Add_infor(Magazine)
        print(Data_Magazine)
        Extend_json(Data_Magazine, 'library_data.json')
    elif typeData == 4:
        Data_Newspaper = Newspaper.Add_infor(Newspaper)
        print(Data_Newspaper)
        Extend_json(Data_Newspaper, 'library_data.json')
    elif typeData == 5:
        print('Dữ liệu được lưu dưới dạng {Tên quy ước : Tên tài liệu chính}')
        Key_find = input('nhập vào Tên quy ước : ')
        Value_find = input('nhập vào tên tài liệu/ báo/ sách/ tạp chí cần tìm: ')
        with open('library_data.json', 'r', encoding='utf-8') as f:
            Load_data = json.load(f)
            TempFind = dict_filter(Load_data, Key_find, Value_find)
            print(f'Dữ liệu tìm thấy: {TempFind}')

