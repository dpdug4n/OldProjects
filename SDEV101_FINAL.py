Pennies=list()
Nickels=list()
Dimes=list()
Quarters=list()
Ones=list()
Fives=list()
Tens=list()
Twenties=list()
Fifties=list()
Hundos=list()
ChecksTotal=list()
StoreTotal=list()
StoreDeposit=list()
GrandTotal=0
StrNum=1
def password():
   print "User must create a password for security purposes. Password must be 4-8 characters in length and contain at least one uppercase letter and a number."
   while True:
       Length=0
       UpperCase=0
       LowerCase=0
       Num=0
       PasswordTest= raw_input("Create password.\n")
       if 4 <= len(PasswordTest) <= 8:
           Length=1
       for x in PasswordTest:
           if x.isupper()==True:
               UpperCase=1
           elif x.islower()==True:
               LowerCase=1
           elif x.isalpha()==False:
               Num=1
       if Length<1:
           print "User Error. Password must be between 4 and 8 characters long."
       elif UpperCase<1:
           print "User Error. Password must contain an uppercase letter."
       elif LowerCase<1:
           print "User Error. Password must contain a lowercase letter."
       elif Num<1:
           print "User Error. Password must contain a number."
       else:
           print "Password has been created."
           break
   while True:
       Password= raw_input("Enter Password.\n")
       if Password!=PasswordTest:
           print "User Error. Incorrect Password."
       else: break
#program starts here
print "This will calculate total cash balance and deposit amount of stores collected from."
password()
while True:
   try:
       DrawerAmt=float(raw_input("Enter cash amount the drawers start the business day with.\n$"))
   except ValueError:
           print "User Error. Enter numerical value."
           continue
   break
while True:
   try:
       StrAmt=int(raw_input("Enter amount of stores collected from..."))
   except ValueError:
           print "User Error. Enter a whole number."
           continue
   else:
       Store=range(1,(StrAmt+1))
       for i in range(0, StrAmt):
           print "Store", StrNum, "drawer."
           #pennies
           while True:
               try:
                   amt=int(raw_input("Enter amount of pennies..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*.01
                   Pennies.append(amt)
               break
           #Nickels
           while True:
               try:
                   amt=int(raw_input("Enter amount of nickels..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*.05
                   Nickels.append(amt)
               break
           #Dimes
           while True:
               try:
                   amt=int(raw_input("Enter amount of dimes..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*.10
                   Dimes.append(amt)
               break
           #Quarters
           while True:
               try:
                   amt=int(raw_input("Enter amount of quarters..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*.25
                   Quarters.append(amt)
               break
           #Ones
           while True:
               try:
                   amt=int(raw_input("Enter amount of one dollar bills..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   Ones.append(amt)
               break
           #Fives
           while True:
               try:
                   amt=int(raw_input("Enter amount of five dollar bills..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*5
                   Fives.append(amt)
               break
           #Tens
           while True:
               try:
                   amt=int(raw_input("Enter amount of ten dollar bills..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*10
                   Tens.append(amt)
               break
           #Twenties
           while True:
               try:
                   amt=int(raw_input("Enter amount of twenty dollar bills..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*20
                   Twenties.append(amt)
               break
           #Fifties
           while True:
               try:
                   amt=int(raw_input("Enter amount of fifty dollar bills..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*50
                   Fifties.append(amt)
               break
           #Hundos
           while True:
               try:
                   amt=int(raw_input("Enter amount of hundred dollar bills..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   amt=amt*100
                   Hundos.append(amt)
               break
           #Checks
           Checks=list()
           while True:
               try:
                   CheckAmt=int(raw_input("Enter amount of checks recieved..."))
               except ValueError:
                       print "User Error. Enter a whole number."
                       continue
               else:
                   CheckCount=1
                   for y in range(0, CheckAmt):
                       while True:
                           try:
                               amt=float(raw_input("Enter amount of check#{}... $".format(CheckCount)))
                           except ValueError:
                                   print "User Error. Enter numerical value."
                                   continue
                           else:
                               Checks.append(amt)
                               CheckCount=CheckCount+1
                           break
                   ChecksTotal.append(sum(Checks))
                   break
           #StoreTotal
           StoreTotal.append(Pennies[i]+Nickels[i]+Dimes[i]+Quarters[i]+Ones[i]+Fives[i]
           +Tens[i]+Twenties[i]+Fifties[i]+Hundos[i]+ChecksTotal[i])
           StoreDeposit.append(StoreTotal[i]-DrawerAmt)
           #increaseStrNum
           StrNum=StrNum+1
   break
#results table
store='\t'.join(map(str, Store))
pennies='\t'.join(map(str, Pennies))
nickels='\t'.join(map(str, Nickels))
dimes='\t'.join(map(str, Dimes))
quarters='\t'.join(map(str, Quarters))
ones='\t'.join(map(str, Ones))
fives='\t'.join(map(str, Fives))
tens='\t'.join(map(str, Tens))
twenties='\t'.join(map(str, Twenties))
fifties='\t'.join(map(str, Fifties))
hundos='\t'.join(map(str, Hundos))
checks='\t'.join(map(str, ChecksTotal))
total='\t'.join(map(str, StoreTotal))
deposit='\t'.join(map(str, StoreDeposit))
print "Store Number\t {}" .format(store)
print "{:12}\t {}" .format('Total',total)
print "{:12}\t {}" .format('Deposit',deposit)
print "{:12}\t {}" .format('Hundreds',hundos)
print "{:12}\t {}" .format('Fifties',fifties)
print "{:12}\t {}" .format('Twenties',twenties)
print "{:12}\t {}" .format('Tens',tens)
print "{:12}\t {}" .format('Fives',fives)
print "{:12}\t {}" .format('Ones',ones)
print "{:12}\t {}" .format('Quarters',quarters)
print "{:12}\t {}" .format('Dimes',dimes)
print "{:12}\t {}" .format('Nickels',nickels)
print "{:12}\t {}" .format('Pennies',pennies)
print "{:12}\t {}" .format('Checks',checks)
print "Your total deposit is ${}." .format(sum(StoreDeposit))
