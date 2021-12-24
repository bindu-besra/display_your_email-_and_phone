
class PhoneEmail:

    def __init__(self, email, phone):
        email = input("Eenter your E-mail:-  ")
        phone = input("Enter your Phone number:-  ")
        self.email = email
        self.phone = phone

    def printinfo(self):
        print("Your email is '{}' and Phone Number is '{}' "   .format(
            self.email, self.phone))


user1 = PhoneEmail("email", "phone")
user1.printinfo()
