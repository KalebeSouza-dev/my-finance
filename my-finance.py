import tkinter as tk

from db import FinanceDB
from app import FinanceAPP

def my_finance():
    financeDB = FinanceDB()

    root = tk.Tk()

    app = FinanceAPP(root, financeDB)

    root.mainloop()

    financeDB.connection.close()


if __name__ == '__main__':
    my_finance()