import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de IMC")

        self.label_height = tk.Label(master, text="Altura (m):")
        self.label_height.grid(row=0, column=0)

        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=0, column=1)

        self.label_weight = tk.Label(master, text="Peso (kg):")
        self.label_weight.grid(row=1, column=0)

        self.entry_weight = tk.Entry(master)
        self.entry_weight.grid(row=1, column=1)

        self.calculate_button = tk.Button(master, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, columnspan=2)

        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=3, columnspan=2)

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())

            if height <= 0 or weight <= 0:
                raise ValueError("Altura e peso devem ser positivos.")

            bmi = weight / (height ** 2)
            bmi_category = self.get_bmi_category(bmi)

            result_text = f"Seu IMC é {bmi:.2f}, o que indica {bmi_category}."
            self.label_result.config(text=result_text)
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            self.label_result.config(text="")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Abaixo do peso"
        elif bmi < 24.9:
            return "Peso normal"
        elif bmi < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"

root = tk.Tk()
app = BMICalculator(root)
root.mainloop()
