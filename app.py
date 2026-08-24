import tkinter as tk 
import customtkinter as ctk

from tkinter import messagebox 

class FinanceAPP: 
    def __init__(self, root, db): 
        self.root = root 
        self.db = db 

        # window
        root.title("My Finance") 
        root.attributes('-type', 'splash')
        root.geometry("300x230+20+20")
        root.lower()

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

        self.btn_add = ctk.CTkButton(root, text="Adicionar Transação", width=175, command=self.add_transaction) 
        self.btn_add.pack(pady=5) 

        # show history
        self.btn_history = ctk.CTkButton(self.root, text="Mostrar Histórico", width=175, command=self.show_history) 
        self.btn_history.pack(pady=5)

        self.update_balance() 

    def update_balance(self): 
        balance = self.db.get_balance() 
        self.lbl_balance.configure(text=f"Saldo: R$ {balance:.2f}", font=("sans-serif", 24, "bold")) 
         
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

    def show_history(self):
        if getattr(self, "history_window", None) is not None and self.history_window.winfo_exists():
            self.history_window.focus()
            return
        
        self.history_window = ctk.CTkToplevel(self.root)
        self.history_window.title("Transaction History")
        self.history_window.geometry("550x300")
        
        self.history_window.focus()

        scroll_frame = ctk.CTkScrollableFrame(self.history_window, width=500, height=250)
        scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        history = self.db.get_historic(100)

        if not history:
            lbl_empty = ctk.CTkLabel(scroll_frame, text="No transactions recorded.", font=("sans-serif", 16))
            lbl_empty.pack(pady=20)
            return

        for idx, item in enumerate(history):
            t_id, value, created_at, bank_id, desc = item
            
            if not desc:
                desc = "ENTRADA" if value >= 0 else "SAIDA"

            #date
            simple_date = created_at.split(' ')[0]
            year, month, day = simple_date.split('-')
            formatted_date = f"{day}/{month}/{year}"
            
            text_color = "#00FF2F" if value >= 0 else "#FF0000"
            
            formatted_desc = desc.upper()[:20]
            line_text = f"{idx+1:^3} - {formatted_date:^12}  |  {formatted_desc:<20}  |  R$ {value:>9.2f}"
            
            lbl_item = ctk.CTkLabel(scroll_frame, text=line_text, font=("Courier", 14, "bold"), text_color=text_color)
            lbl_item.pack(anchor="w")