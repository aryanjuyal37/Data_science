from typing import List

def  num_way(n: int,X: List[int]):
    if n==0 or n==1:
        return 1
    st = [0]*(n+1)
    st[0]=1
    for i in range(1,n):
        for j in X:
            if i - j >= 0:
                st[i]+=st[i-j]
    return st[n]