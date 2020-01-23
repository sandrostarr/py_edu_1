words = ['мадам', 'топот', 'test', 'madam', 'word']
my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
p_list = []
p_list2 = []

# for w in words:
#     if w == w[::-1]:
#         p_list.append(w)
#     else:
#         print(f' {w} - это НЕ слово - палиндром')
# print(p_list)

# my_str2 = my_str.copy()
# my_str2.
# print(my_str2)

for f in my_str:
    t = f
    p_list2 = []
    for s in t:
        if s == ' ':
            continue
        s = s.lower()
        p_list2.append(s)
    if p_list2 == p_list2[::-1]:
        print(t)
