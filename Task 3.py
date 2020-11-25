# 1) Python script to merge two Python dictionaries #
x = {'Name': 'Nivar', 'distance': 500}
y = {'speed': 145, 'Time': '1:52pm'}
z = x.copy()
z.update(y)
print(z)
# 2) Python program to remove a key from a dictionary #
x = {'Name': 'Nivar', 'distance': 500, 'speed': 145, 'Time': '1:52pm'}
del x['distance']
print(x)
# 3) Python program to map two lists into a dictionary #
x = ['Red', 'Blue', 'Green', 'White']
y = ['Fire','Water','Land','Air']
z = dict(zip(x, y))
print(z)
# 4) Python program to find the length of a set #
setA = set([ 5, 10, 15, 20, 25 ])
print(len(setA))
# 5) Python program to remove the intersection of a 2nd set from the 1st set #
num1 = {1, 2, 3, 4, 5}
num2 = {3, 4, 5, 6, 7}
print ("original sets")
print(num1)
print(num2)
print("Removed the intersection of a 2nd set from the 1st set")
print(num1 - num2)