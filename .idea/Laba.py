import pickle


class University:
    def __init__(self, faculties, faculty_info):
        self.faculties = faculties
        self.faculty_info = faculty_info
        self.faculty = None

    def choose_faculty(self):
        for i, faculty in enumerate(self.faculties):
            print(f"{i + 1}: {faculty}")
        print(f"8: Повернутися назад")
        print(f"9: Вийти в головне меню")
        index = input("Виберіть факультет з яким хочете працювати:")
        try:
            index = int(index)
        except ValueError:
            print("Невідома опція. Спробуйте ще раз.\n")
            return self.choose_faculty()
        if 1 <= index <= len(self.faculties):
            self.faculty = self.faculties[index - 1]
        elif index == 8:
            menu()
        elif index == 9:
            main()
        faculty = Faculty(self.faculty, self.faculties, self.faculty_info)
        return faculty.choose_option()


class Faculty(University):
    def __init__(self, faculty, faculties, faculty_info):
        super().__init__(faculties, faculty_info)
        self.faculty = faculty

    def choose_option(self):
        print("1. Створити інформацію про факультет.")
        print("2. Видалити інформацію про факультет.")
        print("3. Редагувати інформацію про факультет.")
        print("4. Повернутися назад")
        print("5. Вийти в головне меню")  # В нас дахуя однакових прінтів я заєбався вже їх писати
        choice = input("Оберіть опцію: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Невідома опція. Спробуйте ще раз.\n")
            self.choose_option()
        choices = [self.add_info, self.delete_info, self.edit_info, self.choose_faculty, menu]
        if 1 <= choice <= len(choices):
            choices[choice - 1]()
        # Я не розумію якого хуя якщо я скіпаю некст раз заапускаю і тут блять помилка але код виконує
        return

    def add_info(self):
        info = input("Введіть інформацію яку хочете додати")
        self.faculty_info[self.faculty].append(info)

    def delete_info(self):
        for i, info in enumerate(self.faculty_info[self.faculty]):
            print(f"{i + 1}. {info}")
        choice = input("Оберіть опцію: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Невідома опція. Спробуйте ще раз.\n")
            self.delete_info()
        self.faculty_info[self.faculty].pop(choice - 1)
        print(self.faculty_info[self.faculty])

    def edit_info(self):
        for i, info in enumerate(self.faculty_info[self.faculty]):
            print(f"{i + 1}. {info}")
        choice = input("Оберіть опцію: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Невідома опція. Спробуйте ще раз.\n")
            self.edit_info()
        new_info = input(f"Введіть нову інформацію: ")
        self.faculty_info[self.faculty][choice - 1] = new_info
        print(self.faculty_info[self.faculty])


def main():
    while True:
        print("1. Показати меню")
        print("2.  Вийти")
        choice = input("Оберіть опцію: ")
        if choice == "2":
            break
        elif choice == "1":
            menu()
        else:
            print("Невідома опція. Спробуйте ще раз.\n")


def menu():
    with open("faculties.pickle", 'rb') as f:
        faculties = pickle.load(f)
    with open("faculties_info.pickle", "rb") as file:
        faculties_info = pickle.load(file)
    university = University(faculties, faculties_info)
    while True:
        print("Меню:")
        print("1. Створити/видалити/редагувати інформацію про факультет.")
        # print("2. Створити/видалити/редагувати інформацію про кафедру [конкретного] факультета.")
        # print(
        #     "3. Додати/видалити/редагувати інформацію про студента на [конкретній] кафедрі [конкретного] факультета.")
        # print(
        # "4. Додати/видалити/редагувати інформацію про викладача на [конкретній] кафедрі [конкретного] факультета.")
        # print("5. Знайти інформацію про студента за ПІБ, курсом або групою.")
        # print("6. Знайти інформацію про викладача за ПІБ, курсом або групою.")
        # print("7. Вивести інформацію про всіх студентів впорядкованих за курсами.")
        # print("8. Вивести інформацію про всіх студентів факультета впорядкованих за алфавітом.")
        # print("9. Вивести інформацію про всіх викладачів факультета впорядкованих за алфавітом.")
        print("10. Вийти")
        choice = input("Оберіть опцію: ")
        if choice == "1":
            university.choose_faculty()
            break
        # elif choice == "2":
        #     # додавання кафедри
        #     pass
        # elif choice == "3":
        #     # додавання викладача
        #     pass
        # elif choice == "4":
        #     # додавання студента
        #     pass
        # elif choice == "5":
        #     university.view_departments()
        # elif choice == "6":
        #     university.view_lecturers()
        # elif choice == "7":
        #     university.view_students()
        # elif choice == "8":
        #     university.view_faculties()
        # elif choice == "9":
        #     filename = input("Введіть ім'я файлу для збереження: ")
        #     university.save_to_json(filename)
        #     print(f'Дані успішно збережено у файл {filename}.\n')
        elif choice == "10":
            print("Програма завершила свою роботу.")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.\n")


main()
