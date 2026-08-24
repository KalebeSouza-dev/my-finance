import tkinter as tk 
import customtkinter as ctk

from tkinter import messagebox 

class FinanceAPP: 
    def __init__(self, root, db): 
        self.root = root 
        self.db = db 

        # window
        root.title("My Finance") 
        root.geometry("300x200") 

        self.lbl_balance = ctk.CTkLabel(root, text="Saldo: R$ 0.00", font=("sans-serif", 24, "bold")) 
        self.lbl_balance.pack(pady=10) 

        # value
        self.input_value = ctk.CTkEntry(self.root, font=("sans-serif", 16), width=175, placeholder_text="Valor") 
        self.input_value.pack(pady=5)

        # description
        self.input_desc = ctk.CTkEntry(self.root, font=("sans-serif", 16), width=175, placeholder_text="Descrição") 
        self.input_desc.pack(pady=5)

        # next input
        self.input_value.bind("<Return>",lambda event: self.input_desc.focus()) 
        self.input_value.bind("<KP_Enter>", lambda event: self.input_desc.focus())   
        self.input_desc.bind("<Return>", self.add_transaction) 
        self.input_desc.bind("<KP_Enter>", self.add_transaction)

        self.btn_add = ctk.CTkButton(root, text="Adicionar Transação", command=self.add_transaction) 
        self.btn_add.pack(pady=15) 

        self.update_balance() 

    def update_balance(self): 
        balance = self.db.get_balance() 
        self.lbl_balance.configure(text=f"Saldo: R$ {balance:.2f}", font=("sans-serif", 24, "bold")) 
         
        print(self.db.get_historic()) 

    def add_transaction(self, event=None): 
        try: 
            value = float(self.input_value.get()) 

            desc = self.input_desc.get()

            self.db.insert_transaction(value, desc) 

            self.update_balance() 

            self.input_value.delete(0, tk.END) 
            self.input_desc.delete(0, tk.END) 

            self.input_value.focus()
        except ValueError: 
            messagebox.showerror("Error", "Valor Inválido")