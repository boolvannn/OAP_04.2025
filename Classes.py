class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority  # "Высокий", "Средний", "Низкий"
        self.status = False  # False - не выполнено, True - выполнено

    def mark_completed(self):
        self.status = True

    def edit_description(self, new_description):
        if new_description:
            self.description = new_description
            print("Описание обновлено.")
        else:
            print("Описание не может быть пустым.")

    def edit_priority(self, new_priority):
        if new_priority in ["Высокий", "Средний", "Низкий"]:
            self.priority = new_priority
            print("Приоритет обновлён.")
        else:
            print("Недопустимое значение приоритета.")

    def __str__(self):
        status_str = "Выполнено" if self.status else "Не выполнено"
        return f"Описание: {self.description} | Приоритет: {self.priority} | Статус: {status_str}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, description, priority):
        if priority not in ["Высокий", "Средний", "Низкий"]:
            print("Ошибка: приоритет должен быть 'Высокий', 'Средний' или 'Низкий'.")
            return
        task = Task(description, priority)
        self.tasks.append(task)
        print("Задача создана.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return
        print("\nСписок задач:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_completed()
            print("Задача отмечена как выполненная.")
        else:
            print("Неверный номер задачи.")

    def edit_task(self, task_index, new_description=None, new_priority=None):
        if 0 <= task_index < len(self.tasks):
            task = self.tasks[task_index]
            if new_description:
                task.edit_description(new_description)
            if new_priority:
                task.edit_priority(new_priority)
        else:
            print("Неверный номер задачи.")