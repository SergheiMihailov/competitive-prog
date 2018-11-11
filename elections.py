# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/contest/1043/problem/A
# Language: Python 2.7

n = int(raw_input())
a = map(int, raw_input().split(' '))
m = max(a)

print max(int(sum(a)*2/n)+1, m)