def levenshtein(word1, word2):
    distance = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]

    for i in range(1, len(word1) + 1): distance[i][0] = i
    for j in range(1, len(word2) + 1): distance[0][j] = j

    for j in range(1, len(word2) + 1):
        for i in range(1, len(word1) + 1):
            substitutionCost = 0 if(word1[i-1] == word2[j-1]) else 1
            distance[i][j] = min(distance[i-1][j] + 1, distance[i][j-1] + 1, distance[i-1][j-1] + substitutionCost)
            
    return distance[len(word1)][len(word2)]