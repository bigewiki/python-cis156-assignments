import re

def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    email = get_email()
    print()
    phone = get_phone()
    print()
    first_name = get_first_name(full_name)   
    print("Hi " + first_name + ", thanks for creating an account.")
    # print the phone number in ddd.ddd.dddd format
    print(f'We\'ll text your confirmation fode to this number: {phone[slice(3)]}.{phone[slice(3,6)]}.{phone[slice(6,10)]}')

# new function for handling the input of a phone number
def get_phone():
    while True:
        phone = input("Enter your phone number: ")
        # Replace any non numeric characters with nothing (basically remove them)
        phone = re.sub(r'[^\d]', "", phone)
        if len(phone) == 10:
            return phone
        else:
            print("Your phone number is invalid, try again. ")

# new function for handling the input of an email
def get_email():
    while True:
        email = input("Enter your email: ")
        # Regex matching for a string that contains 1 or more characters
        # proceeding and following an @ symbol and ends with .com
        if re.match(r'^.+\@.+\.com$',email):
            return email
        else:
            print("Your email is invalid, try again. ")
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name
    
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password
        
if __name__ == "__main__":
    main()
