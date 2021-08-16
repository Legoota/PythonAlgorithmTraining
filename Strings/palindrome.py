def palindrome(word):
    word = word.strip().replace(" ", "").lower()
    
    for i in range(len(word) // 2):
       if word[i] != word[len(word) - i - 1] : 
           return False
    return True