# gold_loan_package/gold_loan_application.py

class gold:
    print("Welcome to the Gold Loan Application Form")
    
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    gold_value = float(input("Enter the value of gold you want to pledge: $"))
    
    if age>=18 and age<=65:
        print("You are approved for Gold Loan")
    else:
        print("You are not eligible for Gold Loan")


