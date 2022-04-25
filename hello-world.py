# print('Hello world')

# name = 'jose'
# Age = 3

# print(f'Hello {name}, i am {Age} years old')

# Lists in Python
# my_list = ['one', 'two', 'three', 'four', 'five']


# print(my_list[1:3])

# List can be mutated unlike strings
# my_list.append('six')

# my_list.pop()
# print(my_list)

# new_list = ['a', 'e', 'x', 'b', 'c', 'd']
# num_list = [4, 1, 8, 3]

# new_list.sort()
# print(new_list)

# Dictionaries in Python
# Dictionaries are key value pairs and are like objects in JS

# my_dict = {'name': 'Jose', 'age': 30, 'country': 'Mexico'}

# print(my_dict['age'])

# fruits = {
#     'apple': 'red',
#     'banana': 'yellow',
#     'orange': 'orange',
#     'key': 'value',
#     'money': 28.22

# }

# print(fruits)
# x = 'apple'


# if x == 1:
#     print('x is 1')

# if True:
#   print('Its true')

# hungry = False

# if hungry:
#     print('Feed me')
# else:
#     print('Im not hungry')


# location = 'ball'

# if location == 'Auto shop':
#     print('Cars are cool')
# elif location == 'Bank':
#     print('Money is cool')
# elif location == 'Store':
#     print('Welcome to the store')
# else:
#     print('omoh')


# houses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for house in houses:
#     # check for even numbers
#     if house % 2 == 0:
#         print(f"Even num: {house}")
#     else:
#         print(f'Oddd num: {house}')

# for num in range(0, 11, 2):
#     print(num)

# index_count = 0

# for letter in 'abcde':
#     print(f'At index {index_count} the letter is {letter}')
#     index_count += 1

# UNDERSTAND THE ENUMERATE FUNCTION

# word = 'abcde'

# for index,letter in enumerate(word):
#     print(index)
#     print(letter)
#     print('\n')

# uNDERSTAND THE ZIP FUNCTION

# mylist1 = [1, 2, 3]
# mylist2 = [4, 5, 6]

# for idex,letter in zip(mylist1, mylist2):
#     print(idex)
#     print(letter)

# d = {'mykey': 3456}

# print(3456 in d.items())

# from random import shuffle

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# shuffle(mylist)
# print(mylist)

# ACCEPTING USER INPUT
# result = input ('Press enter a number to continue: ')

# print(type(int(result)))

# st = 'Print only the words that start with s in this sentence and samson is a silky and silly footballer'

# strings = st.split(' ')

# for s in strings:
#     if s[0] == 's':
#         print(s)

# for x in range(0, 11, 2):
#   print(x)

# divide_by_3 = [x for x in range(1, 51) if x % 3 == 0]

# print(divide_by_3)

# st = 'Print every word in this sentence that has an even number of letters'

# even = st.split(' ')
# for e in even:
#   if len(e) % 2 == 0:
#     print(e)

# for num in range(1,101):
#   if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
#   elif num % 3 == 0:
#     print('Fizz')
#   elif num % 5 == 0:
#     print('Buzz')
#   else:
#     print(num)

# st = 'Create a list of the first letters of every word in this string'

# string = [s[0] for s in st.split(' ') ]

# print(string)