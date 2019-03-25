import datetime
import csv
from datetime import datetime


def main_menu():
    print("\n")
    print("1. Show all tasks")
    print("2. Show pending task")
    print("3. Add new task")
    print("4. Resolve task")
    print("5. Find task")
    print("6. Exit")
    selection = int(input("Enter choice:"))
    if selection == 1:
        app.show_tasks()
    elif selection == 2:
        app.show_pending_tasks()
    elif selection == 3:
        app.add_task_interactive()
    elif selection == 4:
        app.resolve_task()
    elif selection == 5:
        app.find_by_name()
    elif selection == 6:
        exit()
    else:
        print("Invalid choice. Enter 1-6")


class Task:
    name = ''
    date = datetime.strptime("2018-03-01", "%Y-%m-%d")
    status = ''

    def __init__(self, name, date, status):
        self.name = name
        self.date = date
        self.status = status

    def __str__(self):
        return self.name + "," + str(self.date.date()) + "," + self.status


class Application:
    tasks = []

    def __init__(self):
        with open(r'dane.csv', newline='', encoding='utf8') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            for row in reader:
                self.tasks.append(self.add_task(row[0], row[1], row[2]))
        self.tasks = list(filter(self.exists, self.tasks))

    def exists(self, it):
        return it is not None

    def get_date(self, value):
        return value.date

    def show_tasks(self):
        print("Name," + '\t' + "Date," + '\t' + "Status")
        self.tasks.sort(key=self.get_date)
        for task in self.tasks:
            print(task)

    def show_pending_tasks(self):
        print("Name," + '\t' + "Date," + '\t' + "Status")
        for index, task in enumerate(self.tasks):
            if task.status == 'new':
                print(index, task.name + ",", task.date.date(), task.status)

    def add_task_interactive(self):
        while True:
            n = input('Enter the name of the task: ')
            if len(n) < 5:
                print('Task name should be at least 5 characters long!')
            else:
                break

        while True:
            d = input('Enter a date in YYYY-MM-DD format:')
            try:
                data1 = datetime.strptime(d, "%Y-%m-%d")
                print("Name," + '\t' + "Date," + '\t' + "Status")
                break
            except ValueError as e:
                print('ValueError:', e)

        self.add_task(n, data1, 'new')

    def add_task(self, name, date, status):
        date_object = date
        if isinstance(date, str):
            date_object = datetime.strptime(date, "%Y-%m-%d")
        new_task = Task(name, date_object, status)
        self.tasks.append(new_task)
        print(new_task)

    def resolve_task(self):
        app.show_pending_tasks()
        print("\n")
        while True:
            index = int(input('Enter the id of the task, that you want mark as DONE:'))
            try:
                if self.tasks[index].status == "new":
                    self.tasks[index].status = "done"
                    break
                else:
                    print('Incorrect Id! Try again!')
            except IndexError as e:
                print('ValueError:', e)
        app.show_pending_tasks()

    def find_by_name(self):
        while True:
            z = input('Enter a name:').lower()
            for task in self.tasks:
                if z == task.name.lower():
                    print(task)
                    return
            print("No such task! Try again!")


app = Application()

while True:
    main_menu()
