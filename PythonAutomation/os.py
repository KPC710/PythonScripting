import os

cwd = os.getcwd()
print(cwd)


def current_path():
    print("current working directory")
    print(os.getcwd())
    print()
current_path()

os.chdir('../')

current_path()

directory = "chethan"
parent_dir = "/Users/ztlm16/PycharmProjects/pythonProject"
path = os.path.join(parent_dir,directory)
# os.mkdir(path)
print(path)

# print(os.listdir(path))

location = "/Users/ztlm16/PycharmProjects/pythonProject"
path1 = os.path.join(parent_dir, directory)
os.rmdir(path1)
# print(path1)
