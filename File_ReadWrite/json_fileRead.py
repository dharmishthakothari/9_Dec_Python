import json
user_data=[]
with open("user_data.json","r") as file:
    user_data=json.load(file)

print(type(user_data))