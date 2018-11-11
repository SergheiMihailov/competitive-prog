# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/contest/1058/problem/C
# Language: Python 2.7

def dfs(sum_lucky, a):
    for i in range(len(a)+1):
        if sum(a[:i]) == sum_lucky:
            if len(a[i:]) < 1:
                return True
            elif dfs(sum_lucky, a[i:]):
                return True
    return False

def check_lucky(a):
    for i in range(1, len(a)):
        if dfs(sum(a[:i]), a[i:]):
            return True
    return False

n = int(raw_input())
a = list(map(int, str(int(raw_input()))))

if sum(a) == 0 or check_lucky(a):
    print "YES"
else:
    print "NO"
