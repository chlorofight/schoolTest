# Data Types
# Int
-267492
# Float
284.0
-9.5
# String
'hello'
'4.6'
"hello"
# Bool/Boolean
True
False
# Output and priting
print("hello", 'end', 43, False)

print('hello' + 'end' + 43 + False)

print("hello", 43, False, end='|')
print('Python!')

# variables
name = 'Steve'
greetings = 'how are you'
print(name)
print(name, greetings)
# variable naming conventions
# snake case
hello_world
# camel case
helloWorld
# illegal variable names
9hello
hello world
# input
name = input('Name: ')
age = input('Age: ')

print('Hello', name, 'you are', age, 'years old')

print('Hello' + name + 'you are' + age + 'years old')

print(f'Hello {name} you are {age} years old')


# arithmetic operators
x = 10
y = 3
result = x % y
print(result)

result = x // y
print(result)

result = x ** y
print(result)


# type casting

num = input('Number: ')
print(num - 5)
# the code won't work as num is of the type string.
# you can use int() to cast the type into an integer for calculations
# use the type() so you know the num is a string even though it looks like a number
print(type(num))

# string methods
hello = 'hello world'
print(hello.capitalize())

print(hello.lower())

print(hello.upper())

# count() return the occurance of a character in a string
hello = 'HELLO WORLD'
print(hello.count('o'))
print(hello.lower().count('o'))

# comparison operators
""" ==
!=
<=
>=
>
< """
x = 'hello'
y = 'hello'

print(x == y)
print(x != y)
print(x == y)
print('a' > 'Z')
print(ord('a'))
print(ord('Z'))
print('ab' > 'ad')

result = 6 == 6
print(result)

# run the code below
x = 7
y = 8
z = 0
result1 = x == y
result2 = y > x
result3 = z < (x + 2)
print(result1, result2, result3)
result4 = result1 or result2
print(result4)

# logical operators
and
or
not

# IF-ELSE-ELIF
# version 1
coupon = input('Enter your coupon code: ')
total_price = 100
if coupon == 'flashsale21':
    total = total * 0.8
    print('valid coupon')
else:
    print('invalid coupon')
print(total)

# version 2
coupon = input('Enter your coupon code: ').lower()
total_price = 100
if coupon == 'flashsale21':
    total = total * 0.8
    print('valid coupon')
elif:
    coupon == 'newcomer10':
    total = total * 0.9
    print('valid coupon')
else:
    print('invalid coupon')
print(total)

# List
robots = ['bb8', 'wall-e', 'r2d2', 'r4d5']

robots.append('C3PO')
print(len(robots))
robots.pop()
robots.pop(3)  # delete the item at index 3
robots.remove('bb8')
robots.insert(2, 'johny5')
robots.index('wall-e')
robots.count('bb8')

# for loops (start,stop,step)
for i in range(10):
    print(i)

for i in range(2, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

x = [3, 5, 2, 7, 9, 10]
for i in range(_______):
    print(x[i])

x = [3, 5, 2, 7, 9, 10]
for i in x:
    print(i)

x = '40232356'
y = ''
for c in x:
    y += str(int(c)*2)
print(y)


# while loops
game_over = False
x = 0
while game_over == False:
    print('run')
    x += 1
    if x == 5:
        game_over = True

# functions


def add(x, y):
    print(x+y)
    return x+y


result = add(5, 6)
print(result)

# dictionary
x = {'locker1': 'Steve',
     'locker2': 'James',
     'locker3': 'Kirby'}
for key in x:
    print(key, _______)


print('locker4' in x)


print(x['locker1'])
# it returns True if the key is in the dictionary
print('locker4' in x)
print(x.values())
print(list(x.keys()))
for key, value in x.items():
    print(key, value)
