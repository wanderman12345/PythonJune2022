count = int(input("How Many Numbers you want to Enter:"))
number_list = []

for eachNumber in range(0, count):
    in_number = int(input("Enter a Number:"))
    number_list.append(in_number)

print("Thank You", number_list)

max = number_list[0]
min = number_list[0]
total = 0
avg = 0
for eachValue in number_list:
    if max < eachValue:
        max = eachValue
    if min > eachValue:
        min = eachValue
    total = total+eachValue

avg = total / len(number_list)
print("Max value is", max)
print("Min value is", min)
print("Avg value is", avg)