# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/gym/231906/problem/A
# Language: Python 2.7

def solve(lstring, copies):
    if len(lstring) < 1:
        return 0
    for i in reversed(range(1, len(lstring)/2+1)):
        if copies:
            if lstring[:i] == lstring[:i*2][i:]:
                return 1 + solve(lstring[:i], False) + solve(lstring[i*2:], False)
    return 1 + solve(lstring[1:], False)

raw_input()
s = list(raw_input())

print solve(s, True)