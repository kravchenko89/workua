import sqlite3


def save_db(work_path, vacancy, wage, company, address, description):
    con = sqlite3.connect('Workua_Jobs.db')
    c = con.cursor()
    c.execute('''INSERT INTO Workua_Jobs VALUES (?, ?, ?, ?, ?, ?)''',
              (work_path, vacancy,
               wage, company, address,
               description))
    con.commit()
    con.close()


def create_db(work_path, vacancy, wage, company, address, description):
    con = sqlite3.connect('Workua_Jobs.db')
    c = con.cursor()
    # Create table - CLIENTS
    c.execute('''CREATE TABLE Workua_Jobs
                     (work_path, vacancy,
    wage, company, address, description)''')
    con.commit()
