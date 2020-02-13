# exercise ninja
# exercise1
# list1 = [1,'one',2,'two',3,'three']
#
# string_list = []
# int_list = []
#
# for num in list1:
#     if type(num) == str:
#         string_list.append(num)
#     else:
#         int_list.append(num)
#
# print(string_list)
# print(int_list)


# exercise3
# list1 = ['hello','goodbye','goodmorning','yes','hgjhgjhgjhgjhg2212121jgjgh','8979797979']
# longword = max(list1,key=len)
# print(longword)

# exercise4
# password = input('please enter your password: ')
# p = len(password)
# print('*'*p)

# exercise 5
# sandwich_orders = ['capresse','egg','avocado','cheese']
# finished_sandwiches = []

#
# for sandwich in sandwich_orders:
#         print(f'i made your {(sandwich)} sandwich!')
#
# for sandwich in sandwich_orders:
#     if type(sandwich) == str:
#         finished_sandwiches.append(sandwich)
#
# print(finished_sandwiches)
#
# for sandwich in sandwich_orders:
#         print(f'{(sandwich)} sandwich was made!')
#
# -----------------------------------------------------------
# exercises

# exercise 1
# prompt= input('Enter a value for "A": ')
# a = prompt
#
# prompt2 = input('Enter a value for "B": ')
# b = prompt2
#
# if a > b:
#     print('hello wold')
#
# else :
#     print('"A" is not grater than "B"')

#exercise2
# first = input("enter the first number: ")
# a = first
# second = input("enter the second number: ")
# b = second
# third = input("enter the third number: ")
# c = third
#
# if a > b and a > c:
#     print(f'{a}')
# elif b > a and b > c:
#     print(f'{b}')
# elif c > a and c > b:
#     print(f'{c}')
#exercise3
# month = input("Enter a month number: ")
# season = int(month)
# if season in range(3,6):
#     print('it is Spring!')
# elif season in range(6,9):
#     print('it is Summer!')
# elif season in range(9,12):
#     print('it is Autumn!')
# elif season in [1,2,12]:
#     print('it is Winter!')


# exercise4
# prompt = input("Enter a letter: ")
#
# if prompt in ['a','e','i','o','u']:
#     print("it is a vowel")
# else:
#     print("it is a consonant")

# exercise5
# import random
#
# prompt = int(input("enter a number to guess: "))
#
# number = random.randint(0,10)
#
# if number == prompt:
#     print(f"you got it the number is {number}")
# else:
#     print(f"try again the number was {number}")

# exercise6
# for num in range(1,21):
#    print(num)

# exercise 7
# for num in range(1,1000001):
#     print(num)
#


# exercise 8
# list= []
#
# for num in range(1,1000001):
#     list.append(num)
#
# print(min(list))
# print(max(list))

# exercise 9
#
# for i in range(1,6):
#      print("*" * i)

# exercise 10
# list = ["apples","bananas","mangoes","oranges"]
# index = list.index("apples")
# print(index)

# exercise 11

# list1 = [1,2,3]
# list2 = ['one','two','three']
#
# list = list1.extend(list2)
#
# print(list1)

# exercise 12
prompt = input("Enter a topping for your pizza!: ")

pizza = []

order = prompt.apend(pizza)

print(pizza)














