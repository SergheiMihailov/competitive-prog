# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/unlockpattern
# Language: Python 2.7

positions = range(9)
for i in range(3):
    s = raw_input()
    s = s.split(' ')
    for j in range(3):
        positions[int(s[j]) - 1] = [i, j]

distance = 0
for i in range(len(positions)-1):
    distance += ((positions[i+1][0]-positions[i][0])**2+(positions[i+1][1] - positions[i][1])**2)**0.5
print distance