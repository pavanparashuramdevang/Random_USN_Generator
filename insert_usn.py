import sqlite3

class StudentDb():
    def __init__(self):
        
        self.conn=sqlite3.connect('usn.db')
        self.c=self.conn.cursor()


    def insert(self,iterator):
        for val in iterator:
            try:
                self.c.execute("""INSERT INTO usn VALUES (?);""",(val,))

            except:
                print("value already exists")

            self.conn.commit()

        

    def retrive(self):
        self.c.execute("""SELECT * FROM usn""")
        my_list=self.c.fetchall()
        new_list=[]
        for elem in my_list:
            #print(elem)
            new_list.append(elem[0])

        self.conn.commit()
        if new_list:
            return new_list
        else:
            return None
    

    def delete(self,usn):
        try:
            self.c.execute("""DELETE FROM usn WHERE usn=(?);""",(usn,))
            #print("delete successfull")
            self.conn.commit()

        except:
            print("delete not possibe ")


    def close(self):
        self.conn.close()
        #print("connection is closed")

        





