sampleList = ['Apple', 'Banana', 'pineapple']

print(sampleList)
print(sampleList[0])
print(sampleList[0:2])# range access
sampleList.append("Blueberry")
sampleList.append("Blueberry")
sampleList.insert(1, "Blackberry")
print(sampleList)
'''
sampleList.remove('Banana')
print(sampleList)
sampleList.pop(1)
print(sampleList)
del sampleList[0]
print(sampleList)
'''
for eachFruit in sampleList:
    print(eachFruit)

# membership
if 'Apple' in sampleList:
    print("Apple is in sampleList")

# not membership
if 'potato' not in sampleList:
    print("Potato is not a fruit")

# Only when List is homogeneous
sampleList.sort()
print(sampleList)
sampleList.reverse()
print(sampleList)

sampleList.clear()
print(sampleList)