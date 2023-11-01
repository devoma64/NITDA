

my_global = 10

# def fn1():
#     local_v = 5
#     print("Access to Global", my_global)
#     print(local_v)
# fn1()
# print("access to global v ", my_global)


def fn1():
    enclosed_v = 8
    
    
    def fn2():
        local_v = 5
        print('Access to Gobal', my_global)
        print('Access to local_v', local_v)
        print('Access to enclosed_v', enclosed_v)
    fn2()
fn1()