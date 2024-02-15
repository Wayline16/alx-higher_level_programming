#!/urs/bin/python3
"""List all the states from the database hbtn_0e_o_usa"""

import MYSQLdb
from sys import argv

if __name__ == '__main__':
    
    # connection to the database
    db = MYSQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    
    # fetch all rows
    rows = cur.fetchall()
    
    # loop through each individual row
    for row in rows:
        print(row)

    # Clean up process 
    cur.close()
    db.close()  