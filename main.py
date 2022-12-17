import sqlite3

con = sqlite3.connect('PhoneNumberBook.db')

cur = con.cursor()

# INSERT

def INSERT_NEW():
    Name = input('Please enter name: ')
    PhoneNumber = input('Please enter phone number: ')
    Age = input('Please enter age: ')
    Nationality = input('Please enter Nationality: ')
    Where = input('Please enter where to insert: ')
    cur.execute('INSERT INTO ' + Where + ' VALUES(?, ?, ?, ?);', (Nationality, Name, Age, PhoneNumber))
    con.commit()

# INSERT FROM OTHER TABLE
    
def INSERT_FROM_OTHER():
    Name = input('Please enter name of table to be inserted: ')
    where = input('Please enter where to SELECT: ')
    From = input('Please enter where to insert: ')
    Condition = input('Please enter the condition: ')
    cur.execute('INSERT INTO ' + Name + ' SELECT ' + where + ' FROM ' + From + ' WHERE ' + Condition + ';' )
    con.commit()
    
# SELECT 

def SELECT():
    where = input('Please enter where to SELECT: ')
    range = input('Please enter columns to sELECT\nex) Name, Age, PhoneNumber, Nationality  or * for everything: ')
    cur.execute('SELECT ' + range + ' FROM '+ where +';')
    for row in cur:
        print(row)
        
# SELECT DISTINCT

def SELECT_DISTINCT_byPhoneNumber():
    where = input('Please enter where to SELECT. PhoneNumber is default and other fields are your choice: ')
    table = input('Please enter which table to remove duplicated PhoneNumber: ')
    cur.execute('SELECT DISTINCT PhoneNumber, ' + where + ' FROM '+ table +';')
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
    nationality = input('Please enter which nationality you want to delete: ')
    where = input('Please enter which table to delete: ')
    cur.execute('DELETE FROM '+ where +' WHERE Nationality = \'' + nationality +'\';')
    con.commit()

# 나이로 DELETE
    
def DELETE_By_AGE():
    age = input('Please enter which age you want to delete: ')
    where = input('Please enter which table to delete: ')
    cur.execute('DELETE FROM '+ where +' WHERE PhoneNumber = \'' + age +'\';')
    con.commit()
    
# table을 clear

def DELETE_ALLINFO():
    where = input('Please enter which table to clear: ')
    cur.execute('DELETE FROM ' + where)
    con.commit()
    
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
    cur.execute('CREATE TABLE IF NOT EXISTS ' + Name +'(Nationality TEXT, Name TEXT, Age TEXT, PhoneNumber TEXT);')
    con.commit()
    
def DROP_TABLE():
    Name = input('Please enter table name to drop: ')
    cur.execute('DROP TABLE ' + Name +';')
    con.commit()
        
def CHECK_TABLE():
    cur.execute('SELECT * FROM sqlite_master;')
    for row in cur:
        print(row)
        
def CREATE_INDEX():
    Name = input('Please enter the name of index: ')
    Where = input('Please enter where to make index: ')
    Attribute = input('Please enter which attribute to be INDEX')
    cur.execute('CREATE INDEX ' + Name + ' on ' + Where + '(' + Attribute + ')')
    con.commit()
    
def SELECT_byINDEX():
    Where = input('Please enter where to see by INDEX: ')
    Attribute = input('Please enter which attribute you used to make INDEX: ')
    Value = input('Please enter which value you want to check: ')
    cur.execute('SELECT * FROM ' + Where + ' WHERE ' + Attribute + ' = \'' + Value + '\';')
    for row in cur:
        print(row)
        
def MAKE_VIEW():
    Name = input('Please enter name of View: ')
    res = input('Please enter what to show.\nex) (tablename1).(columnname1), (tablename2).(columnname2): ')
    table = input('Please enter table name to show. include what you wrote at tablename in advance: ')
    condition = input('Please enter condition: ')
    cur.execute('CREATE VIEW ' + Name + ' AS SELECT ' + res + ' FROM ' + table + ' WHERE ' + condition + ';')
    con.commit()

def SHOW_VIEW():
    Name = input('Please enter name of View: ')
    cur.execute('SELECT * FROM ' + Name + ';')
    for row in cur:
        print(row)

res = input('Please enter your response: ')

if res == 'insert':
    INSERT_NEW()
elif res == 'insertT':
    INSERT_FROM_OTHER()
elif res == 'select':
    SELECT()
elif res == 'selectD':
    SELECT_DISTINCT_byPhoneNumber()
elif res == 'deletebyName':
    DELETE_By_NAME()
elif res == 'deletebyNumber':
    DELETE_By_NUMBER()
elif res == 'deletebyNationallity':
    DELETE_By_NATIONALITY()
elif res == 'deletebyAge':
    DELETE_By_AGE()
elif res == 'deleteAll':
    DELETE_ALLINFO()
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
elif res == 'createIndex':
    CREATE_INDEX()
elif res == 'showbyIndex':
    SELECT_byINDEX()
elif res == 'inJoin':
    INNER_JOIN()
elif res == 'leftJoin':
    LEFT_OUTER_JOIN()
elif res == 'rightJoin':
    RIGHT_OUTER_JOIN()
elif res == 'fullJoin':
    FULL_OUTER_JOIN()

con.close()