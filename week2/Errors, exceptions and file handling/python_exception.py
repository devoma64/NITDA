def divide_by(a, b):
    return (a / b)
    
try:
    print(divide_by(8,0))
except Exception as e:
    print(e)