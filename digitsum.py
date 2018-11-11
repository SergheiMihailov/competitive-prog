# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/digitsum
# Language: Python 2.7

t = int(raw_input())

def sum_nums(n):
    return n*(n+1)/2

def sums_outer(n):
    n = str(n)
    if len(n) <= 1:
        return sum_nums(int(n))
    else:
        return sum_nums(int(n[0])-1)*10**len(n[1:])+int(n[0])*(int(n[1:])+1)+(int(n[0]))*sums_outer(10**(len(n)-1)-1)+sums_outer(n[1:])

for test in range(t):
    a, b = raw_input().split(' ')
    a, b = int(a), int(b)
    a = max(0, a-1)
    print sums_outer(b) - sums_outer(a)