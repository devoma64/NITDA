# def d():
#      animal = "elephant"
#      def e():
#           nonlocal animal
#           animal = "giraffe"
#           print("Inside nested function: " + animal)
#      print("Before calling function: " + animal)
#      e()
#      print("After nested function: " + animal)
# animal = "camel"
# d()
# print("Inside nested function: " + animal)


def d():
     animal = "elephat"
     def e():
          nonlocal animal
          animal = "giraffe"
          print("Inside nested function: " + animal)
     print("Before call function: " + animal)
     e()
     print("After nested function: " + animal)
animal = "Camel"
d()
print("Global Animal: " + animal)