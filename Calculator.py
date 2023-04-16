#Calculator


while True:
    num1=int(input("Enter the First Number:- "))
    num2=int(input("Enter the Second Number:- "))
    op=input("Enter the operator[(+ for addition), (- for subtraction), (* for multiplication), (/ for division)]:- ")

    if op == "+":
        print(num1+num2)
    
    elif op == "-":
        print(num1-num2)
    
    elif op == "*":
        print(num1*num2)

    elif op == "/":
        print(num1/num2)

    else:
        print("Invalid Input!!")

    print("\n")
