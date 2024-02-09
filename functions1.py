#problem 1
def grams(n):
    ounces = 28.3495231 * n
    return ounces
n = float(input())
ounces = grams(n)
print(ounces)

#problem 2
def far(F):
    cel = (5/9) * (F-32)
    return cel
F = float(input())
cel = int(far(F))
print(cel)

#problem 3
def solve(numheads, numlegs): #chikens - 2 legs; rabbits - 4 legs; overall 35 heads and 94 legs 
    for c in range(numheads + 1):
        r = numheads - c
        if c*2 + r*4 == numlegs:
            return c, r
numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)
print(*solution)

#problem 4
import math
def filter_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

list_1 = [int(i) for i in input().split()]
list_2=[]
for x in list_1:
    if(filter_prime(x)==True):
        list_2.append(x)
print(list_2)

#problem 5
def toString(List): 
    return ''.join(List) # join elements from list -> string
def permute(a, l, r): 
    if l == r: 
        print (toString(a)) 
    else: 
        for i in range(l, r + 1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l + 1, r) 
            a[l], a[i] = a[i], a[l] 
 
string = input()
n = len(string) 
a = list(string) 
permute(a, 0, n-1)

#problem 6
def reverse_words(sen):
    words = sen.split() #sentence -> words(separating if space)
    reversed_sentence = ' '.join(reversed(words)) #join() used to join these rev wrds into str, sep by a space.

    return reversed_sentence
input_sentence = input()
reversed_sentence = reverse_words(input_sentence)
print(reversed_sentence)

#problem 7
def has_33(nums):
    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
list = [int(i) for i in input().split()]
if has_33(list) == True:
    print("True")
else:
    print("False")

#problem 8
def spy_game(nums):
    for i in range(0, len(nums)):
        if nums[i] == 0:
            for j in range(i+1, len(nums)):
                if  nums[j] == 0:
                    for k in range(i+2, len(nums)):
                        if  nums[k] == 7:
                            return True
                    return False
list = [int(i) for i in input().split()]
if spy_game(list) == True:
    print("True")
else:
    print("False")

#problem 9
import math
def  volumef(r):
    volume = (4/3) * math.pi * pow(r, 3)
    return volume
r = int(input())
print(volumef(r))

#problem 10
def unique(elmnts):
    mt_list = []
    for i in elmnts:
        if i not in mt_list:
            mt_list.append(i)
    print(mt_list)
list = [int(i) for i in input().split()]
unique(list)

#problem 11
def palindrome(str):
    str2 = str[::-1]
    if str2 == str:
        return True
    return False
str = input()
if palindrome(str) == True:
    print("Yes, palindrome")
else:
    print("No")

#problem 12
def histogram(nums):
    for i in nums:
        print('*'*i)
list_1 = [int(i) for i in input().split()]
histogram(list_1)
def histogram(nums):
    for i in nums:
        print('*'*i)
list_1 = [int(i) for i in input().split()]
histogram(list_1)

#problem 13
import random
name = input("Hello! What is your name? ")
number = random.randint(1, 20)
print("Well, " + name + ", I am thinking of a number between 1 and 20."'\n')
guessestaken = 0
while guessestaken < 100:
    guess = input("Take a guess. ")
    guess = int(guess)
    guessestaken = guessestaken + 1
    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        print("Good job, " + name + "! You guessed my number in " + str(guessestaken) + " guesses!")
        break