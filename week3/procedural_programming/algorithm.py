# Algorithm for a palindrome

def isPalindrom(str):
    
    startIndex = 0
    endIndex = len(str) -1
    
    for x in str:
        
        if str[startIndex] != str[endIndex]:
            return False
        
        return True
output = isPalindrom("racecar")
print(output)
    # startIndex = 0
    # endIndex = len(str) -1
    
#     for x in str:
#         if str[startIndex] != str[endIndex]:
#             return False
#     return True
# output = isPalindrom("racecar")
# print(output)