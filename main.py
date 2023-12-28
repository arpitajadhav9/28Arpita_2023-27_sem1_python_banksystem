#import bank_package.base

print("__________________________Welcome To Bank System_________________________")

print("PLEASE CHOOSE OPTIONS AS PER YOUR CHOICE!!!")
print("SELECT 1 FOR ACCOUNT DIPOSITE")
print("SELECT 2 FOR WITHDRWAL")
print("SELECT 3 FOR ACCOUNT CREATION")
print("SELECT 4 FOR LOAN APPLICATION")
print("SELECT 5 FOR KYC APPLICATION")

opt=int(input("Enter Your Choice:"))
if opt==1:
 from bank_package.base import Bank

 customer_name = input("Enter your name: ")
 bank_account = Bank(customer_name)    
 # bank_account.create_account()   
 bank_account.deposit()
 # bank_account.withdraw()   
 bank_account.check_balance()
 print("THANKYOU FOR BANKING WITH US")

elif opt==2:
 from bank_package.base import Bank

 customer_name = input("Enter your name: ")
 bank_account = Bank(customer_name)    
 # bank_account.create_account()   
 # bank_account.deposit()
 bank_account.withdraw()   
 bank_account.check_balance()
 print("THANKYOU FOR BANKING WITH US")

elif opt==3:
 from bank_package.base import Bank

 customer_name = input("Enter your name: ")
 bank_account = Bank(customer_name)    
 bank_account.create_account() 
 dob=str(input("Enter your birthdate:"))
 print(dob)
 Pan=str(input("Enter your Pan card number:"))
 print(Pan)
 adhar=int(input("Enter the Adhar Card Number:"))
 print(adhar)
 add=str(input("Enter the Address:"))
 print(add)  
 bank_account.deposit()
 #bank_account.withdraw()   
 bank_account.check_balance()

 print("THANKYOU FOR BANKING WITH US")

