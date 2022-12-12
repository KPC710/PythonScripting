# # #
import  platform
import os
# # import boto3
# # #
# # # print(dir(platform))
# # #
# # # print(platform.python_version())
# # # print(platform.architecture())
print(platform.platform())


# # #
# #
# # import os
# # import sys
# # path=input("Enter your directory path: ")
# # if os.path.exists(path):
# # 	df_l=os.listdir(path)
# # else:
# # 	print("please provide valid path")
# # 	sys.exit()
# #
# #
# # list_of_files_dir=os.listdir(path)
# # print("all files and dirs: ",list_of_files_dir)
# # for each_file_or_dir in list_of_files_dir:
# # 	f_d_p=os.path.join(path,each_file_or_dir)
# # 	if os.path.isfile(f_d_p):
# # 		print(f'{f_d_p} is a file')
# # 	else:
# # 		print(f'{f_d_p} is a directory')
#
#
# # my_list = [1, 4, 4, 6, 8, 10, 12,13]
# # for each_value in my_list:
# #     rem = each_value%2
# #     if rem == 0:
# #         print(f'{each_value} is even')
# #     else:
# #         print(f'{each_value} is odd')
#
#
# char1 = input("enter the char: ")
# index = 0
# for each_value in char1:
#     print(f'{each_value} ---> {index}')
#     index = index+ 1
#
# def myCode():
#     x = 60
#     print(f'hello{x}')
#     return None
# def muCode1():
#     print("chethan")
#     return None
# def myCode3():
#     global x
#     x = 10
#     print("welcome")
#     myCode()
#     return None
#
# myCode()
# myCode3()

# !/bin/python3
import os


class Tomcat(object):

    def get_home_conf_file(self, server_xml):
        self.t_home = os.path.dirname(os.path.dirname(server_xml))
        self.conf_file = server_xml
        return None

    def display_details(self):
        print("Tomcat home is: ", self.t_home)
        print("Tomcat conf file is: ", self.conf_file)
        return None


def get_all_tomcats():
    list_of_config_files = []
    for r, d, f in os.walk("/"):
        for each_file in f:
            if each_file == 'server.xml':
                list_of_config_files.append(os.path.join(r, each_file))
    return list_of_config_files


def main():
    print("Finding list of tomcats...")
    list_of_tomcats = get_all_tomcats()
    tomcat_objects = []
    for each_file in list_of_tomcats:
        tomcat_object = Tomcat()
        tomcat_object.get_home_conf_file(each_file)
        tomcat_objects.append(tomcat_object)
    for each_ob in tomcat_objects:
        each_ob.display_details()

    return None


if __name__ == '__main__':
    main()


