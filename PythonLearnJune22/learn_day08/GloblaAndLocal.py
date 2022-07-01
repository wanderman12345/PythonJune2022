message = "Hello" # Global

def greet(name):
    global message
    message = "Howdy"
    # Local variable - local variable name is same as globle variable name
    # this will be called as Shadow variable
    print("greet ", name, message)


print("Before function call :: " , message)
greet('Rishi')
print("After function call :: " , message)