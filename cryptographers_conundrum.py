# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/conundrum
# Language: Python 2.7

s = raw_input()
days = 0

for i in range(len(s)):
    z = len(s) - 1 - i 
    if i % 3 == 2:
        if s[z ] == 'p' or s[z ] == 'P':
            pass
        else:
            days += 1
    elif i % 3 == 1:
        if s[z ] == 'e' or s[z ] == 'E':
            pass
        else:
            days += 1
    elif i % 3 == 0:
        if s[z ] == 'r' or s[z ] == 'R':
            pass
        else:
            days += 1
            
print days