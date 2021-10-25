def num_way(n: int):
    if n == 0 or n == 1:
        return 1
    st = [0]*(n+1)
    st[0],st[1]=1,1
    for i in range(2,n):
        st[i]=st[i-1]+st[i-2]
    return st[n]


# def f(x:float)->int:
#     return int(x)
# print(f.__annotations__['x'])
# a=f(9.0)
# print(a)