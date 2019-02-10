n = int(input())#введите количество элементов set
s = set(map(int, input().split()))#введите элемент set
for i in range(int(input())):
    eval("s.{0}({1})".format(*input().split()+[""]))

print (sum(s))