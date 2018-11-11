# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/consecutivesums
# Language: Python 2.7

import math

n_tests = int(raw_input())
for t in range(n_tests):
    n = float(raw_input())
    impossible = False
    
    i = 2
    while not impossible:
        m = n / i
        if m - i/2 < 0:
            impossible = True
            break
        if i%2 == 0:
            if (m - int(m) == 0.5):
                result = range(int(math.ceil(m-i/2)), int(math.floor(m+i/2))+1)
                break
        elif i%2 == 1:
            if (m - int(m) == 0):
                result = range(int(math.ceil(m-i/2)), int(math.floor(m+i/2))+1)
                break
        i += 1
    
    
                
    if impossible:
        print "IMPOSSIBLE"
    else:
        answer = str(int(n)) + ' = ' + str(result[0])
        for i in result[1:]:
            answer += ' + ' + str(i)
        print answer
