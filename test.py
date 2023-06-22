# import copy

# myList = [1,2,3,[4,5]]
# normalcopy = myList.copy()

# deepCopy = copy.deepcopy(myList)


# normalcopy[3][0]= 7
# print(normalcopy)
# print(deepCopy)
# student = {
#     "name": "John Doe",
#     "age": 20,
#     "grades": [85, 92, 78],
#     "address": {
#         "street": "123 Main St",
#         "city": "New York",
#         "state": "NY"
#     }
# }

# print(student["age"]["address"]["city"])

# import random
# number = random.randint(1,10)
# isGuessRight = False

# while isGuessRight != True:
#     guess = int(input("Enter a number between 1 and 9 : "))
#     if guess == number:
#         print("The guess is correct : {}".format(guess))
#         isGuessRight = True
#     else:
#         print("Sorry {} is not wright guess".format(guess)) 



# salary = 20000
# name = input("Enter your name : ")
# if (name == 'anup'):
#     print("bonous salary: ",salary*0.2)
# else:
#     print("bonous salary: ",salary*0.1)


# def switch_case_example(args):
#     if args == 'option1':
#         print("Option 1")
#     elif args == 'option2':
#         print("Option 2")
#     elif args == 'option2':
#         print("Option 3")
#     else: 
#         args == 'option4'
#         print("Option 4")
# switch_case_example('option1')


# fruits = ["apple","mango","grapes"]
# for falful in range(len(fruits)):
#     print(fruits[falful])

# string1 = "Hello world"
# print(string1[5:12])
# print(string1[0])

greeting = "  Hello,"
name = input("Enter your name: ")
message = greeting + " " + name + "! HoW ArE yOU ?   "
# print(message)
# print("The length of" + message + "is ",  len(message))
upper = message.upper()
# print(upper)
lower = message.lower()
# print(lower)
stripped = message.strip() #removes first and last spaces
# print(stripped)
words = message.split(",")
# print(words)
replace = message.replace("Hello","Hi")
# print(replace)
index = message.find("Hello")
# print(index)

rev_str = message[::-1]
# print(rev_str)
my_tuple = (5,3,1,2)
sort_tuple = tuple(sorted(my_tuple))
print(sort_tuple)