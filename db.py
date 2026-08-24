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
                name TEXT NOT NULL
            )
        ''')

        self.connection.commit()

    def get_balance(self):
        self.cursor.execute('SELECT SUM(value) FROM transactions')
        balance = self.cursor.fetchone()[0]

        if balance: return balance
        else: return 0.0

    def get_historic(self, limit=5):
        self.cursor.execute('SELECT * FROM transactions ORDER BY created_at DESC LIMIT (?)', (limit,))
        historic = self.cursor.fetchall()
        return historic

    def insert_transaction(self, value, description=""):
        self.cursor.execute('INSERT INTO transactions (value, description) VALUES (?,?)',(value, description))
        self.connection.commit()