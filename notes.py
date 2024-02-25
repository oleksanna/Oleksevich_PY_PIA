import json
import os
from datetime import datetime

NOTES_FILE = "notes.json"
notes = []

def load_notes():
    global notes
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            for line in file:
                notes.append(json.loads(line))

def save_notes():
    with open(NOTES_FILE, "w") as file:
        for note in notes:
            file.write(json.dumps(note) + "\n")

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().isoformat()
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}
    notes.append(note)
    save_notes()

def list_notes():
    print("Список заметок:")
    for note in notes:
        print(f"{note['id']}. {note['title']} - {note['timestamp']}")

def read_note():
    note_id = int(input("Введите ID заметки для чтения: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата создания: {note['timestamp']}")
    else:
        print("Заметка не найдена")

def edit_note():
    note_id = int(input("Введите ID заметки для редактирования: "))
    note = next((note for note in notes if note['id'] == note_id), None)
    if note:
        note["title"] = input("Введите новый заголовок заметки: ")
        note["body"] = input("Введите новый текст заметки: ")
        note["timestamp"] = datetime.now().isoformat()
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