import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"
notes = []

def load_notes():
    global notes
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)

def save_notes():
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    date = datetime.now().date()  # Только дата, без времени
    note = {"id": len(notes) + 1, "title": title, "body": body, "date": str(date)}
    notes.append(note)
    save_notes()

def list_notes():
    print("Список заметок:")
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['date']}")

def read_note():
    note_id = int(input("Введите ID заметки для просмотра: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Текст: {note['body']}, Дата создания: {note['date']}")
    else:
        print("Заметка не найдена")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        print(f"Текущий заголовок: {note['title']}")
        note['title'] = input("Введите новый заголовок: ")
        print(f"Текущий текст: {note['body']}")
        note['body'] = input("Введите новый текст: ")
        save_notes()
        print("Заметка успешно отредактирована")
    else:
        print("Заметка не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    global notes
    notes = [note for note in notes if note['id'] != note_id]
    save_notes()
    print("Заметка успешно удалена")

def display_notes_after_date():
    date_str = input("Введите дату в формате YYYY-MM-DD: ")
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()  # Только дата, без времени
        filtered_notes = [note for note in notes if datetime.strptime(note['date'], "%Y-%m-%d").date() >= date]
        if filtered_notes:
            print("Заметки, созданные после", date_str + ":")
            for note in filtered_notes:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['date']}")
        else:
            print("Нет заметок, созданных после", date_str)
    except ValueError:
        print("Некорректный формат даты. Используйте YYYY-MM-DD.")