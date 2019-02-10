_,L = input(), set(map(int,input().split()))

def set_mutetions(L):
    command = input().split()[0]
    new_set = set(map(int,input().split()))
    if command == "intersection_update":
        L.intersection_update(new_set)
    if command == "update":
        L.update(new_set)
    if command == "symmetric_difference_update":
        L.symmetric_difference_update(new_set)
    if command == "difference_update":
        L.difference_update(new_set)

for i in range(int(input())):
    set_mutetions(L)
print(sum(L))