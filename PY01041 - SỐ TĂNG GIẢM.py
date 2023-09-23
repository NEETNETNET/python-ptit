def check(s):
    if len(s) < 3:
        return 'NO'
    inc = True
    for i in range(1, len(s)):
        if inc and s[i] <= s[i - 1]:
            inc = False
        elif not inc and s[i] >= s[i - 1]:
            return 'NO'
    return 'YES'


for _ in range(int(input())):
    s = input()
    print(check(s))