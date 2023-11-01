# file = open('test.txt', mode='r')
# data = file.readline()
# print(data)


# now creating a function to read the same file


def read_file(file_name):
    
    try:
        
        with open(file_name, mode='r') as file:
            file_contents = file.readline()
            return file_contents
        
    except Exception as e:
        print(e, 'File not found')
    
file_name = "test.txt"
file_content = read_file(file_name)
print(file_content)