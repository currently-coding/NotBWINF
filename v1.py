# STEPS
#
# create map to represent jump distances
#
# ä ö ü ß
#
# read file
FILENAME = "hopsen1.txt"


with open(FILENAME, 'r') as f:
    lines = f.read()
f.close()

stripped_text = ''.join([i.lower() for i in lines if i.isalpha()])

end = len(stripped_text)

def distance(text, score):
    return ctoi(text[score])

def ctoi(char):
    return ord(char)-96


score_a = 0
score_b = 1
has_ended = False
print(end)

# first var to be greater than len wins
while not has_ended:
    print('B:', score_a, score_b)
    score_a += distance(stripped_text, score_a)

    if score_a > end:
        has_ended = True
        break
    score_b += distance(stripped_text, score_b)
    if score_b > end:
        has_ended = True
        break
    print('A:', score_a, score_b)
winner = 'a' if score_a > score_b else 'b'
print(winner)
