n = int(input())
for j in range(n * 2):

    for i in range(n * n) :
        if i == (n*n // 2):
            print(chr(95+i),end = "")
        else:
            print("-",end = "")
