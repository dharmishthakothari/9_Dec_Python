import traceback
try:
    data={"name":"Tops"}
    num=int(input("Enter number "))
    print(data["age"])
except ValueError as e:
    print(e)
# except Exception as e:
#     print("IN EXCEPT BLOCK")
#     traceback.print_exc()
#     print(e)

    