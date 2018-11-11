# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/contest/1065/problem/B
# Language: Python 2.7

import math
n, m = map(int, raw_input().split(' '))
print max(0, n - min(n, m*2)), max(0, n - int((1+(1+8*m)**0.5+1)/2) if m > 0 else n)