# counter = 0
# arr1 = ["even", 4, "even", 7, "even", 55, "even", 6, "even", 10, "odd", 3, "even"]
# arr2 = ["even", 4, "even", 7, "even", 55, "even", 6, "even", 9, "odd", 3, "even"]
# arr3 = ["even", 10, "odd", 2, "even"]
#
# def odd_ball(arr, counter):
#     for key in arr:
#         if key == 'odd':
#             odd_index = counter
#             return odd_index
#         counter += 1
#
# def odd_find(arr, counter):
#     for key in arr:
#         if key == counter:
#             return True
#
# odd_index = odd_ball(arr1, counter)
# print(odd_find(arr1, odd_index))



# i = 1
# b = 0
# n = 10
# def find_sum(i, n):
#     while i <= n:
#         if divider1(i):
#             global b
#             b+=i
#         if divider2(i):
#             b+=i
#         i+=1
#
# def divider1(i):
#     if i % 3 == 0:
#         return True
#
# def divider2(i):
#     if i % 5 == 0:
#         return True
#
#
# find_sum(i, n)
# print(b)

names_ready=[]
names = ['Ryan', 'Kieran', 'Mark', 'John', 'David', 'Paul']

def get_names(names):
    for key in names:
        if len(key) == 4:
            names_ready.append(key)

get_names(names)
print(names_ready)