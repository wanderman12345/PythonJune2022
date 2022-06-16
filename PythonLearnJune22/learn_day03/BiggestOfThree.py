'''
Find the biggest number out of three unequal numbers

'''
var_one = 100
var_two = 120
var_three = 14

if (var_one > var_two) and (var_one > var_three):
    print("Biggest Number is var_one ", var_one)
elif var_two > var_three:
    print("Biggest Number is var_two ", var_two)
else:
    print("Biggest Number is var_three ", var_three)

print("Done!")