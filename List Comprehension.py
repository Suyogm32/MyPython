import random

sentence='This is my home and you cant take it away from me'

def is_consonant(letter):
    vowels='aeiou'
    return letter.isalpha() and letter.lower() not in vowels

# print(is_consonant('a'))
# def is_exists(lst,letter):
#     return  letter not in lst
consonants=[i for i in sentence if is_consonant(i)  ]

print(consonants)
lst=['vinayak','suyog','om','yash']
random.shuffle(lst)
print(lst)

#simple project

n=int(input("Enter the no of days that you want to record the temperature:-\n"))
mylist=[]
for i in range(n):
    temp=int(input(f"Enter the {i+1} day temperature;- "))
    mylist.append(temp)

avg_temp=float(sum(mylist)/n)
print(f"Avarage temp is {avg_temp}")
ct=0
for temp in mylist:
    if temp>avg_temp:
        ct+=1
print(f"There are {ct} days having more than avarage temperature.")
