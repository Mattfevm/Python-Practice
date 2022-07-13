
# Create a list with 6 numbers and print the greatest number  without using inbuilt methods

# first create an empty list
lst = []

# a for to iterating the elements on the list
for i in range(6):
    elem = int(input("please input numbers: "))
    lst.append(elem)

print("this is your list: ", lst)

max_value = 0

# a for to iterating and find the greater number

for x in lst:
    if x > max_value:
        max_value = x

print(max_value)

