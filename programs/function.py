special = 5

def get_total(a, b):
    total = a + b
    print(special)
    
    def double_it():
        double = total * 2
        print(special)
        
    double_it()
    
    return total