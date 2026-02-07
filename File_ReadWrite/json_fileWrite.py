import json

user_data={"name":"dharmishtha","age":30,"c_no":23456}
user_data1=[
    {"name":"tttt","age":22},
    {"name":"sssss","age":33}
]
with open("user_data.json","w") as file:
    json.dump(user_data1,file,indent=8)
print("Data inserted into json file")
