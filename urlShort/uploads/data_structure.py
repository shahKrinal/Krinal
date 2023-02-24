# ER1
def create_list():
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = []

    odd_list = l1[1::2]
    even_list = l2[::2]

    new_list = odd_list + even_list

    print(new_list)


create_list()


# ===================================

# ER 2
def edit_list(n):
    l = int(input("Enter the index"))
    l1 = int(input("Enter the index to be insert "))
    list1 = [54, 44, 27, 79, 91, 41]
    print('original list = ', list1)
    if l > len(list1):
        a= None
    else:
        list1.pop(l)
    list1.insert(l1, n)
    list1.append(None)
    print('After editing', list1)
    return a


n = int(input("Enter the number to be insert"))
print(edit_list(n))


# ========================================

# ER4
def count():
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    res = dict()
    for i in sample_list:
        res[i] = sample_list.count(i)
    print(res)


count()


# ===========================================

# ER5
def create_set():
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64, 8, 88]
    res = set(zip(first_list, second_list))
    print(res)


create_set()


# ================================================

# ER6

def set_operation():
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 43, 48}
    set3 = first_set.intersection(second_set)
    first_set.difference_update(second_set)
    print("Intersection is", set3)
    print(first_set)


set_operation()

# ===========================================
# ER7
# def delete_set():
#     first_set = {27, 43, 34}
#     second_set = {34, 93, 22, 27, 43, 53, 48}
#     a = (first_set.issubset(second_set))
#     b = (second_set.issubset(first_set))
#     c = (first_set.issuperset(second_set))
#     d = (second_set.issuperset(first_set))
#     if a:
#         print("First set is subset of second set -", a)
#         first_set.clear()
#
#     elif b:
#         print("Second set is subset of second set -", b)
#         second_set.clear()
#
#     if c:
#         print("First set is superset of second set -", c)
#
#     elif d:
#         print("Second set is superset of second set -", d)
#
#     print(first_set)
#     print(second_set)
#
#
# delete_set()
#
#
# # ==========================================
#
# # ER8
# def check_elements():
#     roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
#     sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
#     for r in roll_number.copy():
#         if r not in sample_dict.values():
#             roll_number.remove(r)
#     print(roll_number)
#
#
# check_elements()
#
#
# # ============================================
#
# # ER9
# def create_unqie_list():
#     speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#     numbers = []
#     for value in speed.values():
#         if value not in numbers:
#             numbers.append(value)
#     print(numbers)
#
#
# create_unqie_list()
#
#
# # ==================================================
#
# # ER10
# def create_tuple():
#     sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
#     sample_list = set(sample_list)
#     t = tuple(sample_list)
#     print(t)
#     print(min(sample_list))
#     print(max(sample_list))
#
#
# create_tuple()
