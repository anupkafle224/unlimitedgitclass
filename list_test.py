# Task 1: Create a list named "numbers" containing the numbers 1, 3, 5, 7, and 9.
numbers = [1, 3, 5, 7, 9]

# Task 2: Access and print the second element of the list.
print(numbers[1])  # Output: 3

# Task 3: Modify the third element of the list to 10.
numbers[2] = 10

# Task 4: Add the number 12 to the end of the list.
numbers.append(12)

# Task 5: Remove the number 5 from the list.
numbers.remove(5)

# Task 6: Create a new list named "sliced_list" that contains a slice of the original list from the second to the fourth element.
sliced_list = numbers[1:4]

# Task 7: Create a new list named "combined_list" by concatenating the original list with the sliced_list.
combined_list = numbers + sliced_list

# Task 8: Check if the number 8 is present in the combined_list and print the result.
print(8 in combined_list)  # Output: False

# Task 9: Sort the combined_list in ascending order.
combined_list.sort()

# Task 10: Print the final version of the combined_list.
print(combined_list)  # Output: [1, 3, 7, 9, 10, 12]
