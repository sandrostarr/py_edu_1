# counter = 0
# arr1 = ['even', 5, 'even', 1, 'even', 18, 'even', 2, 'odd', 7, 'even']

# def check(arr, counter):
#     for key in arr:
#         if key == 'odd':
#             return counter
#         counter+=1

# def watch(arr):
#     for key in arr:
#         if key == check(arr, counter):
#             return True

# print(watch(arr1))


counter = 1
n = 8

def stat(n, counter):
    while counter <= n:
        summ = check(counter)
        print(summ)
        counter+=1

def check(counter):
    if counter % 3 == 0:
        b = counter
        return b


stat(n, counter)