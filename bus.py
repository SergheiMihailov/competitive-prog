# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/bus
# Language: Python 2.7

t = int(raw_input())
for test in range(t):
    k = int(raw_input())
    n_people = 0
    for i in range(k):
        n_people += 0.5
        n_people *= 2
    print int(n_people)