print("1. Addition","2. Substraction","3. Multilication" , "4. Division","5. Exit",sep="\n")
choice=int(input("Please enter choice "))
match choice:
    case 1:
        num1=int(input("Enter number 1 "))
        num2=int(input("Enter number 1 "))
        print(f"Addition is {num1+num2}")
    case 2:
        num1=int(input("Enter number 1 "))
        num2=int(input("Enter number 1 "))
        print(f"Substraction is {num1-num2}")
    case 3:
        num1=int(input("Enter number 1 "))
        num2=int(input("Enter number 1 "))
        print(f"Mulication is {num1*num2}")
    case 4:
        
        num1=int(input("Enter number 1 "))
        num2=int(input("Enter number 1 "))
        print(f"Division is {num1/num2}")
    case _ :
        print("Invalid choice")



