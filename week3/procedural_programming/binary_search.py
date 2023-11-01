def find_number_log(target):
    iterations = 0
    x = range(100)
    left = 0
    right = len(x) -1
    
    while left <= right:
        iterations += 1
        middle = (left + right) // 2
        isNumber = x[middle]      
    
    if target == isNumber:
                print('Iterations', iterations)
                return middle
    elif target < isNumber:
                    right = middle -1
    else:
                    left = middle + 1
    return -1
print(find_number_log(96))