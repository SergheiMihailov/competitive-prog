# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/whatdoesthefoxsay
# Language: Python 2.7

n_tests = int(raw_input())

for t in range(n_tests):
    sounds = raw_input()
    sounds = sounds.split(' ')
    not_fox = []
    fox = []
    s = ''
    
    while s != "what does the fox say?":
        s = raw_input()
        l = s.split(' ')
        for i in l[2:]:
            not_fox.append(i)
            

            
    for i in sounds:
        if i not in not_fox:
             fox.append(i)
    
    print ' '.join(fox)