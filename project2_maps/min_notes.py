letters = {'x': 6, 'b': 5, 'k': 4, 'd': 5, 'e': 4}

# returns the minimum in a sequence
""" is not index based as it returns b
think dictionaries are not ordered as lists"""
resp = min(letters)

val = letters['x']


""" The key function is called with each element of the list
and return val then used for comparison e.g. find the
min in this instance"""

# looks up the [1] element in dict items tuples
# returns the key=val combination that has min value for element [1]
res1 = min(letters.items(), key=lambda x: x[1])

# evaluates lambda that returns values for the k-th elements
# it then returns the min of dict for the smallest value
res2 = min(letters, key=lambda k: letters[k])  

# uses get method that returns the value for the key in a dictionary
# min returns the key for which the value returned by lambda is min
# each value has a key associated and min is evaluated on the values 
# it returns the first encountered (in this case k), not e
res3 = min(letters, key=letters.get)


""" all these functions can't tell if theres two keys 
with min values in the dictionary"""
