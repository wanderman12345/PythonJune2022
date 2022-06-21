'''
while condition:
    block of code when condition is true
    condition modifier

out of loop when condition is false
'''
# Sum of 1 to 10

counter = 1;
total = 0;
error_point = 15
while counter <= 25:
    if counter == error_point:
        counter += 1
        continue
    print("Counter :: ", counter)
    total = total + counter
    counter = counter + 1 # counter +=1

print("Counter value is {} and total is {}".format(counter, total))