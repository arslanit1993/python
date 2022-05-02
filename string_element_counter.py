# So if you know what you want to count, you can get the number of the things in a string 


alphabet = 'abcdefghijklmnopqrstuvwxyz '

def letter_counter (word):
    empty = []
    for i in word:
        if i in alphabet and i not in empty:
            empty.append(i)
            empty.append(word.count(i))

    return empty

letter_counter('emotional damage')

