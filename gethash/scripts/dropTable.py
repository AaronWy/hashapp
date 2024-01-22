import csv 
from io import StringIO
import sqlite3 

conn = sqlite3.connect("/home/aaron/Projects/hashapp/db.sqlite3")
cursor = conn.cursor()
cursor.execute('''
            DROP TABLE gethash_hashcatmode;
        ''')
conn.commit()
conn.close()
