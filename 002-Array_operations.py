'''
    # create Arrays
    # Random indexing --> O(1) get items if we kwon the index !!!
    # Array index value change
    # Print all Array elements one by one
    # Using slice[] operator acces array elements
    # O(N) Search running time
'''

# create Arrays
number=[12,34,567,8,9.6,8,4,56,34]

# Random indexing --> O(1) get items if we kwon the index !!!
print('1-access array using index value')
print(number[0])
print("index 2,5,1,0:",number[2],number[5],number[1],number[0])


#Array index value change
print('\n2-Array index value change')
number[1]='String' #In python array support any data-type
print(number[1])


#Print all Array elements one by one
print('\n3-Print all Array elements one by one')
for num in number:
    print(num)


#Using slice[] operator acces array elements
print('\n4-Using slice[] operator acces array elements')
print(number[:])
print(number[:3])
print(number[:-2])


# O(N) Search running time
print('\n5-O(N) Search running time')
numbers=[23,56,87,345,67,89]
maximum=numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

print(maximum)
