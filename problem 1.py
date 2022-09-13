username = input('please enter ur name: ')

if username.isdigit():
    username = int(username)
    print(username)
else:
    print(username, 'as a string')
##################################################################

print('your name contains',len(username) , 'letters')
##################################################################
print('o appears ' ,username.count('o'))

##################################################################

if len(username) >= 7:
    print('the 6th letter is', username[6])
else:
    print('there is no letter at index 6')
##################################################################

pi = 3.14
rad = input('enter the radius of the circle? ')
print('area= ', pi * int(rad) ** 2)
print('circumference= ', 2 * pi * int(rad))
##################################################################

height = int(input('enter the height of the rectangle? '))
length = int(input('enter the length of the rectangle? '))
print('area= ',length * height )
print('circumference',2 * (length + height) )
##################################################################

fn = input('enter ur first name: ')
ln = input('enter ur last name: ')
fullname = 'your fullname: {first} {last}'
print(fullname.format(first= fn, last= ln))