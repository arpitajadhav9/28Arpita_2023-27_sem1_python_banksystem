# module1/base.py
class Yashika:
    def __init__(self):
        self.name = input("Enter name: ")
        self.mobile_number = input("Enter mobile number: ")
        self.age = int(input("Enter age: "))
        self.address = input("Enter address: ")
        self.pan_card_number = input("Enter PAN card number: ")
        self.adhar_card_number = input("Enter Aadhar card number: ")

class Yashika2(Yashika):
    def create_account(self):
        print(f"Account created for {self.name}")

    def update_name(self, new_name):
        self.name = new_name
        new_name=str(input("Enter Your updated name:"))
        print(f"Mobile name updated to",new_name)


    def update_mobile_number(self, new_mobile_number):
        self.mobile_number = new_mobile_number
        new_mobile_number=int(input("Enter Your updated Mobile number:"))
        print(f"Mobile number updated to ",new_mobile_number)

    def update_address(self, new_address):
        self.address = new_address
        new_address=str(input("Enter Your updated Address:"))
        print(f"Address updated to ",new_address)

    def update_pan_card_number(self, new_pan_card_number):
        self.pan_card_number = new_pan_card_number
        new_pan_card_number=str(input("Enter Your updated Pan Card number:"))
        print(f"PAN card number updated to ",new_pan_card_number)

    def update_adhar_card_number(self, new_adhar_card_number):
        self.adhar_card_number = new_adhar_card_number
        new_adhar_card_number=int(input("Enter Your updated Adhar Card number:"))
        print(f"Aadhar card number updated to ",new_adhar_card_number)

    def update_age(self, new_age):
        self.age = new_age
        new_age=int(input("Enter Your updated Age:"))
        print(f"Age updated to ",new_age)
