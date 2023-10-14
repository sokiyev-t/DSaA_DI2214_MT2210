from student import Student, Gender
import array

st = [
    Student("Umar", "Mansurov", 12, Gender.MAN),
    Student("Samad", "Qodirov", 13, Gender.MAN),
    Student("Madina", "Shamsiyeva", 14, Gender.WOMAN),
    Student("Maftuna", "Vosiyeva", 15, Gender.WOMAN),
    Student("Voxid1", "Qobilov", 16, Gender.MAN),
    Student("Voxid2", "Qobilov", 17, Gender.MAN),
    Student("Voxid3", "Qobilov", 18, Gender.MAN),
    Student("Voxid4", "Qobilov", 19, Gender.MAN),
    Student("Voxid5", "Qobilov", 20, Gender.MAN),
    Student("Voxid6", "Qobilov", 21, Gender.MAN),
    Student("Voxid7", "Qobilov", 22, Gender.MAN),
    Student("Voxid8", "Qobilov", 23, Gender.MAN),
    Student("Voxid9", "Qobilov", 24, Gender.MAN),
    Student("Voxid10", "Qobilov", 26, Gender.MAN),
    Student("Voxid11", "Qobilov", 27, Gender.MAN),
    Student("Voxid12", "Qobilov", 30, Gender.MAN),
]
# a=12
# b=24
# temp=a
# a=b
# b=temp
#
# print(a,b)


a = [3, 2, 6, 1, 94, 23, 6, 13]

def buble_sort(a):
    for i in range(0, len(a)-1):
        print("----------------")
        for j in range(i+1, len(a)):
            print(a)
            if a[j]>a[i]:
                a[j], a[i]=a[i], a[j]
    return a
ar=buble_sort(a)
print("Result: \n", ar)

#
# # a=[3,2,6,1,94,23,6,13]
# c = array.array('i', [11, 25, 3, 4, 5])
# a = array.array('i', [1, 2, 3, 4, 5])
# b = array.array('i', [14, 25, 3, 4, 5])
# address=id(b)
# print("Address: B", address)
# address=id(a)
# print("Address: A", address)
# for i in range(0, len(a)):
#     print(id(a[i]),'-',a[i])
#
#
# n=int(input())
# for i in range(0,n):
#     a.append(i+100)
#
# print("Print again\n");
# print("Address: ", address)
# for i in range(0, 3):
#     print(id(a[i]), '-', a[i])
#
