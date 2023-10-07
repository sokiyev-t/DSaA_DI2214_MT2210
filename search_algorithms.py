from student import Student, Gender

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

#fasdfasdf

def binary_search(val, st):
    l=0
    h=len(st)-1
    while l<=h:
        mid=(h+l)//2
        guess=st[mid]
        if guess.age==val:
            return mid
        elif guess.age>val:
            h=mid-1
        else:
            l=mid+1
    return None

ind=binary_search(26, st)
if ind:
    st[ind].print()
else:
    print("Student not found!")

# i=1
# for s in st:
#     print(f"Check: {i}")
#     i+=1
#     if s.age==30:
#         s.print();
#         break

# for i in range(0,len(st)):
#     if st[i].age==18:
#         st[i].print()
#         break



