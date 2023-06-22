# Question 1: Write a program that prompts the user to enter their name and their favorite color. Then, create a message
# that combines their name and favorite color to form a personalized message. Finally, print the message on the console.

# name = input("Enter your name : ")
# color = input("what is your favorite color ? : ")
# message = "Hi " + name + " Your favourite color is "+ color + "."
# print(message)

# Question 2: Write a program that prompts the user to enter a sentence. 
# Count and display the number of words in the sentence.

# user_inp = input("Write a Short Sentence : ")
# print(len(user_inp.split()))

# Question 3: Write a program that prompts the user to enter their full name (first name and last name). 
# Convert the name to uppercase and display it in reverse order with a comma separating the last name and the first name.

# full_Name = input("Enter your full name : ")
# first_name , last_name = full_Name.split()
# print(first_name)
# print(last_name)
# rev = last_name.upper() + "," + first_name.upper()
# print(rev)


# Question 4: Write a program that takes a sentence as input and replaces all occurrences of a specific word 
# with another word. Prompt the user to enter the original sentence, the word to be replaced, 
# and the replacement word. Display the modified sentence.

# sentence = input("Enter a sentence : ")
# rep_word = input("Enter a word to replace : ")
# replacement_word = input("Enter the replacement word : ")
# modified_sentence = sentence.replace(rep_word,replacement_word)
# print("Modified one",modified_sentence)



my_list = [1,3,5,7,9]
# print(my_list)
# print(my_list[1])
# my_list[1] = 10
# print(my_list)
# my_list.append(12)
# popped = my_list.remove(7)
# print(my_list)
# print(popped)
sliced_list = my_list[1:4]
# print(sliced_list)
new_list = my_list + sliced_list
# print(new_list)
# print(99 in new_list)
new_list.sort(reverse=True)
print(new_list)
# print (new_list)


