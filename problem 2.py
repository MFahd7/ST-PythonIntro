grade = int(input("please enter your grade: "))

if grade > 85:
    print('excellance!!')
elif grade > 75:
    print('very good !')
elif grade > 65:
    print('good')
elif grade > 60:
    print('u passed')
else:
    print('failed')

# ################################################ 2
temp = int(input('whats the temperature? '))

if temp <= 0:
    print('its cold :(')
elif temp <= 25:
    print('normal :|')
else:
    print('hot !!')

# ################################################ 3
str = 'mohammed fahd'
vowel = 0

for i in str:
    if(i == 'a' or i == 'i' or i == 'o' or i == 'u' or i == 'e'):
        vowel += 1
print('no. of vowels are ', vowel)

################################################## 4
lis = []
for i in range(5):
    lis.append(input('enter a datatype '))

lis.sort()
print(lis)
lis.sort(reverse= True)
print(lis)

################################################## 5
num = int(input('please enter a number: '))
if num % 3 == 0 and num % 5 == 0:
    print('fizzBuzz')
elif num % 5 == 0:
    print("buzz")
elif num % 3 == 0:
    print('fizz')

################################################## 6
str2 = input('write a string of character: ')
str1 =""

for i in str2:
        str1 = i + str1
print(str1)