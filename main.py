import csv
import os
from datetime import datetime
from time import sleep
from multiprocessing import Process
from email_notification import send_email

current_directory = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_directory, "tasks.csv")

def save_new_task(task_name: str, remainder_date: datetime):
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            added_tasks = {row["Task name"]: row["Due to date"] for row in reader}
    except FileNotFoundError:
        added_tasks = {}

    added_tasks[task_name] = remainder_date.strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "w", newline="") as file:
        writer = csv.writter(file)
        writer.writerow(["Task name", "Due to date"])
        for task, due_date in added_tasks.items():
            writer.writerow([task, due_date])

def create_task():
    task_name = input("Enter task name: ")
    reminder_date_str = input("Enter date to remind in this format \"yyyy-mm-dd hh:mm\": ")
    reminder_date = datetime.strptime(reminder_date_str, "%Y-%m-%d %H:%M")
    save_new_task(task_name, reminder_date)

def get_all_tasks():
    try:
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            added_tasks = {row["Task name"]: row["Due to date"] for row in reader}
    except FileNotFoundError:
        added_tasks = {}

    return added_tasks

def print_all_tasks():
    added_tasks = get_all_tasks()
    sorted_tasks_asc = dict(sorted(added_tasks.items(), key=lambada x: x[1]))

    for task in sorted_tasks_asc:
        print(f"Task name: {task} | Due to date: {sorted_tasks_asc[task]}")

def check_if_should_remind():
    while True:
        added_tasks = get_all_tasks()

        new_task_list = {}
        for task in added_tasks:
            if datetime.strftime(added_tasks, "%Y-%m-%d %H:%M:%S") <= datetime.now():
                send_email(f"You have to complete this task right now! \n{task}")
                print("Check your mailbox")
            else:
                new_task_list[task] = added_tasks[task]

        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task name", "Due to date"])
            for task, due_date in added_tasks.items():
                writer.writerow(task, due_date)
        sleep(60)

def main():
    reminder_process = Process(target=check_if_should_remind)
    reminder_process.start()

    while True:
        option = input("Please, choose option (1-create new task 2-get list of all tasks 3-stop program): ")

        if option == '1':
            create_task()
        elif option == '2':
            print_all_tasks()
        elif option == '3':
            reminder_process.terminate()
            break
        else:
            print("Please make a valid input")

if __name__ == '__main__':
    main()