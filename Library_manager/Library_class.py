class Document:
    List_Document = []
    Data = {}

    def __init__(self, Document_Name, Document_Serial, Document_Company, Document_Number_Reissue):
        self.Document_Name = Document_Name
        self.Document_Serial = Document_Serial
        self.Document_Company = Document_Company
        self.Document_Number_Reissue = Document_Number_Reissue

    def Add_infor(self):
        dict_one = {}
        Name = input('Nhập tên tài liệu:')
        Serial = input('nhập serial: ')
        Company = input('nhập tên nhà xuất bản: ')
        Number = input('nhập số bản phát hành: ')
        Temp_one = Document(Name, Serial, Company, Number)
        dict_one['Document_Name'] = Temp_one.Document_Name
        dict_one['Serial'] = Temp_one.Document_Serial
        dict_one['Company'] = Temp_one.Document_Company
        dict_one['Reissue'] = Temp_one.Document_Number_Reissue
        Document.List_Document.append(dict_one)
        return dict_one

    def Show_Data(self):
        print('Danh sách tài liệu lưu trũ: ', Document.List_Document)


class Book(Document):
    List_Book = []

    def __init__(self, Book_Name, Book_author, Paper_number):
        super(Book, self).__init__(Book_Name, None, Book_author, Paper_number)

    def Add_infor(self):
        dict_one = {}
        Book_name = input('Nhập tên sách: ')
        Book_author = input('nhập Tên tác giả: ')
        Paper_number = input('nhập số trang: ')
        Temp_one = Book(Book_name, Book_author, Paper_number)
        dict_one['Book_Name'] = Temp_one.Document_Name
        dict_one['Author'] = Temp_one.Document_Company
        dict_one['Paper_number'] = Temp_one.Document_Number_Reissue
        Book.List_Book.append(dict_one)
        return dict_one


    def Show_Data(self):
        print('Danh sách các loại sách lưu trũ: ', self.List_Book)


class Magazine(Document):
    List_Magazine = []

    def __init__(self, Magazine_Name, Reissue_number, Reissue_month):
        super(Magazine, self).__init__(Magazine_Name, None, None, Reissue_number)
        self.Reissue_month = Reissue_month

    def Add_infor(self):
        dict_one = {}
        Magazine_Name = input('Nhập tên tạp chí: ')
        Reissue_number = input('nhập số bản phát hành: ')
        Reissue_month = input('nhập tháng phát hành: ')
        Temp_one = Magazine(Magazine_Name, Reissue_number, Reissue_month)
        dict_one['Magazine_Name'] = Temp_one.Document_Name
        dict_one['Reissue_number'] = Temp_one.Document_Number_Reissue
        dict_one['Reissue_month'] = Temp_one.Reissue_month
        Magazine.List_Magazine.append(dict_one)
        return dict_one

    def Show_Data(self):
        print('Danh sách tạp chí lưu trũ: ', self.List_Magazine)


class Newspaper(Magazine):
    List_Newspaper = []

    def __init__(self, Newspaper_name, Reissue_day):
        super(Newspaper, self).__init__(Newspaper_name, None, Reissue_day)

    def Add_infor(self):
        dict_one = {}
        Newspaper_name = input('nhập tên tờ báo: ')
        Reissue_day = input('nhập ngày phát hành: ')
        Temp_one = Newspaper(Newspaper_name, Reissue_day)
        dict_one['Newspaper_name'] = Temp_one.Document_Name
        dict_one['Day_Reissue'] = Temp_one.Reissue_month
        Newspaper.List_Newspaper.append(dict_one)
        return dict_one

    def Show_Data(self):
        print('Danh sách tạp chí lưu trũ: ', self.List_Newspaper)
