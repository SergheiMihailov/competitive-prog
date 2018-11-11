# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/minimumscalar
# Language: Python 2.7

n_tests = int(raw_input())

for t in range(n_tests):
    n = int(raw_input())
    x, y = [], []
    x = raw_input().split(' ')
    y = raw_input().split(' ')
    
    for i in range(n):
        x[i], y[i] = int(x[i]), int(y[i])
    
    x.sort()
    y.sort()
    
    result = 0
    
    for i in range(n):
        result += x[i] * y[len(y) - i - 1]
    
    print ("case #"+str(t+1)+":"), result