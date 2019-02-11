#https://www.hackerrank.com/challenges/designer-door-mat/problem
n,m = map(int,input().split())
patern = [(".|."*(2*i+1)).center(m,"-") for i in range(n//2)]
print("\n".join(patern + ["WELCOME".center(m,"-")] +patern[::-1]))