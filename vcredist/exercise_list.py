

# ---------------   1. Write a Python program to sum all the items in a list.

# data = [1,2,3,4,5,6]
# result = 0
# for item in data:
#     result += item
# print(f"This is result sum all item : {result} ")

# ---------------   2. Write a Python program to multiply all the items in a list.

# data = [1,2,3,4,5,6]
# result = 0
# if len(data) > 0:
#     result = 1
#     for item in data:
#         result *= item
# print(f"This is result multiply all item : {result} ")

# ---------------   3. Write a Python program to get the largest number from a list.

# data = [1,2,3,4,5,6,-99,-1,-2,77,0]
# data.sort() # sort default increment if you set reverse = True is descending
# length = len(data) -1
# print(f"This is result largest all item : {data[length]} ")


# ---------------   4. Write a Python program to get the smallest number from a list.

# data = [1,2,3,4,5,6,-99,-1,-2,77,0]
# data.sort(reverse= True) # sort default increment if you set reverse = True is descending
# length = len(data) -1
# print(f"This is result smallest all item : {data[length]} ")

# ---------------   5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

# data = ['abc', 'xyx', 'aba', '1221']
# result = 0
# for item in data:
#     if len(item) > 1 and item[0] == item[len(item) - 1]:
#         result +=1
# print(f"This is result  all item : {result} ")

# ---------------   6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.


# data =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# def last(n): return n[-1]
#
# result = sorted(data, key= last)
# print(f"This is result  all item : {result} ")

# --------------- 7. Write a Python program to remove duplicates from a list.

# data = [1,2,3,4,1,2]
# print(data)
# result = set(data)
# print(f"This is result  all item : {result} ")

# --------------- 8. Write a Python program to check a list is empty or not.

# data = []
# result = not data
# print(f"This is result  all item : {result} ")

# --------------- 9. Write a Python program to clone or copy a list.

# data = [1,2,3,4,1,2]
# result = data.copy() # list(data)
# print(f"This is result  all item : {result} ",id(result), id(data))
# print(result == data) # compare value
# print(result is data) # compare object

# ---------------  10. Write a Python program to find the list of words that are longer than n from a given list of words.

# def compute(n, data):
#     result = []
#     for item in data.split():
#         if len(item) > n:
#             result.append(item)
#     return result
#
# result = compute(3, "The quick brown fox jumps             over the                lazy              dog")
# print(f"This is result  all item : {result} ")

# ---------------   11. Write a Python function that takes two lists and returns True if they have at least one common member.

# def compute(a,b):
#     for item in a :
#         if item in b:
#             return True
# result = compute([1,2,3],[1,5,6])
#
# print(f"This is result  all item : {result} ")


# ---------------    12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

# data = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# result = [value for index,value in enumerate(data) if index not in (0,4,5)]
# print(f"This is result  all item : {result} ")

# ---------------    13. Write a Python program to generate a 3*4*6 3D array whose each element is *.

# data = [
#     [
#         ['*','*','*','*'],
#         ['*','*','*','*'],
#         ['*','*','*','*']
#     ],
#     [
#         ['*', '*', '*', '*'],
#         ['*', '*', '*', '*'],
#         ['*', '*', '*', '*']
#     ], [
#         ['*','*','*','*'],
#         ['*','*','*','*'],
#         ['*','*','*','*']
#     ], [
#         ['*','*','*','*'],
#         ['*','*','*','*'],
#         ['*','*','*','*']
#     ], [
#         ['*','*','*','*'],
#         ['*','*','*','*'],
#         ['*','*','*','*']
#     ], [
#         ['*','*','*','*'],
#         ['*','*','*','*'],
#         ['*','*','*','*']
#     ],
# ]
# data = [ [ ['*' for row in range(6)]  for row in range(4) ] for row in range(3)]
#
# print(data)

# ---------------  14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

# data = [7,8, 120, 25, 44, 20, 27]
# result = [item for item in data if item % 2 != 0]
# print(f"This is result  all item : {result} ")

# ---------------   15. Write a Python program to shuffle and print a specified list.

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# result = sorted(color, reverse= True)
# print(f"This is result  all item : {result} ")

# ---------------    16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

# data = list()  # []
# for i in range(1,31):
#     data.append(i**2)
# print(f'5 element first: {data[:5]}')
# print(f'5 element last: {data[-5:]}')

# ---------------   17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

# data = [i**2 for i in range(1,31)]
# print(data)
# print(f'except 5 element first: {data[5:]}')

# ---------------    18. Write a Python program to generate all permutations of a list in Python.

# list = [1,2,3,4]
# giai_thua = 1
# for i in  range(1,len(list)+1):
#    giai_thua *= i
# result = []
# for  i in range(1, giai_thua + 1):
#     for i in range(1, giai_thua + 1):
#         len_lst = len(list)
#         item = ()

# ---------------   19. Write a Python program to get the difference between the two lists.

# def compute(a,b):
#     result = []
#
#     for item in a:
#         if item not in b:
#             result.append(item)
#
#     for item in b:
#         if item not in a:
#             result.append(item)
#     return  result
#
# result = compute([1,2,3,4],[3,4,5])
# print(f'result difference two list: {result}')

# list1 = [1, 3, 5, 7, 9]
# list2=[1, 2, 4, 6, 7, 8]
# result = [set(list1) ^ set(list2)]
# print(f'result difference two list: {result}')

# ---------------    20. Write a Python program access the index of a list

# list1 = [1, 3, 5, 7, 9]
# for index, value in enumerate(list1):
#     print(index, value)












