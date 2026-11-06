#Question : WAP to print twin prime numbers between 1 to N.

#Answer :
import math 
N = int(input("Enter a number : "))
for i in range(2, N - 1):
    def is_prime(num):
        if num < 2: return False
        for k in range(2, int(math.sqrt(num)) + 1):
            if num % k == 0: return False
        return True
    if is_prime(i) and is_prime(i + 2):
        print(f"({i}, {i+2})")

#Output:
'''Enter a number : 20
(3, 5)
(5, 7)
(11, 13)
(17, 19)'''