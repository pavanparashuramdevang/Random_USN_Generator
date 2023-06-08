import sqlite3

conn=sqlite3.connect('usn.db')

c=conn.cursor()

c.execute("""
CREATE TABLE usn
(usn TEXT PRIMARY KEY);
""")



c.execute("""
INSERT INTO usn VALUES ('4HG19CS028'),('4HG19CS029');
""")
c.execute("""
SELECT * FROM usn;
""")
usns=c.fetchall()

for usn in usns:
    print(usn[0])

conn.commit()
conn.close()