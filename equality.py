# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/gym/231921/problem/A1
# Language: Python 2.7

n, k = map(int, raw_input().split(' '))
s = raw_input()
d = {}

for i in range(ord('A'), ord('A') + k):
    d[i] = 0

for i in s:
    d[ord(i)] += 1

if d.keys() < n:
    print 0
elif n == 0:
    print 0
else:
    minimum = 99999999
    for i in d.keys():
        minimum = min(minimum, d[i])
    
    print minimum*k