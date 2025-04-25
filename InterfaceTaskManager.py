from Classes import Task, TaskManager


def main():
    manager = TaskManager()
    print("Добро пожаловать в Таск-менеджер!")

    while True:
        print("\nДоступные команды:")
        print("1 - Создать задачу")
        print("2 - Просмотреть список задач")
        print("3 - Отметить задачу выполненной")
        print("4 - Редактировать задачу")
        print("5 - Выход")

        choice = input("Введите номер команды: ")

        if choice == "1":
            desc = input("Введите описание задачи: ")
            prio = input("Введите приоритет (Высокий, Средний, Низкий): ")
            manager.create_task(desc, prio)

        elif choice == "2":
            manager.list_tasks()

        elif choice == "3":
            index = int(input("Введите номер задачи для отметки выполнения: ")) - 1
            manager.mark_completed(index)

        elif choice == "4":
            index = int(input("Введите номер задачи для редактирования: ")) - 1
            new_desc = input("Новое описание (или оставьте пустым): ")
            new_prio = input("Новый приоритет (Высокий, Средний, Низкий) или оставьте пустым: ")
            manager.edit_task(index, new_description=new_desc or None, new_priority=new_prio or None)

        elif choice == "5":
            print("Выход из программы.")
            break
        else:
            print("Неверная команда. Повторите ввод.")

print(main())
