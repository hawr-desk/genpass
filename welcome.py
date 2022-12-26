import genpass

print("Привет. Данный скрипт создан для генерации паролей.")
print("Все пароли созданы случайным образом.")

print("Что ты хочешь сделать?")
print("1 - Посмотреть пароль?")
print("2 - Сгенерировать пароль!")
listpass =[ ] #отдельный список для паролей
#для паролей и для имен аккаунтов делается разные списки
#сделано это для более комфортного дальнейшего хэширования паролей
ans = input()

if ans == str(2):
    lenlist, name = genpass.collecting() #принимаем данные опроса - количество паролей и имена аккаунтов
    print("Вы хотите сгенерировать ", lenlist, " паролей для: ", name)
    lenlist = int(lenlist)
    ask = input("Всё верно?(y/n) ")
    if ask == ('n' or 'N'):
        exit()
    else:
        i = 0
        while i < lenlist: #генерируем пароли с разными сидами
            password = genpass.parol()
            listpass.append(password) #загоняем в список пароли
            print(name[i], listpass[i])
            i+=1

        ans = input("Хотите сохранить пароли?(y/n) ")

        if ans == 'y' or 'Y':
            
            #save name accounts
            namefile = open('name_accounts.txt', 'w')
            i = 0
            while i < lenlist:
                namefile.write(str(name[i]))
                i += 1
            namefile.close()

            #hashing and save passwords
            hashpass = []
            passfile = open('save.txt', 'w')
            i = 0
            while i < lenlist:
                self = hash(listpass[i])
                hashpass.append(self)
                passfile.write(str(hashpass[i]))
                i+=1
            
            passfile.close()
        else:
            exit()
            