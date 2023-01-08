import mysql.connector as c
con=c.connect(host='localhost',
              user='root',
              passwd='Saurabh@23',
              database='sbibank')

cursor= con.cursor()

#create a menu
#1. open account
#2. cash deposit
#3. cash withdrawl
#4. account details
#5. exit

while True:
    print('######## WELCOME TO BANK MANAGEMENT SYSTEM ########')

    choice=input("1.Open Account\n2.Cash Deposit\n3.Cash Withdrawl\n4.Account Details\n5.Exit")

    ##code for open account##

    if choice=="1":
        name=input('Enter the name')
        age=int(input('Enter the age'))
        contact=int(input('Enter the contact'))
        amount=int(input('Enter the amount'))

        query="Insert into customer values('{}',{},{},{})".format(name,age,contact,amount)
        cursor.execute(query)
        con.commit()

        print("Account Open Successfully")

    ##code for deposit amount##

    elif choice=='2':


        name=input("enter the name")
        accountnumber=int(input("enter the accountnumber"))
        depositamount=int(input("enter the depositamount"))
        totalamount=int(input("enter the totalamount"))

        query="Insert into customer values('{}',{},{},{})".format(name,accountnumber,depositamount,totalamount)
        cursor.execute(query)
        con.commit()

        print("Cash Deposit Successfully")

    ## code for cash withdrawl

    elif choice=='3':

        name=input("enter the name")
        accountnumber=int(input("enter the accountnumber"))
        withdrawlamount=int(input("enter the withdrawlamountamount"))
        totalamount=int(input("enter the totalamount"))


        query="Insert into customer values ('{}',{},{},{})".format(name,accountnumber,withdrawlamount,totalamount)
        cursor.execute(query)
        con.commit()
        print("Cash Withdrawl Successfully")

    ##account details##


    elif choice=='4':
        query='Select * from customer'
        cursor.execute(query)

        account_details=cursor.fetchall()
        print(account_details)
        con.commit()

    ##code for exit ##
    elif choice=='5':
        break;








