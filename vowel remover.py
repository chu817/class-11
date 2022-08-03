s=input('enter a word/words')
for i in s:
    if (i in 'AEIOUaeiou'):
        continue
    print(i)
