word = ('pqqbd')

for i in word:
    if word[i] == 'p':
        word[i]  == 'q'
    elif word[i] == 'q':
        word[i] == 'p'
    elif word[i] == 'b':
        word[i] == 'd'
    elif word[i] == 'd':
        word[i] == 'b'
    
print(word)