def read_file(file_name):

    try:
        
        with open(file_name, mode='r') as file:
            file_content = file.readline()
            print(file_content)
    except Exception as e:
        print(e)
read_file('test.txt')