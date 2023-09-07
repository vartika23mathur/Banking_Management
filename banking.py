import matplotlib.pyplot as plt

import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',password='student',db='SBI')
cursor=conn.cursor()

def New_Account():
    Accno=int(input("Enter account no "))
    customer_Name=input("Enter Customer Name ")
    Amount=float(input("Enter Amount "))
    
    query="Insert into customer values({},'{}','{}');".format(Accno,customer_Name,Amount)
    
    cursor.execute(query)
    conn.commit()
    print("Account Created Successfully")

    

def Deposit():
    Accno=int(input("Enter account no "))
    Amount=float(input("Enter Amount "))
    
    query="update customer set Amount=Amount+{} where accno={};".format(Amount,Accno)
    
    cursor.execute(query)
    conn.commit()
    print("Deposit  Successfully")


def Withdraw():
    Accno=int(input("Enter account no "))
    Amount=float(input("Enter Amount "))
    
    query="update customer set Amount=Amount-{} where accno={};".format(Amount,Accno)
    
    cursor.execute(query)
    conn.commit()
    print("Withdraw Successfully")


    


def Delete_Account():
    Accno=int(input("Enter account no "))
      
    query="Delete from customer where accno={};".format(Accno)
    
    cursor.execute(query)
    conn.commit()
    print("Account Deleted Successfully")
    

def Show_Detail():

    Accno=int(input("Enter Account number "))          
    query="select * from customer where accno={};".format(Accno)
    cursor.execute(query)
    data=cursor.fetchall()
    
    for i in data:
        print(i[1],i[2],i[0])

def Show_chart():
    name=[]
    amount=[]
    query="select * from customer"
    cursor.execute(query)
    data=cursor.fetchall()
    
    for i in data:
        name.append(i[1])
        amount.append(i[2])

    plt.bar(name,amount)
    plt.show()

    


# main Code


while True:
    print("1. For Create Account \n2. For Depost \n3. For withdraw\n4. For Show Detail \n5. Delete Account \n6. Graph \n7. Exit ")
    choice=int(input("Enter Your choice "))

    if choice ==1:
        New_Account()
        
    elif choice==2:
        Deposit()
        
    elif choice==3:
        Withdraw()
        
    elif choice==4:
        Show_Detail()
        
    elif choice==5:
        Delete_Account()
        
    elif choice==6:
        Show_chart()

    elif choice==7:
        break
        







