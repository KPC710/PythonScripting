# def duplicatesInArray():
#     my_arr = [10, 30, 40, 50, 30, 20, 20, 40]
#     print("Duplicates elements given are: ")
#     arr_len = len(my_arr)
#
#     for i in range(0, arr_len):
#         for j in range(i+1, arr_len):
#             if my_arr[i] == my_arr[j]:
#                 print(my_arr[j])
#
# duplicatesInArray()
#
# #######################
# print("#######################")
# # Finding Unique Elements in a String
# my_string = "aavvccccddddeee"
#
# # converting the string to a set
# temp_set = set(my_string)
#
# # stitching set into a string using join
# new_string = ''.join(temp_set)
#
# print(new_string)
#
# print("#######################")

def add(a ,b):
    return a+b

print(add(10,20))

print(add(10,"hello"))