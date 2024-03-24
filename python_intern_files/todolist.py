from tkinter import messagebox
import tkinter as tk
class TodoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do")

        self.tasks = []

        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(master, text="Create", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.pack(pady=10)

        self.update_button = tk.Button(master, text="Update", command=self.update_task)
        self.update_button.pack()

        self.complete_button = tk.Button(master, text="Done", command=self.mark_as_completed)
        self.complete_button.pack()

        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.load_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")


    def update_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_task_index] = new_task
                self.task_entry.delete(0, tk.END)
                self.load_tasks()
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        else:
            messagebox.showwarning("Warning", "Please select a task to update!")

    def mark_as_completed(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            selected_task_index = selected_task_index[0]
            completed_task = self.tasks.pop(selected_task_index)
            self.load_tasks()
            messagebox.showinfo("Completed", f"Task '{completed_task}' marked as completed!")
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")


def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
