import os, re


def phone_format(n):  # форматирование телефонного номера
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]


def printData(data):  # Функция вывода телефонной книги в консоль
    phoneBook = []
    splitLine = "=" * 49
    print(splitLine)
    print(" №  Фамилия        Имя          Телефонные номера")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, phone = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "Фамилия": lastName,
                "Имя": name,
                "телефон": phone_format(phone),
            }
        )
        personID += 1

    for contact in phoneBook:
        personID, lastName, name, phone = contact.values()
        print(f"{personID:>2}. {lastName:<15} {name:<10} -- {phone:<15}")

    print(splitLine)


def showContacts(fileName):  # Функция открытия телефонной книги
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("\n--- нажмите любую кнопку ---")


def addContact(fileName):  # Функция добавления нового контакта в телефонную книгу
    os.system("cls")
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите фамилию для контакта: ") + ","
        res += input("Введите имя для контакта: ") + ","
        res += input("Введите телефон для контакта: ")

        file.write(res + "\n")

    input("\nКонтакт был успешно добавлен!\n--- нажмите любую кнопку ---")


def findContact(fileName):  # Функция поиска контактов в телефонной книге
    os.system("cls")
    target = input("Введите данные контакта для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)
                # break

    if len(result) != 0:
        printData(result)
    else:
        print(f"Здесь нет контакта с заданными данными '{target}'.")

    input("--- нажмите любую кнопку ---")


def changeContact(fileName):  # Функция изменения информации в контакте
    os.system("cls")
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для изменения или 0 для возврата в главное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите новую фамилию: ")
            newName = input("Введите новое имя: ")
            newPhone = input("Введите новый телефон: ")
            data[numberContact - 1] = (
                newLastName + "," + newName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт был успешно изменен")
                input("\n--- нажмите любую кнопку ---")
        else:
            return


def deleteContact(fileName):  # Функция удаления контакта из телефонной книги
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите номер контакта для удаления или 0 для возврата в главное меню: ")
        )
        if numberContact != 0:
            print(f"Deleting record: {data[numberContact-1].rstrip().split(',')}\n")
            data.pop(numberContact - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return

    input("--- press any key ---")


def drawInterface():  # Функция рисования интерфейса главного меню
    print("#####   PHONE BOOK   #####")
    print("=" * 26)
    print(" [1] -- Показать контакты")
    print(" [2] -- Добавить контакты")
    print(" [3] -- Найти контакты")
    print(" [4] -- Изменить контакты")
    print(" [5] -- Удалить контакты")
    print("\n [0] -- Выход")
    print("=" * 26)


def main(file_name):  # Функция реализации главного меню
    while True:
        os.system("cls")
        drawInterface()
        userChoice = int(input("Введите номер от 1 до 5 или 0 для выхода: "))

        if userChoice == 1:
            showContacts(file_name)
        elif userChoice == 2:
            addContact(file_name)
        elif userChoice == 3:
            findContact(file_name)
        elif userChoice == 4:
            changeContact(file_name)
        elif userChoice == 5:
            deleteContact(file_name)
        elif userChoice == 0:
            print("Спасибо!")
            return


path = "phonebook.txt"

main(path)