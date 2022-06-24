# Dictionaries are written in Curly Braces { "Key" : "value"}
sampleDictionary = {
    'name': "Camry",
    'make': "Toyota",
    'Year': 2020,
    'Color': 'Grey',
}

# Accessing Items: sampleDictionary["101"]
print(sampleDictionary)
print(sampleDictionary['Color'])
print(sampleDictionary.get('Year'))
sampleDictionary['engine'] = "V6 Core Engine" # Add new value
sampleDictionary['Color'] = "White" # replace the value
print(sampleDictionary)
print(len(sampleDictionary))

print("**** Iterate with key ***")
for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary[eachKey])

print("**** Iterate with key, value - with items() ***")
for eachKey, eachValue in sampleDictionary.items():
    print(eachKey, eachValue)

print("**** Iterate with Values ***")
for eachValue in sampleDictionary.values():
    print(eachValue)

# What is a proper data structure to keep only Keys of dictionary - Set
# What is a proper data structure to keep only Values of dictionary - List

if 'Color' in sampleDictionary:
    print("Color is provided")

if 'White' in sampleDictionary.values():
    print("Color is White")

sampleDictionary.popitem() # removed last entered key, value pair
print(sampleDictionary)
sampleDictionary.pop('make')
print(sampleDictionary)
sampleDictionary.clear()
print(sampleDictionary)