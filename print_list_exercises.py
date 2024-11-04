#1. Creating a List
fruits = ["apple", "banana", "mango", "watermelon", "orange"]
print(fruits)

#2. Accessing Elements
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print("first element:", colors[0])
print("third element:", colors[2])
print("last element:", colors[4])

#3. Modifying a List
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)

#4. List Slicing
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = names[0:3]
print(subset)

#5. Looping through a List
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print("The square of",i,"is", i*i)

#6. List Methods: 
# Append
shopping_cart1 = []
shopping_cart1.append("milk")
shopping_cart1.append("bread")
shopping_cart1.append("eggs")

print(shopping_cart1)

# Extend
shopping_cart2 = ["butter", "cheese"]
shopping_cart1.extend(shopping_cart2)

print(shopping_cart1)

#7. Finding Maximum and Minimum in a List
numbers = [45, 22, 88, 56, 92, 33]
print("Maximum value:", max(numbers))
print("Miminum value:", min(numbers))

#8. Counting Occurrences
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a = letters.count("a")
print("count of a:", count_of_a)

#9. List Comprehension
even_squares = [x**2 for x in range(0, 11, 2)]
print("squares of all even numbers from 0 to 10:", even_squares)

#10. Removing Duplicates
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_elements = []
for x in nums:
    if x not in unique_elements:
        unique_elements.append(x)
print(unique_elements)        
