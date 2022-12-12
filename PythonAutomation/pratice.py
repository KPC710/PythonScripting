num1 = 20
num2 = 10

if num1 < num2:
    print("before swap", num1,num2)

    num2 = num1 + num2 # 30
    num1 = num2 - num1 # 20
    num2 = num2 - num1 #  10

    print(" after swap ", num1, num2)

else:

    print("before swap ", num1,num2)

    num1 = num1 + num2 # 30
    num2 = num1 - num2 #20
    num1 = num1 - num2 #10

    print("after swap " , num1, num2)


