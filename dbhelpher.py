from itertools import count
from httplib2 import RETRIES
import mysql.connector as connector
class DBHelper:
    #Creating constractor
    def __init__(self):
        self.cnx=connector.connect(host='localhost',
                port='3306',
                user='root',
                password='root',
                database='pythonTest')
        query="""create table if not exists user(
                userId int primary key, 
                userName varchar(255), 
                phone varchar(12))"""
        cur=self.cnx.cursor()
        cur.execute(query)
        print("Created")

    #Insert
    def insert_user(self, userId, userName, phone):
       query="""insert into user(userId, userName, phone)
            values({},'{}','{}')""".format(userId, userName, phone)
       print(query)
       cur=self.cnx.cursor()    #curser method is come from connection
       cur.execute(query)
       self.cnx.commit()    #commit method come from connection
    #    print("User saved to db")
       return True
        
    #fetch all
    def fetch_all(self):
        query="select * from user"
        cur=self.cnx.cursor()
        cur.execute(query)

        for row in cur:
            # print(row)
            print("UserID :",row[0])
            print("UserName :",row[1])
            print("Phone :",row[2])
            print()
            print()
        return True

    #fetch one
    def fetch_one(self, userId):
        query="select * from user where userId={}".format(userId)
        cur=self.cnx.cursor()
        res=cur.execute(query)
        count=0
        print(cur)
        # print(res)
        for row in cur:
            count=1
            print("UserID :",row[0])
            print("UserName :",row[1])
            print("Phone :",row[2])
        print()
        print()
        if count ==0:
            return False
        return True

        # Delete user
    def delete_user(self, userId):
        
        query="delete from user where userId={}".format(userId)
        print(query)
        cur=self.cnx.cursor()
        
        cur.execute(query)
        affectd_rows=cur.rowcount
        self.cnx.commit()
        # print("Deleted")

        if affectd_rows==0:
            return False
        
        return True

    # update
    def update_user(self, userId, newName, newPhone):
        query="update user set userName='{}', phone='{}' where userId={}".format(newName, newPhone, userId)
        print(query)
        cur=self.cnx.cursor()
        cur.execute(query)
        affectd_rows=cur.rowcount
        
        self.cnx.commit()
        # print("Updated")
        # Check data exist or not
        if affectd_rows==0:
            return False
        
        return True
