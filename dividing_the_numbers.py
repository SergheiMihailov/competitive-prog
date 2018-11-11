# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: http://codeforces.com/gym/231906/problem/B
# Language: Python 2.7

import math

n = int(raw_input())
half_sum = (n+1)*n/2.0/2
group_1 = []
diff = half_sum

for i in reversed(range(1, n+1)):
    if i <= diff:
        group_1.append(str(i))
        diff -= i

print int(math.ceil(diff))
print len(group_1), ' '.join(group_1)