# class ToDoList:
#     def __init__(self):
#         self.tasks = []
#         self.load_tasks()
#
#     def load_tasks(self):
#         try:
#             with open("tasks.txt", "r") as file:
#                 self.tasks = [line.strip() for line in file.readlines()]
#         except FileNotFoundError:
#             pass
#
#     def save_tasks(self):
#         with open("tasks.txt", "w") as file:
#             for task in self.tasks:
#                 file.write(task + "\n")
#
#     def display_tasks(self):
#         if not self.tasks:
#             print("No tasks in the list.")
#         else:
#             print("Tasks:")
#             for idx, task in enumerate(self.tasks, start=1):
#                 print(f"{idx}. {task}")
#
#     def add_task(self, new_task):
#         self.tasks.append(new_task)
#         self.save_tasks()
#         print(f"Task '{new_task}' added.")
#
#     def remove_task(self, task_index):
#         if 1 <= task_index <= len(self.tasks):
#             removed_task = self.tasks.pop(task_index - 1)
#             self.save_tasks()
#             print(f"Task '{removed_task}' removed.")
#         else:
#             print("Invalid task index.")
#
#     def mark_completed(self, task_index):
#         if 1 <= task_index <= len(self.tasks):
#             self.tasks[task_index - 1] += " (Completed)"
#             self.save_tasks()
#             print("Task marked as completed.")
#         else:
#             print("Invalid task index.")
#
#
# def main():
#     todo = ToDoList()
#     while True:
#         print("\n===== To-Do List Menu =====")
#         print("1. Display Tasks")
#         print("2. Add Task")
#         print("3. Remove Task")
#         print("4. Mark Task as Completed")
#         print("5. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             todo.display_tasks()
#         elif choice == "2":
#             new_task = input("Enter the new task: ")
#             todo.add_task(new_task)
#         elif choice == "3":
#             task_index = int(input("Enter the task index to remove: "))
#             todo.remove_task(task_index)
#         elif choice == "4":
#             task_index = int(input("Enter the task index to mark as completed: "))
#             todo.mark_completed(task_index)
#         elif choice == "5":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")
#
#
# if __name__ == "__main__":
#     main()




#added tkinter but something is not correct, not sure what

import tkinter as tk

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.tasks = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task + "\n")

    def display_tasks(self):
        if not self.tasks:
            self.output_label.config(text="No tasks in the list.")
        else:
            tasks_str = "Tasks:\n" + "\n".join(self.tasks)
            self.output_label.config(text=tasks_str)

    def add_task(self, new_task):
        self.tasks.append(new_task)
        self.save_tasks()
        self.output_label.config(text=f"Task '{new_task}' added.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            self.output_label.config(text=f"Task '{removed_task}' removed.")
        else:
            self.output_label.config(text="Invalid task index.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1] += " (Completed)"
            self.save_tasks()
            self.output_label.config(text="Task marked as completed.")
        else:
            self.output_label.config(text="Invalid task index.")

def display_tasks():
    todo.display_tasks()

def add_task():
    new_task = entry_task.get()
    todo.add_task(new_task)

def remove_task():
    task_index = int(entry_index.get())
    todo.remove_task(task_index)

def mark_completed():
    task_index = int(entry_index.get())
    todo.mark_completed(task_index)

def exit_program():
    root.destroy()

todo = ToDoList()

root = tk.Tk()
root.title("To-Do List")

label_task = tk.Label(root, text="Enter the new task:")
label_task.pack()

entry_task = tk.Entry(root)
entry_task.pack()

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.pack()

label_index = tk.Label(root, text="Enter the task index:")
label_index.pack()

entry_index = tk.Entry(root)
entry_index.pack()

button_display = tk.Button(root, text="Display Tasks", command=display_tasks)
button_display.pack()

button_remove = tk.Button(root, text="Remove Task", command=remove_task)
button_remove.pack()

button_completed = tk.Button(root, text="Mark Task as Completed", command=mark_completed)
button_completed.pack()

button_exit = tk.Button(root, text="Exit", command=exit_program)
button_exit.pack()

todo.output_label = tk.Label(root, text="")
todo.output_label.pack()

root.mainloop()