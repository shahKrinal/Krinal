# ER1
def create_dict():
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    result = dict(zip(keys, values))
    print(result)


create_dict()


# ================================

# ER2
def merge_dict():
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
    dict3= dict1.update(dict2)
    print(dict3)


merge_dict()


# ==================================

# ER3
def print_value():
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

    print(sampleDict['class']['student']['marks']['history'])


print_value()


# =======================================

# ER 4

def intialize_default_dict():
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    res = dict()
    for e in employees:
        res[e] = defaults
    print(res)


intialize_default_dict()


# ========================================

# ER 5
def extracting_keys():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    # Keys to extract
    keys = ["name", "salary"]

    res = dict()
    for k in keys:
        res[k] = sample_dict[k]
    print(res)


extracting_keys()


# ================================================

# ER 6
def delete_keys():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    # Keys to remove
    keys = ["name", "salary"]
    for k in keys:
        sample_dict.pop(k)
    print(sample_dict)


delete_keys()


# =======================================

# ER 7
def get_value():
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    if 200 in sample_dict.values():
        print("200 is present")
    else:
        print("200 is not present")


get_value()


# =========================================

# ER 8
def rename_key():
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    sample_dict['location'] = sample_dict.pop('city')
    print(sample_dict)


rename_key()


# =========================================
# ER 9
def get_min_value():
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }

    print(min(sample_dict.keys()))


get_min_value()


# =======================================

# ER 10
def change_value():
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }

    sample_dict['emp3']['salary'] = 8500
    print(sample_dict)


change_value()
