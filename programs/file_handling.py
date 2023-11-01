# opening a file in python

file = open('test.txt', mode= 'r')
data = file.readline()
print(data)
with open('test.txt', mode= 'r') as file:
    data = file.read()
    print(data)
    

try:
    
     # write using the writelines function
     
    with open("sample/newfil.txt", 'a') as file:
        file.write("\nThis is a new file")
        file.writelines("\nThis is another line to b added")
except FileExistsError as e:
    print("Error", e)
        
   
    
    