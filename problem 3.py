def Q1(length, start):
    number_list = []
    for i in range(start, length):
      print("Enter number at index", i, )
      item = int(input())
      number_list.append(item)
    print("User list is ", number_list)

def Q2():
    num = int(input('enter a num: '))
    if num % 3 == 0 and num % 5 == 0:
        print('fizzBuzz')
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0:
        print('fizz')

def Q3():

    str2 = input('write a string of character: ')
    str1 = ""

    for i in str2:
        str1 = i + str1
    print(str1)

def Q4():
    while True:
     str = input('write ur name: ')

     if str.isdigit():
        print('this is a num pls enter ur name')
     elif str == "":
        print('this is an empty string pls enter ur name')
     else:
        emal = input('write ur email: ')
        print(str + " & ur email: " + emal)
        break

def Q5(str):
    longest = str[0]
    current = str[0]
    for c in str[1:]:
        if c >= current[-1]:
            current += c
            if len(current) > len(longest):
                longest = current
        else:
            current = c
    print("Longest substring in alphabetical order is:", longest)

def Q6():
     sum = 0
     cnt = 0
     while True:
         num1 = input('enter a number: ')
         if num1 == 'done':
             break
         if num1.isdigit():
            sum += int(num1)
            cnt = cnt+1

     avg = sum / cnt
     print('sum= ', sum)
     print('count= ', cnt)
     print('average= ', avg)

def Q7():
        import random
        name = input("What is your name? ")

        words = ['rainbow', 'computer', 'science', 'programming',
                 'python', 'mathematics', 'player', 'condition',
                 'reverse', 'water', 'board', 'geeks']

        word = random.choice(words)
        print("Guess the characters")

        guesses = ''
        turns = 7

        while turns > 0:
            failed = 0

            for char in word:
                if char in guesses:
                    print(char, end=" ")
                else:
                    print("_")
                    print(char, end=" ")

                    failed += 1

            if failed == 0:

                print("You Win")
                print("The word is: ", word)
                break
            print('Please guess another alphabet')
            guess = input("guess a character:")
            guesses += guess
            if guess not in word:
                turns -= 1

#just call ur function here :)
