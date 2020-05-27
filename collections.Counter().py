from collections import Counter
x = int(input())
shoes = list(map(int, input().rstrip().split()))
n = int(input())
l = []
for i in range(n):
    shoe, price = input().split()
    l.append({ shoe : price })
income = 0
for i in range(len(l)):
    if 