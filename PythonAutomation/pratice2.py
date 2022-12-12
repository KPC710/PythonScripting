# def collectNumbers(totalNumbers):
#         print("Please enter", totalNumbers, "numbers:")
#         for i in range(0,totalNumbers):
#             ele = float(input())
#             myList.append(ele)
#
# # Calculates average
#
# def calculateAverage():
#     total = 0
#     for i in range(0,len(myList)):
#         total = total + myList[i]
#     return (total/totalNumbers)
#
# myList = []
#
# totalNumbers=int(input("Average of how many numbers? "))
# collectNumbers(totalNumbers) # Calling function to create a list
#
# average=calculateAverage()  # Calling function to calculate average
# print("The average is : ", average)

def collectNumber(totalNUmber):
    print(f"please enter {totalNUmber} number")
    for i in range(0, totalNUmber):
        ele = float(input())
        my_list.append(ele)

def calculateAverage():
    total = 0
    for i in range(0,len(my_list)):
        total = total + my_list[i]
    return total/totalNUmber


my_list = []
totalNUmber = int(input("enter the total average number:  "))
collectNumber(totalNUmber)
print(my_list)

average = calculateAverage()
print("the average is " , average)