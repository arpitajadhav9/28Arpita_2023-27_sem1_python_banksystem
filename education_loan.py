# education_loan_package/education_loan_application.py

class education:
    def _init_(self, name, age, course,tution_fee,cibil_score):
        self.name = name
        self.age = age
        self.course = course
        self.tution_fee=tution_fee
        self.cibil_score=cibil_score
    print("Welcome to the Education Loan Application Form")
    
    name = input("Enter your full name: ")
    age = int(input("Enter your age: "))
    course = input("Enter the course you want to pursue: ")
    tuition_fee = float(input("Enter the tuition fee for the course: $"))
    cibil_score=int(input("Enter your Parent/Gardian Account Cibil Score:"))

    if cibil_score>=700:
        print("Education Loan is Approved Bank will contact for further Details")
    else:
        print("Cibil Score is Low due to which we cant approve Educational Loan")
    
    
