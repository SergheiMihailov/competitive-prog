# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/contest/1031/problem/A
# Language: Python 2.7

h, w, k = map(int, raw_input().split(' '))
print sum(list(map(lambda k: (h - 2 + w - k*8)*2, range(k))))
