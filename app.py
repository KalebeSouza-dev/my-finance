import tkinter as tk 
from tkinter import messagebox 

class FinanceAPP: 
    def __init__(self, root, db): 
        self.root = root 
        self.db = db 

        root.title("My Finance") 
        root.geometry("300x200") 

        self.lbl_balance = tk.Label(root, text="Saldo: R$ 0.00", font=("Arial", 24)) 
        self.lbl_balance.pack(pady=20) 

        self.input_value = tk.Entry(root, font=("Arial", 21)) 
        self.input_value.pack(pady=5) 
        self.input_value.bind("<Return>", self.add_value) 
        self.input_value.bind("<KP_Enter>", self.add_value)   

        self.btn_add = tk.Button(root, text="Adicionar Transação", command=self.add_value) 
        self.btn_add.pack(pady=5) 

        self.update_balance() 

    def update_balance(self): 
        balance = self.db.get_balance() 
        self.lbl_balance.config(text=f"Saldo: R$ {balance:.2f}") 
         
        print(self.db.get_historic()) 

    def add_value(self, event=None): 
        try: 
            value = float(self.input_value.get()) 
            self.db.insert_value(value) 

            self.update_balance() 
            self.input_value.delete(0, tk.END) 
        except ValueError: 
            messagebox.showerror("Error", "Valor Inválido")