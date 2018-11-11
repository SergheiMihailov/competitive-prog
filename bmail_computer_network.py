# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/contest/1057/problem/A
# Language: Python 2.7

n = int(raw_input())
l = map(int, raw_input().split(' '))

result = []

while (n > 1):
    result.append(str(n))
    n = l[n-2]

result.append('1')

print ' '.join(reversed(result))
