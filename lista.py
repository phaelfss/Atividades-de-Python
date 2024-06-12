import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Tarefas")

        self.label_task = tk.Label(master, text="Tarefa:")
        self.label_task.grid(row=0, column=0, sticky="w")

        self.entry_task = tk.Entry(master)
        self.entry_task.grid(row=0, column=1)

        self.add_button = tk.Button(master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.grid(row=0, column=2)

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.grid(row=1, column=0, columnspan=3, sticky="nsew")

        self.remove_button = tk.Button(master, text="Remover Tarefa Selecionada", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=3)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Por favor, digite uma tarefa.")

    def remove_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Aviso", "Por favor, selecione uma tarefa para remover.")

root = tk.Tk()
app = ToDoListApp(root)
root.mainloop()
