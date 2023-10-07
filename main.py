import math


class Animal:
    _weigh = 4
    def __init__(self):
        print("Animal object created")
    def move(self):
        print("Animal moved")

    def get_weight(self):
        return self._weigh

    def set_weigh(self, weigh):
        if weigh>0:
            self._weigh=weigh
        else:
            print("Ne pravilnoe znachenie vesa")
    def __del__(self):
        print("Animal object deleted!")



class Dog(Animal):
    def __init__(self):
        print("Dog object created")
    def voice(self):
        print("Gav gav gav!!!")
    def __del__(self):
        print("Dog object deleted")


class Cat(Animal):
    def __init__(self):
        print("Cat object created")
    def voice(self):
        print("Meov meov meov!!!")
    def __del__(self):
        print("Cat object deleted")


def speak( a):
 a.voice()


d=Dog()
c=Cat()
speak(d)
speak(c)

def div(a, b):
    try:
        return a/b
    except ArithmeticError:
        print("Zero division error")
    except TypeError:
        print("Type errro")

    finally:
        print("Chtoto delat vne zavisimosti ot rezultata!")

dr=div(4, 0)
print("Div result: ", dr)





# d.move()
# d._weigh=43
#
# d.voice()

# b = Animal()
# b.move()
# b.set_weigh(-12)
# print ("Animal weight is: ",b.get_weight())



# int a=7
#
# def is_simple(a):
#     for i in range(2, math.isqrt(a)+1):
#         if a%i==0:
#             return False
#     return True
#
#
# for i in range(1,100):
#     if is_simple(i):
#         print(i, "-prostoe chislo")

# if is_simple(127):
#     print("Chislo prostoe")
# else:
#     print("Chislo sostavnoe")


# def my_max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#
#
#
# c=my_max(3,12)
# print(c)


# ar=[5,"Hello",5,6,3,12]
# print(ar[4])
#

# a=15
# b=7
# for i in range(3,100, 3):
#     print(i)
# if i%3==0:
#     print(i)

# if a>b:
#     max=a
# else:
#     max=b
# print("Max: ",max)


# c=a+b
# print("Summa: ", c)
