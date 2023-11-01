def divide_by(a, b):
    return a / b


try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, " We can not divide by zerio")
except Exception as e:
    print(e, "Something went wrong")