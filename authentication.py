import jwt
import sqlite3
conn = sqlite3.connect('to_do_list.db')

cursor=conn.cursor()
def jwt_authentication(name,password):
    header={
        "alg": "HS256",  
        "typ": "JWT" 
    }
    """ = input("enter your name please: ")
     = input("your password: ")"""
    payload={
        "name":name,
        "password":password
    }
    secret="manasa"
    encoded_jwt=jwt.encode(payload, secret, algorithm='HS256', headers=header)  
    print(encoded_jwt)
    sign_up=("insert into auth_db(token,user_name) values (?,?);")
    cursor.execute(sign_up,(encoded_jwt,name,))
    
    decoded_jwt=jwt.decode(encoded_jwt, secret, algorithms=['HS256'])  
    print(decoded_jwt) 
def sign_in(name,password):
    header={
        "alg": "HS256",  
        "typ": "JWT" 
    }
    
    payload={
        "name":name,
        "password":password
    }
    secret="manasa"
    encoded_jwt=jwt.encode(payload, secret, algorithm='HS256', headers=header)  
    print(encoded_jwt)
    sign=("select * from auth_db where user_name=(?);" )
    data=cursor.execute(sign,(name,))
    for i in data:
        print('in data')
        print(i)
    if data== None:
        print("invalid data\n")
    decoded=jwt.decode(encoded_jwt, secret, algorithms=['HS256'],verify=True)
    print(decoded)

    print("if you want to get your task details please press 1")
    t=int(input())
    if t==1:
        script=("select * from to_do where user_name=(?);")
        k=cursor.execute(script,(name,))
        for i in k:
            print(i)
    else:
        print("!!!!!---------GOOD BYE-----------!!!!!!")
        exit
def get_all():
    
    data=cursor.execute('select * from auth_db')
    for i in data:
        print(i)

"""table='create table auth_db(token varchar(300),user_name varchar(100), primary key(user_name))'
cursor.execute(table)
"""

 
if __name__ == '__main__':
    while 1:
        print("press\n 1 for sign in \n 2 for sign up")
        k=int(input())
        if k==1:
            name = input("enter your name please:\n ")
            password = input("your password:\n ")
            sign_in(name,password)
            
        
        elif k==2:
            name = input("enter your name please:\n ")
            password = input("your password:\n ")
            jwt_authentication(name,password)
        elif k==3:
            get_all()
        else:
            print("wrong input please try again\n")
            break
conn.commit()
conn.close()