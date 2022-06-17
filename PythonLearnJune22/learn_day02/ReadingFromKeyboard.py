# Input name as variable
# Input age as variable - read value from Keyboard
# HW - Combine these two conditions in single if statement - provide appropriate output

name = input("Enter Your Name : ")
if name.isalpha():
    print("Hello ", name, type(name))
else:
    print("Wrong Name Entered")
    name="Unknown"

age = input("Enter Your Age: ")
if age.isnumeric():
    int_age = int(age)
    validity_upto = int_age + 5
    print("Your Policy is valid upto ", validity_upto)
else:
    print("Invalid Age Entry. Please restart")

email = input("Enter Your Email ID: ")
# condition to find if @ exists and . exists
at_index = email.find('@')
if (at_index > 0) and (email.find('.') > at_index):
    print("Valid Email ID ", email)
