import itertools
k,m =map(int,input().split())
n = (list(map(int,input().split()))[1:] for _ in range(k))
res = map(lambda x:sum(i**2 for i in x)%m,itertools.product(*n))
print(max(res))
