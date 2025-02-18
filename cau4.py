def levenshtein_distance(token1, token2):
    distances = [[0 for _ in range(len(token2) + 1)] for _ in range(len(token1) + 1)]

    for i in range(len(token1) + 1):
        distances[i][0] = i
    for j in range(len(token2) + 1):
        distances[0][j] = j

    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                distances[i][j] = 1 + min(distances[i - 1][j], distances[i][j - 1], distances[i - 1][j - 1])

    return float(distances[-1][-1])

assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance("hola", "hello"))