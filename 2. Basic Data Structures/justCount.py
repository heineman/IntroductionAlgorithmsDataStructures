"""
Just count the number of 4-letter words in the english dictionary.

Note: This dictionary only has 4-letter words, but you can replace
it with any dictionary you have and the resulting code will still work.
"""

ct = 0

wordList = "words.english.txt"
with open(wordList) as fp:
    line = fp.readline()
    while line:
        word = line[:-1].upper()
        if len(word) == 4:
            ct = ct+1
        line = fp.readline()
        
print (ct)
