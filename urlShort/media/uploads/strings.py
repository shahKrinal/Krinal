# ER1
def display_str():
    str1 = "James"
    str2 = str1[slice(0, 5, 2)]
    print(str2)


display_str()


# ==========================

# ER2
def add_string():
    s1 = "Ault"
    s2 = "Kelly"
    mid = len(s1) // 2
    s1 = s1[:mid] + s2 + s1[mid:]
    print(s1)


add_string()


# ===================================
def create_string():
    s1 = "America"
    s2 = "Japan"


# ER3
# def join_str(str1, str2):
#     new_string = str1[0] + str2[0]
#
#     mid1 = len(str1) // 2
#     mid2 = len(str2) // 2
#     new_string = new_string + str1[mid1] + str2[mid2]
#
#     new_string = new_string + str1[-1] + str2[-1]
#     print(new_string)
#
#
# str1 = (input("Enter fisrt string"))
# str2 = (input("Enter second string"))
# join_str('apple', 'mango')

# ==============================================

# ER4
# def create_str(str1):
#     low_str = ""
#     upper_str = ""
#
#     for i in str1:
#         if i.islower():
#             low_str = low_str + i
#         else:
#             upper_str = upper_str + i
#
#     new_str = low_str + upper_str
#     print(new_str)
#
#
# word = (input("Enter the string"))
# create_str(word)


# ====================================

# ER5
def count():
    str1 = "P@#yn26at^&i5ve"
    c_digit = 0
    c_alpha = 0
    c_symbol = 0
    for i in str1:
        if i.isalpha():
            c_alpha = c_alpha + 1

        elif i.isdigit():
            c_digit = c_digit + 1

        else:
            c_symbol = c_symbol + 1

    print("Total digits are ", c_digit)
    print("Total letters are ", c_alpha)
    print("Total symbols are ", c_symbol)


count()


# =================================
# ER6
def mixed_str():
    s1 = "Abc"
    s2 = "Xyz"
    s3 = s1[0] + s2[-1]
    s4 = s1[1] + s2[1]
    s5 = s1[2] + s2[0]
    new_str = s3 + s4 + s5
    print(new_str)


mixed_str()


# ======================================

# ER7
def check(s1, s2):
    if s1.find(s2) == -1:
        print("NO")
    else:
        print("YES")


# driver code
string = "PYnative"
sub_str = "Yn"
check(string, sub_str)


# ========================================

# ER8
def count_word():
    str1 = "Welcome to USA. usa awesome, isn't it?"
    print(str1.lower().count('usa'))


count_word()


# =====================================
# ER9
def calculate():
    str1 = "PYnative29@#8496"
    sum = 0
    c = 0
    for n in str1:
        if n.isdigit():
            sum = sum + int(n)
            c = c + 1
    avg = sum / c
    print(sum)
    print(avg)


calculate()


# ========================================

# ER10
def char_count():
    str1 = "Apple"
    new_dict = {}
    for i in str1:
        c = str1.count(i)
        new_dict[i] = c
    print(new_dict)


char_count()


# ================================================

# ER11
def reverse_str():
    str1 = "PYnative"
    print(str1[::-1])


reverse_str()


# ===============================================

# ER12
def last_index():
    str1 = "Emma is a data scientist who knows Python. Emma works at google."
    print(str1.rfind('Emma'))


last_index()


# =============================================


# ER13
def split_string():
    str1 = "Emma - is -a - data - scientist"
    str2 = str1.split('-')
    for c in str2:
        print(c)


split_string()


# ================================================

# ER14
def remove_str():
    str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
    while "" in str_list:
        str_list.remove("")
    print(str_list)


remove_str()


# =================================================

# ER15
def remove_ss():
    import string

    str1 = '/*Jon is @developer & musician!!'

    for c in string.punctuation:
        str1 = str1.replace(c, '')

    print(str1)


remove_ss()


# ===========================================

# ER16
def remove_char():
    str1 = 'I am 25 years and 10 months old'
    str2 = (list(filter(lambda i: i.isdigit(), str1)))
    for i in str2:
        print(i, end="")


remove_char()


# ==========================================

# ER17
def find_words():
    str1 = "Emma25 is Data scientist50 and AI Expert"
    print(str1.isalnum())
    str2 = str1.split()
    str3 = []
    for i in str2:
        if any(chr.isalpha() for chr in i) and any(chr.isdigit() for chr in i):
            str3.append(i)
    print(str3)


find_words()

# ==============================

# ER18
# def replace_symbols():
#     import string
#
#     str1 = '/*Jon is @developer & musician!!'
#
#     for c in string.punctuation:
#         str1 = str1.replace(c, '#')
#
#     print(str1)
#
#
# replace_symbols()
