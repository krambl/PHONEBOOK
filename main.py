import sys
import json
databasa_file = 'I:/MY_PROJECT/PHONEBOOK/databasa.json'

class PhoneBook():
    name = ''
    last_name = ''
    phone = ''

    # Открывает файл базы данных. Возвращает базу в ввиде массива
    def open_base(self):
        with open(databasa_file) as filek:
            db = json.load(filek)
            return db

    # Открывает файл базы данных для записи. Принимает отредактированную базу данных.
    def save_base(self,db):
        with open(databasa_file, 'w') as filek:
            json.dump(db, filek)

    # Создает объект контакт, вносит его в базу
    def create(self):
        self.name = input('Внесите имя, для продолжения enter: ')
        self.last_name= input('Внесите фамилию, для продолжения enter: ')
        self.phone = input('Внесите номер телефона, для продолжения enter: ')
        data = {'self.name':self.name,'self.last_name':self.last_name,'self.phone':self.phone}
        db = self.open_base()
        db.append(data)
        self.save_base(db)

    # Выводит данные о контакте
    def show(self):
        print(self.name + ' ' + self.last_name + ' ' + self.phone)

    # Выводит все контакты в базе
    def show_all(self):
        with open(databasa_file) as filek:
            db = json.load(filek)
            for i in range(len(db)):
                con_tact = db[i]['self.name'] + ' ' + db[i]['self.last_name'] + ' ' + db[i]['self.phone']
                print(con_tact)


    # Вывод контакта при совпадении одного запроса и одного из его атрибутов( имени, фамилии, номера)
    def search_contact(self,data,search):
        for i in range(len(data)):
            if search == data:
                self.show()
                break
            else:data = data[0:-1]

    # Поиск контакта по имени
    def search_name(self,search):
        self.search_contact(self.name,search)

    # Поиск контакта по Фамилии
    def search_last_name(self,search):
        self.search_contact(self.last_name,search)

    # Поиск контакта по номеру телефона
    def search_phone(self,search):
        self.search_contact(self.phone,search)

    # Поиск по всем атрибутам контакта
    def search_all(self,search):
        self.search_contact(self.name,search)
        self.search_contact(self.last_name,search)
        self.search_contact(self.phone,search)

    # Поиск по всем контактам, по всем атрибутам контакта
    def search_base(self):
        db = self.open_base()
        search = input('Введите критерий для поиска: ')
        for i in range(len(db)):
            con = PhoneBook()
            con.name = db[i]['self.name']
            con.last_name = db[i]['self.last_name']
            con.phone = db[i]['self.phone']
            con.search_all(search)



contact = PhoneBook()
contact.show_all()