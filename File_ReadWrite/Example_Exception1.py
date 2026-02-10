try:
    num=int(input("Enter number "))
    print(12/2)
    data={"name":"tops"}
    #print(data["age"])
except ZeroDivisionError:
     print("Number can not divide by 0")
except ValueError:
     print("Input mismatch")
except:
     print("Error in try")
finally:
     print("Have a nice day!!!!")