import datetime
import random
import mysql.connector

name =[]
phno =[]
seat=[] 
price=[]


print("\t\t\t INFINITY ARENA KUNNAMKULAM\n")
now=datetime.datetime.now()
print(now)
mydb=mysql.connector.connect(host="localhost",user="root",passwd="buck",database="sys")
mycursor=mydb.cursor()
def home():
    print("1.Ticket booking\n")
    print("2.Match Fixtures\n")
    print("3.Food menu\n")
    print("4.Payment\n")
    print("5.Show details\n")
    print("6.Cancel ticket\n")
    print("7.exit\n")
    ch1=int(input("--->"))



#Ticket booking
    if ch1==1:
        print("Barcelona vs Real Madrid\n")
        print("Bayern Munich vs PSG\n")
        print("Juventus vs Manchester United\n")
        global ch3
        ch3=int(input("--->"))
        if ch3==1:
            booking()
        elif ch3==2:
            booking()
        elif ch3==3:
            booking()
            
            
#match fixtures            
    elif ch1==2:
        print("Barcelona vs Real Madrid\n")
        print("Bayern Munich vs PSG\n")
        print("Juventus vs Manchester United\n")
        v=int(input("press 0 to go back"))
        if v==0:
            home()


#food menu
    elif ch1==3:
        food()

#payment
    elif ch1==4:
        payment()

#cancellation
    elif ch1==5:
        details()

#details
    elif ch1==6:
        cancel()



#function for booking      
def booking():
    a=str(input("Enter name:"))
    b=str(input("Enter phone no."))
    name.append(a)
    phno.append(b)
    print("------SELECT SEAT TYPE------")
    print("1.VIP seat - Rs.2000")
    print("2.Upper area - Rs.1400")
    print("3.Middle area - Rs.1000")
    print("4.Lower area - Rs.600")
    ch2=int(input("--->"))


#VIP seat
    if ch2==1: 
        print("VIP seat")
        print("price:Rs.2000")
        l=int(input("Enter no:of seats:"))
        price.append(l*2000)
        print("\t\t\t----SEAT BOOKED SUCCESSFULLY----\n")
        m=random.randint(1,20)
        print("seat no:V",m)
        seat.append(m)
        for i in range(1,l):
            m=m+1
            print("seat no:V",m)
            seat.append(m)
        if ch3==1:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Barcelona vs Real Madrid","VIP seat")""",(a,b,))
            mydb.commit()
        elif ch3==2:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Bayern Munich vs PSG","VIP seat")""",(a,b,))
            mydb.commit()
        elif ch3==3:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Juventus vs Manchester United","VIP seat")""",(a,b,))
            mydb.commit()
        p=int(input("press 0 to go back"))
        if p==0:
            home()
#Upper area
    elif ch2==2:
        print("Upper area seat")
        print("price:Rs.1400")
        l=int(input("Enter no:of seats:"))
        price.append(l*1400)
        print("\t\t\t----SEAT BOOKED SUCCESSFULLY----\n")
        m=random.randint(1,100)
        print("seat no:U",m)
        seat.append(m)
        if ch3==1:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Barcelona vs Real Madrid","Upper area")""",(a,b,))
            mydb.commit()
        elif ch3==2:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Bayern Munich vs PSG","Upper area")""",(a,b,))
            mydb.commit()
        elif ch3==3:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Juventus vs Manchester United","Upper area")""",(a,b,))
            mydb.commit()
        for i in range(1,l):
            m=m+1
            print("seat no:U",m)
            seat.append(m)
        n=int(input("press 0 to go back"))
        if n==0:
            home()


#Middle area
    elif ch2==3:
        print("Middle area seat")
        print("price:Rs.1000")
        l=int(input("Enter no:of seats:"))
        price.append(l*1000)
        print("\t\t\t----SEAT BOOKED SUCCESSFULLY----\n")
        m=random.randint(1,100)
        print("seat no:M",m)
        seat.append(m)
        if ch3==1:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Barcelona vs Real Madrid","Middle area")""",(a,b,))
            mydb.commit()
        elif ch3==2:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Bayern Munich vs PSG","Middle area")""",(a,b,))
            mydb.commit()
        elif ch3==3:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Juventus vs Manchester United","Middle area")""",(a,b,))
            mydb.commit()
        for i in range(1,l):
            m=m+1
            print("seat no:M",m)
            seat.append(m)
        n=int(input("press 0 to go back"))
        if n==0:
            home()
