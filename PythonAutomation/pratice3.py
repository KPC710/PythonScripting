# series 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

index=int(input("Enter the index till you want the series : "))

firstNumber=0
secondNumber=1
temp=0

print(firstNumber)
print(secondNumber)
for i in range(0, index):
    temp = firstNumber + secondNumber
    firstNumber = secondNumber
    secondNumber = temp
    print(temp)


###################################

def febonaci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return febonaci(i-2)+ febonaci(i-1)
indexRecursive = int(input("please enter the index value series: "))

if indexRecursive <=0:
    print("please enter the postive number")
else:
    for i in range(0, indexRecursive):
        print(febonaci(i))
