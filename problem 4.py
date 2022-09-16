def reverse_capitalize(str1):

    str2 = ""
    for i in str1:
        str2 = i + str2
    #str2 is reversed

    print(str2.upper())

reverse_capitalize("god")
###################################### 2

def getRemainder(num, divisor):
    print("remainder is",num - divisor * (num // divisor))

getRemainder(25,8)

###################################### 3

def invert_list(lst):
    result = [x * -1 for x in lst]
    print(result)

lis = [2,4,6,8]
invert_list(lis)
###################################### 4

import random
def rand_int(fst, lst):
    result = random.randint(fst,lst)
    print(result)

rand_int(10,20)
###################################### 5

def sum_polygon(ang):
    ang =(ang - 2) * 180
    print(ang)

sum_polygon(6)