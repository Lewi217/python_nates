def grade(m):
    if (m <= 100 )& (m >= 70):
        print("A")
    elif(m < 70 ) & (m >= 60):
        print("B")
    elif(m < 60 ) & (m >= 50):
        print("C")
    elif(m < 50 ) & (m >= 40):
        print("D")
    elif(m < 40 ) & (m >= 0):
        print("E")
    else:
        print("I")
grade(7)

marks=[10,7,77,800,-100,20]
for mk in marks:
    if mk==77:
        continue
    grade(mk)
    print(len(marks))
    for i in range(len(marks)):
        if i==3:
            break
        if i==3:
            continue
        grade(marks[i])                        