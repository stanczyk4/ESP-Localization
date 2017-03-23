import os.path
import sqlite3
import sys

class Database:
    def __init__(self, filepath):
        if(os.path.exists(filepath)):
            pass
        else:
            print("Database is Missing...")
            sys.exit()
        self.conn = sqlite3.connect(filepath)
        self.c = self.conn.cursor()

    def searchIDfromMACinSensor(self, MAC):
        self.c.execute('SELECT ID FROM sensor WHERE MAC=?',(MAC,))
        return self.c.fetchone()

    def closeDatabase(self):
        self.conn.close()


