import string


def key_matrix_generation(key):
    atoz = string.ascii_lowercase.replace("j", ".")
    print(atoz)

    key = 'playfair example'
    key_matrix = ['' for i in range(5)]

    i = 0
    j = 0

    for c in key:
        c = c.lower()
        if c in atoz:
            key_matrix[i] += c
            atoz = atoz.replace(c, ".")
            j += 1
            if j == 5:
                j = 0
                i += 1

    for c in atoz:
        if c != ".":
            key_matrix[i] += c
            j += 1
            if j == 5:
                j = 0
                i += 1

    return key_matrix
    #print(key_matrix)

#rule 1: if the letters are the same, insert an x between them
def rule1(plaintext):
    i = 0
    plaintext = "Hidethegoldinthetreestump"
    plaintextpairs = []
    while i < len(plaintext):
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + "X" + plaintext[i+1:]
        plaintextpairs.append(plaintext[i:i+2])
        i += 2

    return plaintextpairs
    # print (plaintextpairs)

#rule 2: if the letters are in the same row, replace them with the letters to their immediate right respectively
#rule 3: if the letters are in the same column, replace them with the letters immediately below respectively
#rule 4: if the letters are not in the same row or column, replace them with the letters on the same row respectively
#but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first
#letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.

