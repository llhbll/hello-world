import sqlite3

con = sqlite3.connect('./test.db')
cur = con.cursor()
#cur.execute('CREATE TABLE PhoneBook(Name text, PhoneNum text);')
cur.execute('INSERT INTO PhoneBook VALUES("Lim ChanHyuk", "010-8443-8473");')
cur.execute('SELECT * FROM PhoneBook;')
con.commit()

print(cur.fetchall())