elif opt==4:
 print("DO YOU HAVE ACCOUNT IN THIS BANK!!")

 ans=str(input("Do You  YES/NO")).lower()

 if ans=="no":
   print("DO YOU WANT TO CREATE ACCOUNT IN THIS BANK??")
   acc=str(input("YES/NO??")).lower()
   if acc=="no":
    print("WITHOUT BANK ACCOUNT YOU CANT APPLY FOR LOAN")
    print("THANKYOU FOR BANKING WITH US")
   elif acc=="yes":
    from bank_package.base import Bank
    customer_name = input("Enter your name: ")
    bank_account = Bank(customer_name)    
    bank_account.create_account()   
    #bank_account.deposit()
    dob=str(input("Enter your birthdate:"))
    print(dob)
    Pan=str(input("Enter your Pan card number:"))
    print(Pan)
    adhar=int(input("Enter the Adhar Card Number:"))
    print(adhar)
    add=str(input("Enter the Address:"))
    print(add) 
    bank_account.deposit() 
    #bank_account.withdraw()   
    bank_account.check_balance()
    print("YOU HAVE SUCCESSFULLY CREATED ACCOUNT!!YOU CAN APPLY FOR LOAN")

    kyc=str(input("Have You Done Your KYC: YES/NO")).lower()

    if kyc=="yes":
     update=str(input("DO YOU WANT TO UPDATE YOUR KYC??YES/NO")).lower()
     if update=="no":
      print("CONGRATULATIONS YOU CAN APPLY FOR LOAN")
      print("CHOOSE 1 FOR GOLD LOAN")
      print("CHOOSE 2 FOR EDUCATIONAL LOAN")
      print("CHOOSE 3 FOR HOME LOAN")

      loan=int(input("Enter your Loan preference:"))

      if loan==1:
       from bank_package import gold_loan
       gold_loan

      elif loan==2:
       from bank_package import education_loan
       education_loan
    
      elif loan==3:
       from bank_package import home_loan
       home_loan

       print("THANKYOU FOR BANKING WITH US")

    elif kyc=="no":
      print("DO YOU WANT TO DO KYC WITHOUT KYC YOU CAN HAVE LOAN")

      P=str(input("enter yes/no")).lower()
      if P=="no":
       print("YOU CANT HAVE LOAN THANKOU FOR BANKING WITH US")
      elif P=="yes":
       from bank_package.kyc import Yashika2

        # Create an instance of the inherited class Yashika2
       yashika_instance = Yashika2()

       # Call create_account method
       yashika_instance.create_account()
       print("YOUR KYC IS DONE !!YOU CAN APPLY FOR LOAN")

       print("CHOOSE 1 FOR GOLD LOAN")
       print("CHOOSE 2 FOR EDUCATIONAL LOAN")
       print("CHOOSE 3 FOR HOME LOAN")

       loan=int(input("Enter your Loan preference:"))

       if loan==1:
        from bank_package import gold_loan
        gold_loan

       elif loan==2:
        from bank_package import education_loan
        education_loan
    
       elif loan==3:
        from bank_package import home_loan
        home_loan

        print("THANKYOU FOR BANKING WITH US")

 elif ans=="yes":
    kyc=str(input("Have You Done Your KYC: YES/NO")).lower()

    if kyc=="yes":
     update=str(input("DO YOU WANT TO UPDATE YOUR KYC??YES/NO")).lower()
     if update=="no":
      print("CONGRATULATIONS YOU CAN APPLY FOR LOAN")
      print("CHOOSE 1 FOR GOLD LOAN")
      print("CHOOSE 2 FOR EDUCATIONAL LOAN")
      print("CHOOSE 3 FOR HOME LOAN")

      loan=int(input("Enter your Loan preference:"))

      if loan==1:
       from bank_package import gold_loan
       gold_loan

      elif loan==2:
       from bank_package import education_loan
       education_loan
    
      elif loan==3:
       from bank_package import home_loan
       home_loan

       print("THANKYOU FOR BANKING WITH US")

     elif update=="yes": 
    
       from bank_package.kyc import Yashika2

       if __name__ == "__main__":
     # Create an instance of the inherited class Yashika2
        yashika_instance = Yashika2()

     # Call each update method separately
        yashika_instance.update_name('new_name')
        yashika_instance.update_mobile_number('new_mobile_number')
        yashika_instance.update_address('new_address')
        yashika_instance.update_pan_card_number('new_pan_card_number')
        yashika_instance.update_adhar_card_number('new_adhar_card_number')
        yashika_instance.update_age('new_age')

        print("YOUR KYC HAS BEEN UPDATED,YOU CAN APPLY FOR LOAN")

        print("CHOOSE 1 FOR GOLD LOAN")
        print("CHOOSE 2 FOR EDUCATIONAL LOAN")
        print("CHOOSE 3 FOR HOME LOAN")

        loan=int(input("Enter your Loan preference:"))

        if loan==1:
         from bank_package import gold_loan
         gold_loan

        elif loan==2:
         from bank_package import education_loan
         education_loan
    
        elif loan==3:
         from bank_package import home_loan
         home_loan

         print("THANKYOU FOR BANKING WITH US")

    elif kyc=="no":
 
      from bank_package.kyc import Yashika2
 
      if __name__ == "__main__":
      # Create an instance of the inherited class Yashika2
       yashika_instance = Yashika2()

       print("CONGRTULATIONS YOUR KYC IS DONE NOW YOU CAN APPLY FOR LOAN!!")

       print("CHOOSE 1 FOR GOLD LOAN")
       print("CHOOSE 2 FOR EDUCATIONAL LOAN")
       print("CHOOSE 3 FOR HOME LOAN")

       loan=int(input("Enter your Loan preference:"))

       if loan==1:
        from bank_package import gold_loan
        gold_loan

       elif loan==2:
        from bank_package import education_loan
        education_loan
    
       elif loan==3:
        from bank_package import home_loan
        home_loan

        print("HANKYOU FOR BANKING WITH US")

elif opt==5:
 
 print("Enter 1 For New KYC ")
 print("Enter 2 for Updating KYC")
 
 kyc2=int(input("Enter your Option:"))

 if kyc2==1:
 
  from bank_package.kyc import Yashika2
  # Create an instance of the inherited class Yashika2
  yashika_instance = Yashika2()

  # Call create_account method
  yashika_instance.create_account()

  print("THANYOU FOR BANKING WITH US")
 elif kyc2==2:

  from bank_package.kyc import Yashika2

  # Create an instance of the inherited class Yashika2
  yashika_instance = Yashika2()

     # Call create_account method
     #yashika_instance.create_account()

     # Call each update method separately
  yashika_instance.update_name('new_name')
  yashika_instance.update_mobile_number('new_mobile_number')
  yashika_instance.update_address('new_address')
  yashika_instance.update_pan_card_number('new_pan_card_number')
  yashika_instance.update_adhar_card_number('new_adhar_card_number')
  yashika_instance.update_age('new_age')

  print("THANKYOU FOR BANKING WITH US")
 




     








    
  



      







