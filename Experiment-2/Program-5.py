#Question : WAP to enter a string and print it in reverse also print the no of vowels and consonant in it.

#Answer :
s = input("Enter a string: ")
l = s.split()
l1 = []
i = len(l) - 1
while i >= 0:
    l1.append(l[i])
    i = i - 1
output = " ".join(l1)
print(output)
vowels = 0
consonant = 0
for i in s:
    if i in 'aeiouAEIOU':
        vowels += 1
    elif i.isalpha():
        consonant += 1
print("The Vowels are:", vowels)
print("The consonants are:", consonant)

#Output:
'''Enter a string: Hello World
World Hello
The Vowels are: 3
The consonants are: 7'''