# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/bank
# Language: Python 2.7

s = raw_input().split(' ')
n, t = int(s[0]), int(s[1])

people = {}

for i in range(t):
    people[i] = []

for i in range(n):
    s = raw_input().split(' ')
    people[int(s[1])].append(int(s[0]))
    
maxHeap = [0]

summ = 0
for i in range(t):
    maxHeap += people[t-1-i]
    maxHeap.sort()
    if len(maxHeap) > 0:
        summ += maxHeap[-1]
        maxHeap.pop()
    
print summ