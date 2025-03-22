my_list = []

# Appending the elements 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending elements:", my_list)

# Inserting 15 at the second position (index 1).
my_list.insert(1, 15)
print("After inserting 15 at the second position:", my_list)

# Extending with another list.
my_list += [50, 60, 70]
print("After extending:", my_list)

# Removing the last element.
my_list.pop()
print("After popping last element:", my_list)

# Sorting the list in ascending order.
my_list.sort()
print("After sorting:", my_list)

# Finding and printing the index of 30.
i = my_list.index(30)
print("The index for 30 is:", i)
