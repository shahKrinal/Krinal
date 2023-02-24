# # ER1
# import simplejson as json
#
#
# def create_json():
#     data = {"key1": "value1", "key2": "value2"}
#     json_data = json.dumps(data)
#     return json_data
#
#
# print(create_json())
#
#
# # ======================================
#
# # ER2
# def access_value():
#     sample_json = """{"key1": "value1", "key2": "value2"}"""
#     json_data = json.loads(sample_json)
#     return json_data.get('key2')
#
#
# print(access_value())
#
#
# # ========================================
#
# # ER3
# def json_format():
#     sampleJson = {"key1": "value1", "key2": "value2"}
#     json_data = json.dumps(sampleJson, indent=2, separators=(',', '='))
#     return json_data
#
#
# print(json_format())
#
#
# # ======================================================
#
# # ER4
# # def write_file():
# #     sample_json = {"id": 1, "name": "value2", "age": 29}
# #     with open('json_data.json', "w") as f:
# #         json.dump({'data': [sample_json]}, f, indent=4, separators=(',', ': '), sort_keys=True)
# #
# #
# # write_file()
#
#
# # =====================================================
#
# # ER5
# def access_salary():
#     sample_json = """{
#        "company":{
#           "employee":{
#              "name":"emma",
#              "payble":{
#                 "salary":7000,
#                 "bonus":800
#              }
#           }
#        }
#     }"""
#
#     print(sample_json)
#     json_data = json.loads(sample_json)
#     data = json_data.get('company').get('employee').get('payble').get('salary')
#     return data
#
#
# print('Salary is ', access_salary())
#
#
# # ==============================================================
# # ER6
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
#
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# json_data = json.dumps(vehicle.__dict__)
# print(json_data)
#
#
# # =============================================================
# # ER7
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
#     def display(obj):
#         return Vehicle(obj['name'], obj['engine'], obj['price'])
#
#     vehicle = '{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}'
#     vehicle_obj = json.loads(vehicle, object_hook=display)
#     print(vehicle_obj.name, vehicle_obj.engine, vehicle_obj.price)
#
#
# # ===================================================================
# # ER8
# def validatejson(jsondata):
#     try:
#         json.loads(jsondata)
#     except ValueError:
#         return False
#     return True
#
#
# json_data = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payble":{
#             "salary":7000
#             "bonus":800
#          }
#       }
#    }
# }"""
# print(validatejson(json_data))
#
#
# # =================================================
# # ER9
# def parsing():
#     data = [
#         {
#             "id": 1,
#             "name": "name1",
#             "color": [
#                 "red",
#                 "green"
#             ]
#         },
#         {
#             "id": 2,
#             "name": "name2",
#             "color": [
#                 "pink",
#                 "yellow"
#             ]
#         }
#     ]
#     val = [i.get('name') for i in data]
#     print(val)
#
#
# parsing()
#
#
# def read_file():
#     with open("json_data.json", 'r') as f:
#         data = json.load(f)
#         print(data)
#
#
# read_file()
