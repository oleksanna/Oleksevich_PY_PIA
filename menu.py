import notes

def main_menu():
    while True:
        print("\nГлавное меню:")
        print("1. Вывести список заметок")
        print("2. Создать новую заметку")
        print("3. Просмотреть заметку по ID")
        print("4. Редактировать заметку по ID")
        print("5. Удалить заметку по ID")
        print("6. Вывести заметки созданные после определенной даты")
        print("7. Выйти")
        choice = input("Выберите действие: ")
        
        if choice == "1":
            notes.list_notes()
        elif choice == "2":
            notes.create_note()
        elif choice == "3":
            notes.read_note()
        elif choice == "4":
            notes.edit_note()
        elif choice == "5":
            notes.delete_note()
        elif choice == "6":
            notes.display_notes_after_date()
        elif choice == "7":
            break
        else:
            print("Некорректный ввод, попробуйте еще раз.")