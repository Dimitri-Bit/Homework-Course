import sqlite3, datetime
from pyargon2 import hash

DATABASE = 'db.db'
SALT = "dwaaaaawdaww"

class database_manager:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE)
        self.cursor = self.connection.cursor()
        self.init_tables()

    def init_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (ID INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, email TEXT, password TEXT, image_path TEXT, time TEXT)")
        self.connection.commit()

    def register_user(self, username, email, password, image_path):
        if not self.get_user(email):
            password = self.hash_password(password)
            query = f"INSERT INTO users VALUES (NULL, '{username}', '{email}', '{password}', '{image_path}', '{self.get_current_time()}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        else:
            return False

    def get_user(self, email):
        query = f"SELECT * from users where email = '{email}'"
        rows = self.cursor.execute(query).fetchall()
        return rows
        
    def login_user(self, email, password):
        user = self.get_user(email)

        if user:          
            if self.verify_password(user[0][3], password):
                return "Correct Password"
            else:
                return "Incorrect Password"
        else:
            return "User does not exist"

    def get_current_time(self):
        return datetime.datetime.now()
    
    def hash_password(self, password):
        hashed_password = hash(password, SALT)
        return hashed_password
    
    def verify_password(self, hashed_password, password):
        hashed_password_2 = self.hash_password(password)
        return hashed_password == hashed_password_2

    def print_database(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

database_m = database_manager()
