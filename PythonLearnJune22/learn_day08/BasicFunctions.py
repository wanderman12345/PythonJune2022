# method or function are same
# name='Unknown User' - this is called as default parameter value
def greet(name='Unknown User'):
    print("Hello ", name)

def tax_calculation(items):
    # item_name : item_price
    total = 0
    for name, price in items.items():
        total = total + price
        print(name, price)
    return total * 0.06



def add(valOne, valTwo):
    return valOne + valTwo

# Python function can return multiple values
def calc(varOne, varTwo):
    sum = varOne + varTwo
    multiply = varOne * varTwo
    divide = varOne / varTwo
    return sum, multiply, divide


greet('David')
greet('Neil')
# TypeError: greet() missing 1 required positional argument: 'name'
greet()

total = add(5,5)
print("Total", total)

calc_result = calc(10,2)
print(calc_result, type(calc_result)) # what is data type of calc_result

items = {
    "Apples" : 2.69,
    "Potatos" : 4.99,
    "toothpaste" : 1.29,
    "Milk" : 4.99,
}
tax = tax_calculation(items)
print("Tax on items ", tax)