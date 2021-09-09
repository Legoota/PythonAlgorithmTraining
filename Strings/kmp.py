def kmp(word, text):
    word_length = len(word)
    text_length = len(text)
    t = [0]*word_length
    indexes = [] # array containing indexes of the beginning of each occurences of word in text

    compute_T(word, word_length, t)

    i = j = 0 # indexes for word and text respectively
    while i < text_length:
        if word[j] == text[i]:
            i += 1
            j += 1
        if j == word_length:
            indexes.append(i-j)
            j = t[j-1]
        elif i < text_length and word[j] != text[i]:
            if j != 0:
                j = t[j-1]
            else:
                i += 1

    return indexes

def compute_T(word, word_length, t):
    length = 0

    t[0] # t[0] is always 0
    i = 1
  
    while i < word_length:
        if word[i]== word[length]:
            length += 1
            t[i] = length
            i += 1
        else:
            if length != 0:
                length = t[length-1]
            else:
                t[i] = 0
                i += 1