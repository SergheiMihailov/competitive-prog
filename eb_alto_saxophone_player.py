# Repo: https://github.com/SergheiMihailov/competitive-prog
# Link to problem: https://open.kattis.com/problems/saxophone
# Language: Python 2.7

fings_to_notes = {}
notes_1 = 'cdefgab'
for i in range(len(notes_1)):
    fings_to_notes[notes_1[i]] = [2,3,4,7,8,9,10][:len(notes_1) - i]
    
notes_2 = notes_1.upper()
for i in range(len(notes_2)):
    fings_to_notes[notes_2[i]] = [1,2,3,4,7,8,9][:len(notes_1) + 1 - i]

fings_to_notes['C'] = [3]

n = int(raw_input())

melods = [] 
for i in range(n):
    melods.append(raw_input())


for mel in melods:
    fings_presses = []
    last_pressed = []

    for i in range(1, 11):
        fings_presses.append(0)
        last_pressed.append(False)
    
    for char in mel:
        for digit in fings_to_notes[char]:
            if not last_pressed[digit-1]:
                fings_presses[digit-1] += 1
        for digit in range(10):
            last_pressed[digit-1] = False
            
        for digit in fings_to_notes[char]:
            last_pressed[digit-1] = True
    
    s = ""
    for i in fings_presses:
        s += str(i)
        s += ' '
    print s