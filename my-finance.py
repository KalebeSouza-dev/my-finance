import customtkinter as ctk

from db import FinanceDB
from views.app import App
from views.finance_app import FinanceAPP
from views.bank_app import BankAPP

def my_finance():
    financeDB = FinanceDB()

    root = ctk.CTk()
    app = App(root, financeDB)

    root.mainloop()

    financeDB.connection.close()


if __name__ == '__main__':
    my_finance()