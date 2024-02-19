#!/urs/bin/python3
"""List all the states from the database hbtn_0e_o_usa"""

import MYSQLdb
from sys import argv

if __name__ == '__main__':
    
    # connection to the database
    db = MYSQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name,\
                FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])
    
    # fetch all rows
    rows = cur.fetchall()
    list = []
    # loop through each individual row
    for row in rows:
        list.append(row[1])
        print(", ".join(list))

    # Clean up process 
    cur.close()
    db.close()  