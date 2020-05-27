marks = {}
n = int(input())
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    marks[name] = scores
specific = input()
m = list(marks[specific])
average = sum(m) / len(m)
print("{:.2f}".format(average))