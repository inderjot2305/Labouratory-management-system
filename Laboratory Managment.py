print("""
        *************************************
        Welcome to Laboratory Management System
        *************************************
""")

import mysql.connector as ms
pd=str(input("Enter Database Password:"))

cn=ms.connect(host="localhost",user="root",password="123456",database="laboratory")
cur=cn.cursor()
'''
#creating database for Laboratory
cur.execute("create database Laboratory")
cur.execute("use Laboratory")
cur.execute("create table  bacteria\
                 (SAmple_no int(10) primary key,\
                 Sample_name varchar(30) not null,\
                 type varchar(10),\
                 disease varchar(30),\
                 media varchar(50),\
                 category varchar(30))")
cur.execute("create table  virus\
                (SAmple_no int(10) primary key,\
                 Sample_name varchar(30) not null,\
                 type varchar(10),\
                 disease varchar(30),\
                 media varchar(50),\
                 category varchar(30))")
cur.execute("create table  prozona\
                (SAmple_no int(10) primary key,\
                 Sample_name varchar(30) not null,\
                 type varchar(10),\
                 disease varchar(30),\
                 media varchar(50),\
                 category varchar(30))")
cur.execute("create table users\
                 (username varchar(30) primary key,\
                  password varchar(30) default'000')")'''
2
def sign_up():
    print("""
            ********************************************
            !!!!!!!Please enter new user details!!!!!!!!
            ********************************************
                                                """)

    u=input("Enter New User Name!!:")
    p=input("Enter password (Combination of Letters, Digits etc.):")
    cur.execute("insert into users values('"+u+"','"+p+"')")
    cn.commit()
    print("""
        *******************************************************
        !!!!!!!!Congratulations!!!, New User Created...!!!!!!!!
        *******************************************************
                                            """)

def login():

            print("""
                **********************************************************
                !!!!!!!!  {{Loginwith username and password }}  !!!!!!!!!!
                **********************************************************
                                                    """)

            un=input("Username!!:")
            ps=input("Password!!:")
            pid=0
            cur.execute("select password from users where username='"+un+"'")
            rec=cur.fetchall()
            for i in rec:
                a=list(i)
                if a[0]==str(ps):
                    while(True):
                        print("""
                            1.bacteria
                            2.virus
                            3.Prozona(Add yourself)
                            4.Sign Out
                                                        """)

                        a=int(input("Enter your choice:"))
                        if a==1:
                            print("""
                                1. Show Details
                                2. Add new Sample
                                3. Delete existing sample
                                4. Exit
                                                     """)
                            b=int(input("Eter your choice:"))
                            if b==1:
                                cur.execute("select * from bacteria")
                                rec=cur.fetchall()
                                for i in rec:
                                    b=0
                                    v=list(i)
                                    k=["SAMPLE_NO","SAMPLE_NAME","TYPE","DECIESE","MEDIA","CATEGORY"]
                                    d=dict(zip(k,v))
                                    print("")
                                    for i in d:
                                        print(i,":",d[i])
                                    print()
                                
                            elif b==2:
                                S_No=input("Enter Sample no :")
                                S_name=input("Enter Sample_name:")
                                S_type=input("Enter type:")
                                Deciese=input("Enter deciese:")
                                Media=input("Enter Media:")
                                category=input("Enter category:")
                                cur.execute("insert into bacteria values("+S_No+",'"+S_name+"','"+S_type+"','"+Deciese+"','"+Media+"','"+category+"')")
                                cn.commit()
                                print("New bacteria details has been added successfully. ")

                            elif b==3:
                                name=input("Enter bacteria name to delete:")
                                cur.execute("select * from bacteria where name=",name)
                                rec=cur.fetchall()
                                print(rec)
                                p=input("you really wanna delete this data? (y/n):")
                                if p=="y":
                                    cur.execute("delete from bacteria where name=","+name+")
                                    cn.commit()
                                    print("bacteria has been deleted successfully")
                                else:
                                    print("Error in deletion....")
                                   
                            elif b==4:
                                print("Thank you! See you again! Have nice Day!")
                                break
                        # virus
                        if a==2:
                            print("""
                                1. Show Details
                                2. Add new Sample
                                3. Delete existing sample
                                4. Exit
                                                         """)
                            b=int(input("Eter your choice:"))
                            if b==1:
                                cur.execute("select * from virus")
                                rec=cur.fetchall()
                                for i in rec:
                                    b=0
                                    v=list(i)
                                    k=["SAMPLE_NO","SAMPLE_NAME","TYPE","DECIESE","MEDIA","CATEGORY"]
                                    d=dict(zip(k,v))
                                    print("")
                                    for i in d:
                                        print(i,":",d[i])
                                    print()   
                            elif b==2:  
                                S_No=input("Enter Sample no :")
                                S_name=input("Enter Sample_name:")
                                S_type=input("Enter type:")
                                Deciese=input("Enter deciese:")
                                Media=input("Enter Media:")
                                category=input("Enter category:")
                                cur.execute("insert into virus values("+S_No+",'"+S_name+"','"+S_type+"','"+Deciese+"','"+Media+"','"+category+"')")
                                cn.commit()
                                print("New virus details has been added successfully. ")

                            elif b==3:
                                name=input("Enter virus name to delete:")
                                cur.execute("select * from virus where name='"+name+"'")
                                rec=cur.fetchall()
                                print(rec)
                                p=input("you really wanna delete this data? (y/n):")
                                if p=="y":
                                    cur.execute("delete from virus where name='"+name+"'")
                                    cn.commit()
                                    print("virus has been deleted successfully")
                                else:
                                    print("Error in deletion....")
                                   
                            elif b==4:
                                print("Thank you! See you again! Have nice Day!")
                                break
                        elif a==4:
                            break
def change_pass():
    cur.execute("select username from users")
    rec=cur.fetchall()
    for i in rec:
        v=list(i)
        k=["USERNAME"]
        d=dict(zip(k,v))
    print(d)
    u=input("Enter username to change password from above:")
    if u in d.values():
        pd=input("Enter New Password:")
        pd1=input("Renter New Password again:")
        if pd==pd1:
          cur.execute("update users set password='"+pd+"'where username='"+u+"'")
          cn.commit()
          print("Password Changed Successfully.")
        else:
          print("Password did not match...")
    else:
        print("Username not found")
r=0
while r!=4:
    print("""
                    1. Sign Up (New User)
                    2. Log In
                    3. Change Password
                    4. Exit
                                                        """)

    r=int(input("Enter your choice:"))    
    if r==1:
        sign_up()
    elif r==2:
        login()                 
    elif r==3:
        change_pass()
    elif r==4:
      print("Thank you , Have a nice day!")
      break

