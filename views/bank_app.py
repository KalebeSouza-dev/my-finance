import tkinter as tk 
import customtkinter as ctk

class BankAPP:
    def __init__(self, root, db):
        self.root = root 
        self.db = db 

        root.title("Patrimônio") 
        root.geometry("300x380")
        root.resizable(False, False)

        self.input_bank = ctk.CTkEntry(self.root, font=("sans-serif", 16), width=175, placeholder_text="Nome da fonte") 
        self.input_bank.pack(pady=5)

        self.input_bank.bind("<Return>", self.add_bank) 
        self.input_bank.bind("<KP_Enter>", self.add_bank)

        self.btn_add = ctk.CTkButton(root, text="Adicionar fonte", width=175, command=self.add_bank) 
        self.btn_add.pack(pady=5)

        self.scroll_frame = ctk.CTkScrollableFrame(self.root)
        self.scroll_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.lbl_total = ctk.CTkLabel(self.root, text="PATRIMÔNIO TOTAL: R$ 0.00", font=("Arial", 16, "bold"))
        self.lbl_total.pack(pady=(0, 5))

        self.show_account()

    def add_bank(self, event=None):
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
            self.lbl_total.configure(text="PATRIMÔNIO TOTAL: R$ 0.00")
            return
        
        for idx, bank in enumerate(banks):
            b_id, name, value = bank

            row_frame = ctk.CTkFrame(self.scroll_frame, fg_color="transparent")
            row_frame.pack(fill="x", pady=2)

            lbl_name = ctk.CTkLabel(row_frame, text=name, font=("Arial", 14, "bold"), anchor="w", width=120)
            lbl_name.pack(side="left", padx=5)

            lbl_rs = ctk.CTkLabel(row_frame, text="R$", font=("Arial", 14))
            lbl_rs.pack(side="left")

            entry_val = ctk.CTkEntry(row_frame, width=80, font=("Arial", 14))
            entry_val.insert(0, f"{value:.2f}")
            entry_val.pack(side="left", padx=5)

            entry_val.bind("<Return>", lambda event, n=name, e=entry_val: self.update_value(n, e.get()))
            entry_val.bind("<KP_Enter>", lambda event, n=name, e=entry_val: self.update_value(n, e.get()))

        self.root.update_idletasks()
        
        total = self.db.get_patrimonio()
        self.lbl_total.configure(text=f"PATRIMÔNIO TOTAL: R$ {total:.2f}")

    def update_value(self, name, new_value_str):
        try:
            new_value = float(new_value_str.replace(",", "."))
            self.db.update_bank_value(name, new_value)
            self.root.focus()
            self.show_account()
        except ValueError:
            print(f"Erro ao atualizar {name}: Digite apenas números!")