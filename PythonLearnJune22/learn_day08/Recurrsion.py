'''
Add N numbers
'''

def tri_recursion(n):
    if n > 0:
        result = n + tri_recursion(n - 1)
        print(result)
    else:
        result = 0
    return result

total = tri_recursion(5)
print(total)