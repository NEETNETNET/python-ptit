import math
def isPrime(n):
    if n < 2: 
        return 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1


def check(s):
    for i in range(len(s)):
        if (isPrime(i) and not isPrime(int(s[i]))) or (not isPrime(i) and isPrime(int(s[i]))):
            return 'NO'
    return 'YES'
for i in range(int(input())):
	print(check(input()))