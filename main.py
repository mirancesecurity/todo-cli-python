import json
import sys
from pathlib import Path

TASKS_FILE = Path("tasks.json")


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(task_text):
    tasks = load_tasks()
    tasks.append(task_text)
    save_tasks(tasks)
    print(f"✅ Задача добавлена: {task_text}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 Список задач пуст")
        return

    print("📋 Список задач:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


def remove_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑 Удалена задача: {removed}")
    except IndexError:
        print("❌ Неверный номер задачи")


def show_help():
    print("""
Использование:
  python main.py add "Текст задачи"
  python main.py list
  python main.py remove <номер>

Примеры:
  python main.py add "Выучить Python"
  python main.py list
  python main.py remove 1
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "remove" and len(sys.argv) == 3:
        remove_task(int(sys.argv[2]))
    else:
        show_help()


if __name__ == "__main__":
    main()
