while True:
    try:
        print("This is an adding machine")
        first_number = int(input("what is the first number you want to add"))
        second_number = int(input("what is the second number you want to add"))
        sum = first_number + second_number
        print("the sumof your two numbers is", sum)
        break
    except:
        print("your input is not correct")