# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной1



import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file: 
        data = sorted(file.readlines())

        for contact in data:
            print(contact, end='')
    
    print("", end="\n")

    input('\npress any key')

def add_contact(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Input a surname of contact: ') + ' '
        res += input('Input a name of contact: ') + ' '
        res += input('Input a phone number of contact: ')

        file.write('\n'+ res)
    
    input('Contact was successfully added! Press any key for return')
        
def search_contact(file_name):
    os.system('CLS')
    target = input('Input a name of contact for searching: ')

    with open(file_name, 'r') as file: 
        contacts = file.readlines()

        for contact in contacts:                
            if target in contact:
                print(contact)
                break
        else :
            print('there is no contacts with this name.')

    input('press any key')

def drawing():
    print('1 - show contacts')
    print('2 - add contact')
    print('3 - search contact')
    print('4 - delete contact')
    print('5 - change contact')
    print('6 - exit')

def delete_data(file_name):
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print('')
        index_delete_data = int(input("Input string number to delete:"))-1
        tel_book_lines = tel_book.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
    with open(file_name, 'w', encoding='utf-8') as data:
        data.write('\n'.join(tel_book_lines))
    input('press any key')

def change_data(file_name):
    os.system('CLS')
    with open(file_name, 'r+', encoding='utf-8') as data:
        tel_book = data.read()
        print("Current contacts are:")
        print()
        print(tel_book)
        print('')
        index_delete_data = int(input("Input string number to change:"))-1
        tel_book_lines = tel_book.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        res = ''
        res += input('Input a new surname of contact: ') + ' '
        res += input('Input a new name of contact: ') + ' '
        res += input('Input a new phone number of contact: ')
        tel_book_lines.append(res)
        data.write('\n'.join(tel_book_lines))
    input('press any key')


def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Input a number from 1 to 6: "))

        if user_choice == 1 :
            show_contacts(file_name)
        elif user_choice == 2 :
            add_contact(file_name)
        elif user_choice == 3 :
            search_contact(file_name)
        elif user_choice == 4 :
            delete_data(file_name)
        elif user_choice == 5 :
            change_data(file_name)
        elif user_choice == 6 :
            print('Have a nice day!')
            return
            
        

main('test.txt')