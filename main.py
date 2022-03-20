from dbhelpher import DBHelper
#main coding
def main():
    
    # creating object

    db=DBHelper()

    while True:
        print("*********WELCOME*********")
        print()
        print("Press 1 to insert new user ")
        print("Press 2 to display all user ")
        print("Press 3 to display single user information ")
        print("Press 4 to delete user ")
        print("Press 5 to update user ")
        print("Press 6 to exit ")
        print()

        try:
            choice=int(input("Enter Your Choice: "))
            
            if(choice==1):
                #insert user
                try:
                    userId=int(input("Enter userId : "))                
                    userName=input("Enter userName : ")                
                    userPhone=input("Enter userPhone : ")                
                    db.insert_user(userId, userName, userPhone)
                
                except Exception as e:
                    print(e)

            elif(choice==2):
                #display all user
                try:
                    db.fetch_all()
                except Exception as e:
                    print(e)

            elif(choice==3):
                # display single user
                try:
                    userId=int(input("Enter userId to fetch information: "))                
                    if(db.fetch_one(userId))==True:
                        pass
                    else:
                        print("Invalid userId")
                        print()
                except Exception as e:
                    print(e)
            
            elif(choice==4):
                # delete user
                try:
                    userId=int(input("Enter userId to which you want to delete: "))                
                    if (db.delete_user(userId))==True:
                       print("{} userId deleted".format(userId))

                    else:
                        print("Invalid userId")

                except Exception as e:
                    print(e)

                
            elif(choice==5):
                # update user

                try:
                    userId=int(input("Enter userId to which you want to update: "))                
                    if(db.fetch_one(userId)==True):
                        newUserName=input("Enter userName : ")                
                        newUserPhone=input("Enter userPhone : ")
                        
                        if(db.update_user(userId, newUserName, newUserPhone)==True):
                            print("User saved to db")
                        else:
                            print("Unable to save")
                            print()
                    else:
                            print("Invalid userId")
                            print()

                except Exception as e:
                    print(e)

            elif(choice==6):
                break
            
            else:
                print("invalid input try again")

        except Exception as e:
            print(e)
            print("Invalid Details ! Try again")

if __name__=='__main__':
    main()





# helpher=DBHelper()
# helpher.insert_user(1437,"Anup","7001496091")
# helpher.insert_user(1445,"Rick","7001496091")
# helpher.insert_user(1448,"Ankita","7001496091")
# helpher.insert_user(1436,"Manorma","7001496091")
# helpher.fetch_all()
# helpher.fetch_one(1437)
# helpher.delete_user(1437)
# helpher.fetch_all()
# helpher.update_user(1445, "Ankita", "700148146")
# helpher.fetch_all()