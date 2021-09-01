import os
# read = os.listdir("D:\\Web Development")
root = "D:\SUMMER"
def list_all(path):
    files = os.listdir(path)
    print(path)
    for file in files:
        half_path = os.path.join(path,file)
        if os.path.isdir(half_path):
            list_all(half_path)
        else:
            print("\t", file)

list_all(root)