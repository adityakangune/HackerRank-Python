def func(s):
    s = list(s)
    i = 0
    j = len(s)
    c = 0
    for _ in range(len(s)):
        if s[::] != s[::-1]:
            if s[i] != s[j-1]:
                #s[j-1] = chr(ord(s[j-1]) - 1)
                c += 1
            i += 1
            j -= 1
    return c



n = int(input())
for d in range(n):
    s = input()
    print(func(s))