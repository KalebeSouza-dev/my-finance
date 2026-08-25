import sqlite3

class FinanceDB:

    def __init__(self):
        self.connection = sqlite3.connect("finance.db")
        self.cursor = self.connection.cursor()

        self.create_tables() 


    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                value REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                bank_id INTEGER,
                description TEXT,

                FOREIGN KEY (bank_id) REFERENCES banks (bank_id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS banks(
                bank_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                value REAL DEFAULT 0.0
            )
        ''')

        self.connection.commit()


    # transactions
    def get_balance(self):
        self.cursor.execute('SELECT SUM(value) FROM transactions')
        balance = self.cursor.fetchone()[0]

        if balance: return balance
        else: return 0.0

    def get_historic(self, limit=10):
        self.cursor.execute('SELECT * FROM transactions ORDER BY created_at DESC LIMIT (?)', (limit,))
        historic = self.cursor.fetchall()
        return historic

    def insert_transaction(self, value, description=""):
        self.cursor.execute('INSERT INTO transactions (value, description) VALUES (?,?)',(value, description))
        self.connection.commit()


    # banks
    def insert_bank(self, name):
        self.cursor.execute('INSERT INTO banks (name) VALUES (?)', (name,))
        self.connection.commit()

    def get_banks(self):
        self.cursor.execute('SELECT * FROM banks')
        banks = self.cursor.fetchall()
        return banks

    def get_patrimonio(self):
            self.cursor.execute('SELECT SUM(value) FROM banks')
            patrimonio = self.cursor.fetchone()[0]
    
            if patrimonio: return patrimonio
            else: return 0.0

    def update_bank_value(self, name, value):
        self.cursor.execute('''
            UPDATE banks 
            SET value = ?
            WHERE name = ?
        ''', (value, name))
        self.connection.commit()
