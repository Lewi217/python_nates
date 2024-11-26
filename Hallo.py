a = 10.12
print(type(a))
print(int(a))

import math
def hyp(x,y):
    return math.sqrt((x*x)+(y*y))
print(math.pi)
print(math.e)
print(math.hypot(3,4))
print(hyp(3,4))

import string
a = "david"; b= "kibaara"; c = a+" "+b
print(c); print(c*3); print(c[1])
print(c[ :-5])
print(c[0:8])
print ("My name is %s and weight\
       is %d kg!" % ('Zara', 21))
print(string.capwords(c))

list1 = ['physics', 'chemistry', 1997, 2000];
print(list1); del list1[2]; print(list1)
print(len(list1));
print(list1+list1);
print(list1*3);
print(min(list1[-2]));
print(max(list1[-2]));
list1[0] = "Maths"
print(list1)