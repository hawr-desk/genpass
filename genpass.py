import random

def collecting():
    #Сначала нужно собрать данные - сколько паролей
    #И для каких аккаунтов
    lenlist = input("Сколько паролей вы хотите сгенерировать?")
    print("Для каких аккаунтов?")
    i = 0

    spisok = [ ]
    while i < int(lenlist):
        self = input("Введите имя аккаунта: ")
        spisok.append(self)
        i+=1
    
    return lenlist, spisok


def parol():
    digits = '1234567890'
    leters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    leters_2='abcdefghijklmnopqrstuvwxyz'
    symbols = '!@#$%&*()-+'
    password = ' '
    var = [digits,leters, leters_2, symbols]

    #generation password

    password += random.choice(digits)
    password += random.choice(leters)
    password += random.choice(leters_2)
    password += random.choice(symbols)
    while len(password) < 17:
        password+=random.choice(var[random.randint(0,3)])
    
            
    return password 