def KMPArray(pattern):  # returns KMP list of indexes
    indexing = [-1] * (len(pattern) + 1)
    pred = -1

    for i in range(1, len(pattern) + 1):
        while pred > -1 and pattern[pred] != pattern[i - 1]:
            pred = indexing[pred]

        pred += 1

        if i != len(pattern) and pattern[i] == pattern[pred]:
            indexing[i] = indexing[pred]
        else:
            indexing[i] = pred

    return indexing

def main():
    text = 'acbabadababbdbabac'
    pattern = 'babac'
    # text = 'ABABBCAACCAWACACAWCCA'
    # pattern = 'BCAACCA'
    # text = 'abbababbabababb'
    # pattern = 'abb'
    # text = 'ababcabcabababd'
    # pattern = 'ababd'

    patIndex = 0
    indexing = KMPArray(pattern)
    matchedIndexes = [] 

    for textIndex, char in enumerate(text):
        while patIndex > -1 and pattern[patIndex] != char:
            patIndex = indexing[patIndex]
        
        patIndex += 1

        if patIndex == len(pattern):
            matchedIndexes.append(textIndex - len(pattern) + 1)
            patIndex = 0

    print(matchedIndexes) 

if __name__ == "__main__":
    main()