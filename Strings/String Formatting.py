#https://www.hackerrank.com/challenges/python-string-formatting/problem

n = int(input())
w = len("{0:b}".format(n))
for i in range(1,1+n):
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,width=w))