#Lower area
    elif ch2==4:
        print("Lower area seat")
        print("price:Rs.600")
        l=int(input("Enter no:of seats:"))
        price.append(l*600)
        print("\t\t\t----SEAT BOOKED SUCCESSFULLY----\n")
        m=random.randint(1,100)
        print("seat no:L",m)
        seat.append(m)
        if ch3==1:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Barcelona vs Real Madrid","Lower area")""",(a,b,))
            mydb.commit()
        elif ch3==2:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Bayern Munich vs PSG","Lower area")""",(a,b,))
            mydb.commit()
        elif ch3==3:
            mycursor=mydb.cursor()
            mycursor.execute("""insert into infinity(name,phone_no,fixture,seat_type) values(%s,%s,"Juventus vs Manchester United","Lower area")""",(a,b,))
            mydb.commit()
        for i in range(1,l):
            m=m+1
            print("seat no:L",m)
            seat.append(m)
        n=int(input("press 0 to go back"))
        if n==0:
            home()


    else:
        print("Wrong choice......")
        n=int(input("press 0 to go back"))
        if n==0:
            home()

#function for food menu
def food():
    if name==[]:
        print("------Book ticket first-------")
        n=int(input("press 0 to go back"))
        if n==0:
            home()

    else:
        
        print("1.Lays-------------Rs.20")
        print("2.Chicken puffs----Rs.25")
        print("3.Burger-----------Rs.35")
        print("4.Popcorn----------Rs.20")
        print("5.Soft drinks------Rs.25")
        ch4=int(input("--->"))
        r=0
        if ch4==1:
            print("Lays ordered")
            r=r+20
            price.append(r)
            t=int(input("press 0 to go back"))
            if t==0:
                home()
        elif ch4==2:
            print("Chicken puffs ordered")
            r=r+25
            price.append(r)
            a=int(input("press 0 to go back"))
            if a==0:
                home()
        elif ch4==3:
            print("Burger ordered")
            r=r+35
            price.append(r)
            b=int(input("press 0 to go back"))
            if b==0:
                home()
        elif ch4==4:
            print("Popcorn ordered")
            r=r+20
            price.append(r)
            c=int(input("press 0 to go back"))
            if c==0:
                home()
        elif ch4==5:
            print("Soft drink ordered")
            r=r+25
            price.append(r)
            d=int(input("press 0 to go back"))
            if d==0:
                home()


#function for payment
def payment():
    if price==[]:
        print("Book a seat first")
        g=int(input("press 0 to go back"))
        if g==0:
            home()
    else:
        print("Payment by credit/debit card")
        print("Total amount to be paid:",sum(price))
        h=int(input("enter credit/debit card number:"))
        p=input("press y to confirm payment:")
        if p=="y":
            print("\t\t\t ----PAYMENT SUCCESSFULL----\n")
            print("Tickets holder name:",str(name[0]))
            print("Phone Number:",str(phno[0]))
            n=int(input("press 0 to go back:"))
            if n==0:
                home()
        else:
            print("\t\t\t ----PAYMENT UNSUCCESSFULL----\n")
            n=int(input("press 0 to go back:"))
            if n==0:
                home()


#function for cancelling ticket
def cancel():
    if phno==[]:
        print("No tickets booked")
        n=int(input("press 0 to go back"))
        if n==0:
            home()
    else:
        m=str(input("Enter ticket holder's phone number:"))
        if m in phno:
            o=str(input("Press y to confirm ticket cancellation:"))
            if o=="y":
                print("\t\t\t ----TICKET CANCELLED----\n")
                name.pop(0)
                price.pop()
                mycursor=mydb.cursor()
                mycursor.execute("""delete from infinity where name=%s""",(m,))
                mydb.commit()
            else:
                print("\t\t\t ----TICKET NOT CANCELLED----\n")
        else:
            print("Ticket not found")
            n=int(input("press 0 to go back:"))
            if n==0:
                home()
            
    
            
            
#function for details
def details():
    mycursor.execute("select * from infinity")
    for x in mycursor:
        print(x)
    n=int(input("press 0 to go back:"))
    if n==0:
        home()

home()



        
    
    



    



        


        
        
        
        

    
        
