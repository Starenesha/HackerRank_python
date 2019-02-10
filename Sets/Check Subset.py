for _ in range(int(input())):
    a,x,b,z = input(), set(input().split()),input(),set(input().split())
    print(x.issubset(z))