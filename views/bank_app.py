import tkinter as tk 
import customtkinter as ctk

class BankAPP:
    def __init__(self, root, db):
        self.root = root 
        self.db = db 

        root.title("Banks") 
        root.geometry("300x300")
        root.resizable(False, False)

        self.input_bank = ctk.CTkEntry(self.root, font=("sans-serif", 16), width=175, placeholder_text="Adicionar Banco") 
        self.input_bank.pack(pady=5)

        self.btn_add = ctk.CTkButton(root, text="Adicionar Banco", width=175, command=self.add_bank) 
        self.btn_add.pack(pady=5)

        self.scroll_frame = ctk.CTkScrollableFrame(self.root)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.show_account()

    def add_bank(self):
        name = self.input_bank.get()

        if name.strip(): 
            self.db.insert_bank(name)
            self.input_bank.delete(0, 'end')
            self.show_account()

    def show_account(self):
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        banks = self.db.get_banks()

        if not banks:
            return
        
        for idx, bank in enumerate(banks):
            id, name, value = bank

            text = f"{name:<20} | R$ {value:^4.2f}"
            lbl_item = ctk.CTkLabel(self.scroll_frame, text=text, font=("Courier", 14, "bold"))
            lbl_item.pack(anchor="w")

        self.root.update_idletasks()
