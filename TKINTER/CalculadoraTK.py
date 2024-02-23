import tkinter as tk
from tkinter import ttk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("228x155")

        self.num1_entry = ttk.Entry(self)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self, text="Número 1:").grid(row=0, column=0, padx=5, pady=5)

        self.num2_entry = ttk.Entry(self)
        self.num2_entry.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(self, text="Número 2:").grid(row=1, column=0, padx=5, pady=5)

        self.result_label = ttk.Label(self, text="Resultado:", anchor='center')
        self.result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.add_button = ttk.Button(self, text="+", command=self.add)
        self.add_button.grid(row=3, column=0, padx=15, pady=5)

        self.sub_button = ttk.Button(self, text="-", command=self.sub)
        self.sub_button.grid(row=3, column=1, padx=5, pady=5)

        self.mul_button = ttk.Button(self, text="*", command=self.mul)
        self.mul_button.grid(row=4, column=0, padx=5, pady=5)

        self.div_button = ttk.Button(self, text="/", command=self.div)
        self.div_button.grid(row=4, column=1, padx=5, pady=5)

    def add(self):
        try:
            result = float(self.num1_entry.get()) + float(self.num2_entry.get())
            self.result_label.config(text=f"Resultado: {result}")
        except ValueError:
            self.result_label.config(text="ERRO! Somente números.")

    def sub(self):
        try:
            result = float(self.num1_entry.get()) - float(self.num2_entry.get())
            self.result_label.config(text=f"Resultado: {result}")
        except ValueError:
            self.result_label.config(text="ERRO! Somente números.")

    def mul(self):
        try:
            result = float(self.num1_entry.get()) * float(self.num2_entry.get())
            self.result_label.config(text=f"Resultado: {result}")
        except ValueError:
            self.result_label.config(text="ERRO! Somente números.")

    def div(self):
        try:
            num2 = float(self.num2_entry.get())
            if num2 != 0:
                result = float(self.num1_entry.get()) / num2
                self.result_label.config(text=f"Resultado: {result}")
            else:
                self.result_label.config(text="ERRO! Somente números.")
        except ValueError:
            self.result_label.config(text="ERRO! Somente números.")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
