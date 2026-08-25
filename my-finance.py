import customtkinter as ctk

from db import FinanceDB
from views.finance_app import FinanceAPP
from views.bank_app import BankAPP

def my_finance():
    financeDB = FinanceDB()

    root = ctk.CTk()

    finance_app = ctk.CTkToplevel(root)
    financeapp = FinanceAPP(finance_app, financeDB)

    bank_root = ctk.CTkToplevel(root)
    bankapp = BankAPP(bank_root, financeDB)

    root.mainloop()

    financeDB.connection.close()


if __name__ == '__main__':
    my_finance()