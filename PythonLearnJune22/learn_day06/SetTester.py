sampleSet = {'Apple', 'Pineapple', 'Banana', 'Apple'}
anotherSet = {'A', 'D', 'F', 'Z', 'W'}
# Unordered
print(anotherSet)
# no duplicates
sampleSet.add("Blueberry")
sampleSet.add("Blueberry")
print(sampleSet)
sampleSet.remove('Apple') # dont use without checking membership
print(sampleSet)
sampleSet.discard('Apple') # no error if item isnt there
print(sampleSet)
sampleSet.update(anotherSet)
print(sampleSet)