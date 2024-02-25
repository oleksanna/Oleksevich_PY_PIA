import notes

def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Читать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            notes.create_note()
        elif choice == "2":
            notes.list_notes()
        elif choice == "3":
            notes.read_note()
        elif choice == "4":
            notes.edit_note()
        elif choice == "5":
            notes.delete_note()
        elif choice == "6":
            break
        else:
            print("Некорректный ввод, попробуйте еще раз.")