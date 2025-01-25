import tkinter as tk

tasks = []

def add_task():
    task = entry_task.get()
    tasks.append(task)
    output_text.set(f"Task '{task}' added to the list.")

def list_tasks():
    if not tasks:
        output_text.set("There are no tasks currently.")
    else:
        task_list = "Current Tasks:\n"
        for index, task in enumerate(tasks):
            task_list += f"Task #{index}: {task}\n"
        output_text.set(task_list)

def delete_task():
    try:
        task_to_delete = int(entry_delete.get())
        if 0 <= task_to_delete < len(tasks):
            tasks.pop(task_to_delete)
            output_text.set(f"Task {task_to_delete} has been removed.")
        else:
            output_text.set(f"Task #{task_to_delete} was not found.")
    except ValueError:
        output_text.set("Invalid input. Please enter a number.")

root = tk.Tk()
root.title("To-Do List App")

label_task = tk.Label(root, text="Task:")
label_task.grid(row=0, column=0)

entry_task = tk.Entry(root)
entry_task.grid(row=0, column=1)

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.grid(row=0, column=2, padx=5)

button_list = tk.Button(root, text="List Tasks", command=list_tasks)
button_list.grid(row=1, column=0, pady=5)

label_delete = tk.Label(root, text="Task # to Delete:")
label_delete.grid(row=1, column=1)

entry_delete = tk.Entry(root)
entry_delete.grid(row=1, column=2)

button_delete = tk.Button(root, text="Delete Task", command=delete_task)
button_delete.grid(row=1, column=3, padx=5)

output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text, wraplength=250)
output_label.grid(row=2, columnspan=4, pady=5)

root.mainloop()
