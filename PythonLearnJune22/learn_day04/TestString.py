greet = 'hello , world!'

print(greet)
print(greet[0])
print(greet[0:5])
print(greet[-1])
# String functions
print("greet.upper() :: " , greet.upper())
print("greet.isupper() :: " , greet.isupper())
print("greet.lower() :: " , greet.lower())
print("greet.islower() :: " , greet.islower())
print("greet.title() : " , greet.title())
print("greet.capitalize() : " , greet.capitalize())

# finding string as number
age = "21"
print("greet.isnumeric() : " ,greet.isnumeric())
print("greet.isdigit() : " ,greet.isdigit())
print("age.isnumeric() : " ,age.isnumeric(), type(age))
print("age.isdigit() : " ,age.isdigit())

name="David"
print("greet.isalpha() : " ,greet.isalpha())
print("name.isalpha() : " ,name.isalpha())

long_string = "This is Long String, This is Just for testing purpose"
first_index = long_string.find("is")
second_index = long_string.find("is", first_index+1)
three_index = long_string.find("is", second_index+1)
forth_index = long_string.find("is", three_index+1)
fifth_index = long_string.find("is", forth_index+1)

print("long_string.find('is') " , first_index) # first occurrence of query
print("second_index " , second_index)
print("three_index " , three_index)
print("forth_index " , forth_index)
print("fifth_index " , fifth_index)

print("long_string.count('is') " , long_string.count("is"))

print("len(long_string) : " , len(long_string))

test_string = "This is a {} book, by Author {}"
print(test_string.format("Good", "Dan Brown" ))
print(test_string.format("Good", "Dan Brown" ))