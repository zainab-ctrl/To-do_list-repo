import os
import json

fileName = "To-do list.json"

def load():
    if not os.path.exists (fileName):
        return []
    else:
        with open(fileName) as file:
            return json.load(file)

def save(tasks):
    with open(fileName, "w") as file:
        return json.dump(tasks, file, indent = 4)
        
def add(tasks):
    task = input("Enter the task:")
    if task:
        tasks.append({"task": task, "Status": False})
        print("Task added successfully.")
    else:
        print("Task added failed.")

def show(tasks):
    if not tasks:
        print("There is no tasks yet.")
        return
    if tasks:
        print("\t----Your To-Do List----")
        for index, task in enumerate(tasks, 1):
            status = "Done" if  task["Status"] else  "Not done"
            print(f"{index}. {task["task"]} [{status}]")

def markas_done(tasks):
    if not tasks:
        print("There is no tasks to mark as done.")
        return
    num = int (input("Enter the number of the task that has done:"))
    try:
        if num>=1 and num<=len(tasks):
         tasks[num-1]["Status"] = True
         print("Task has marked as done.")
        else:
         print("Task has failed to mark as done")
    except ValueError:
        print("Enter right value.")

def delete(tasks):
    if not tasks:
        print("There is no tasks to delete.")
        return
    num = int (input("Enter the number of task you want to delete:"))
    try:
        if num>=1 and num<=len(tasks):
            deleted = tasks.pop(num -1)
            print(f"Task:{deleted["task"]} has deleted successfully.")
        else:
            print("Task failed to delete.")
    except ValueError:
     print("Enter right value.")

def menu():
    print()
    print("\t\t------To-Do List App--------")
    print("1. Show list")
    print("2. Add task")
    print("3. Mark as Done")
    print("4. Delete")
    print("5. Exit")
    num = int (input("Select any above option(1-5):"))
    return num
    
def main():
    tasks = load()
    while True:
     num = menu()
     match num:
            case 1:
             show(tasks)
            case 2:
             add(tasks)
            case 3:
             markas_done(tasks)
            case 4:
             delete(tasks)
            case 5:
             save(tasks)
             print("Saving tasks and exiting the app.")
             break
            case _:
             print("Enter right option.")

if __name__ == "__main__":
     main()