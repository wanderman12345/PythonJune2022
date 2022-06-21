'''
for each_variable in data_structure:
    execute line of code for each Variable

End of loop when all items in data_structure completes

range(start, stop, step) - start - included, stop -excluded (stop -1)
'''
error_point= 17
total = 0
for each_number in range(1, 21):
    if each_number == error_point:
        continue
    total = total + each_number
    print("Each Number from array :: " , each_number)

print("Total" , total)