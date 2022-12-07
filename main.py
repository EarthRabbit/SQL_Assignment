import sqlite3

con = sqlite3.connect('PhoneNumberBook.db')

cur = con.cursor()

# INSERT

def INSERT():
    Name = input('Please enter name: ')
    PhoneNumber = input('Please enter phone number: ')
    Age = input('Please enter age: ')
    Nationality = input('Please enter Nationality: ')
    Where = input('Please enter where to insert: ')
    cur.execute('INSERT INTO ' + Where + ' VALUES(?, ?, ?, ?);', (Nationality, Name, Age, PhoneNumber))
    con.commit()

# SELECT 

def SELECT():
    where = input('Please enter where to sELECT: ')
    range = input('Please enter columns to sELECT\nex) Name, Age, PhoneNumber, Nationality  or * for everything: ')
    cur.execute('SELECT ' + range + ' FROM '+ where +';')
    for row in cur:
        print(row)

# 이름으로 DELETE

def DELETE_By_NAME():
    name = input('Please enter who you want to delete: ')
    where = input('Please enter which table to delete: ')
    cur.execute('DELETE FROM ' + where + ' WHERE Name = ' + name + ';')
    con.commit()
    
# 전화번호로 DELETE
    
def DELETE_By_NUMBER():
    number = input('Please enter which phone number you want to delete: ')
    where = input('Please enter which table to delete: ')
    cur.execute('DELETE FROM '+ where +' WHERE PhoneNumber = \'' + number +'\';')
    con.commit()
    
# 국적으로 DELETE

def DELETE_By_NATIONALITY():
    number = input('Please enter which nationality you want to delete: ')
    where = input('Please enter which table to delete: ')
    cur.execute('DELETE FROM '+ where +' WHERE PhoneNumber = \'' + number +'\';')
    con.commit()

# 나이로 DELETE
    
def DELETE_By_AGE():
    age = input('Please enter which age you want to delete: ')
    where = input('Please enter which table to delete: ')
    cur.execute('DELETE FROM '+ where +' WHERE PhoneNumber = \'' + number +'\';')
    con.commit()
    
# table을 clear

def DELETE_ALLINFO():
    where = input('Please enter which table to clear: ')
    cur.execute('DELETE FROM ' + where)
    
# INNER JOIN
    
def INNER_JOIN():
    colname = input('Please enter column names to use.(* for every column): ')
    table1 = input('Please enter name of table for from: ')
    table2 = input('Please enter name of table for join: ')
    condition = input('Please enter condition for on: ')
    cur.execute('SELECT ' + colname + ' FROM ' + table1 + ' INNER JOIN ' + table2 + ' ON '+ condition+ ';')
    for row in cur:
        print(row)

# LEFT OUTER JOIN

def LEFT_OUTER_JOIN():
    colname = input('Please enter column names to use.(* for every column): ')
    table1 = input('Please enter name of table for from: ')
    table2 = input('Please enter name of table for join: ')
    condition = input('Please enter condition for on: ')
    cur.execute('SELECT ' + colname + ' FROM ' + table1 + ' LEFT OUTER JOIN ' + table2 + ' ON '+ condition+ ';')
    for row in cur:
        print(row)

# RIGHT OUTER JOIN
# SQLite는 RIGHT OUTER JOIN을 지원하지 않기에 LEFT를 활용했다.

def RIGHT_OUTER_JOIN():
    colname = input('Please enter column names to use.(* for every column): ')
    table1 = input('Please enter name of table for from: ')
    table2 = input('Please enter name of table for join: ')
    condition = input('Please enter condition for on: ')
    cur.execute('SELECT ' + colname + ' FROM ' + table2 + ' LEFT OUTER JOIN ' + table1 + ' ON '+ condition+ ';')
    for row in cur:
        print(row)
        
# FULL OUTER JOIN
# SQLite는 FULL OUTER JOIN을 지원하지 않는다.

def FULL_OUTER_JOIN():
    colname = input('Please enter column names to use.(* for every column): ')
    table1 = input('Please enter name of table for from: ')
    table2 = input('Please enter name of table for join: ')
    condition = input('Please enter condition for on: ')
    cur.execute('SELECT ' + colname + ' FROM ' + table1 + ' LEFT OUTER JOIN ' + table2 + ' ON '+ condition + ' UNION ALL ' + 'SELECT ' + colname + ' FROM ' + table2 + ' LEFT OUTER JOIN ' + table1 + ' ON '+ condition + ' EXCEPT ' + 'SELECT ' + colname + ' FROM ' + table1 + ' INNER JOIN ' + table2 + ' ON '+ condition+ ';')
    for row in cur:
        print(row)

def MAKE_NEW_TABLE():
    Name = input('Please enter table name: ')
    cur.execute('CREATE TABLE IF NOT EXISTS ' + Name +'(Nationality TEXT, Name TEXT, Age INT, PhoneNumber TEXT);')
    
def DROP_TABLE():
    Name = input('Please enter table name to drop: ')
    cur.execute('DROP TABLE ' + Name +';')
        
def CHECK_TABLE():
    cur.execute('SELECT * FROM sqlite_master;')
    for row in cur:
        print(row)
        
def MAKE_VIEW():
    Name = input('Please enter name of View: ')
    res = input('Please enter what to show.\nex) (tablename1).(columnname1), (tablename2).(columnname2): ')
    table = input('Please enter table name to show. include what you wrote at tablename in advance: ')
    condition = input('Please enter condition: ')
    cur.execute('CREATE VIEW ' + Name + ' AS SELECT ' + res + ' FROM ' + table + ' WHERE ' + condition + ';')

def SHOW_VIEW():
    Name = input('Please enter name of View: ')
    cur.execute('SELECT * FROM ' + Name + ';')
    for row in cur:
        print(row)

res = input('Please enter your response: ')

if res == 'insert':
    INSERT()
elif res == 'sELECT':
    SELECT()
elif res == 'deletebyName':
    DELETE_By_NAME()
elif res == 'deletebyNumber':
    DELETE_By_NUMBER()
elif res == 'newTable':
    MAKE_NEW_TABLE()
elif res == 'drop':
    DROP_TABLE()
elif res == 'tableInfo':
    CHECK_TABLE()
elif res == 'createView':
    MAKE_VIEW()
elif res == 'showView':
    SHOW_VIEW()
elif res == 'inJoin':
    INNER_JOIN()
elif res == 'leftJoin':
    LEFT_OUTER_JOIN()
elif res == 'rightJoin':
    RIGHT_OUTER_JOIN()
elif res == 'fullJoin':
    FULL_OUTER_JOIN()

con.close()