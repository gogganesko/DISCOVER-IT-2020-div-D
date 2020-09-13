from itertools import combinations

n = int(input())
ar = [int(x) for x in input().split() if int(x) <= n]

def maxsearch(m):
    if sum(m) <= n:
        return sum(m)
    maxx = 0
    for i in range(1, len(m) + 1):
        res = filter(lambda x: maxx < x <= n, map(sum,  combinations(m, i)))
        for y in res:
            if y > maxx:
                maxx = y
                if maxx == n:
                    return maxx
    return maxx
    
print(maxsearch(ar))