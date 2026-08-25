import tkinter as tk 
import customtkinter as ctk

from views.finance_app import FinanceAPP
from views.bank_app import BankAPP

class App:
    def __init__(self, root, db):
        self.root = root 
        self.db = db 

        root.title("MY FINANCE") 
        root.geometry("200x100")
        root.resizable(False, False)

        self.btn_add = ctk.CTkButton(root, text="Finance", width=175, command=self.open_finance) 
        self.btn_add.pack(pady=15) 

        self.btn_add = ctk.CTkButton(root, text="Bank", width=175, command=self.open_bank) 
        self.btn_add.pack(pady=5) 

    def open_finance(self):
        finance_window = ctk.CTkToplevel(self.root)
        FinanceAPP(finance_window, self.db)
        finance_window.focus()

    def open_bank(self):
        bank_window = ctk.CTkToplevel(self.root)
        BankAPP(bank_window, self.db)
        bank_window.focus()