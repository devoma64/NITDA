import random

# file = open("sample/petname.txt", 'r')

# file_content = file.read()
# file_content_list = file_content.split("\n")
# print(file_content_list)


f_name = input('Type the file name: ')

f = open(f_name)
f_content = f.read()
f_content_list = f_content.split("\n")
print(random.choice(f_content_list))


