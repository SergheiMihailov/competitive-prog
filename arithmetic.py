# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/arithmetic
# Language: Python 2.7

num = int(raw_input(), 8)
s = str(hex(num))
if num < 0:
    result = s[:1]+s[3:].upper()
else:
    result = s[2:].upper()

if result[-1] == 'L':
    result = result[:(len(result)-1)]
print result