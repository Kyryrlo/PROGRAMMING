import json

json_data = '{"nimi":"Kyrylo Chernykh","age":"18","onPrillid":"True"}'
data_ = json.loads(json_data)
for id_, data in enumerate(data_):
    print(id_, ": ", data)
for key, value in data_.items():
    print(key, ": ", value)
    
data_1 = json.dumps(json_data)
print(data_1)