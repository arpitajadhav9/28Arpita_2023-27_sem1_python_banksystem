class HomeLoanApplication:
    def _init_(self, applicant, loan_amount, property_value,loan_to_value):
        self.applicant = applicant
        self.loan_amount = loan_amount
        self.property_value = property_value
        self.loan_to_value=loan_to_value

    applicant = input("Enter your name for the home loan application: ")
    loan_amount = float(input("Enter the desired home loan amount: "))
    property_value = float(input("Enter the property value: "))
    
    loan_to_value=property_value/loan_amount


    if loan_to_value>=0.2 and loan_to_value<=0.8:
        print("Loan is approved")
    else:
       print("loan is not approved")

       


   

