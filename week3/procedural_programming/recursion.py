def find_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)
    
print(find_factorial_recursive(1))

#Otherewise to find the factorial of the integer n to be (5) which is 120

# 5 * (factorial (4))
# 5 * (4 * (factorial (3)))
# 5 * (4 * (3 * (factorial (2))))
# 5 * (4 * (3 * (2 * (factorial (1)))))
# 5 * (4 * (3 * (2 * (1 * (facotiral (0))))))
# 5 * (4 * (3 * (2 * (1 * 1))))
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
