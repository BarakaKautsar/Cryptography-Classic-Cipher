#playfair cipher

import string

def key_matrix_generation(key):
    key = key.upper()
    key = key.replace("J", "I")
    key = key.replace(" ", "")
    key_matrix = []
    for i in key:
        if i not in key_matrix:
            key_matrix.append(i)
    for i in string.ascii_uppercase.replace("J", ""):
        if i not in key_matrix:
            key_matrix.append(i)
    return key_matrix

key_matrix = key_matrix_generation("playfair example")
print(key_matrix)

def playfair_encryption(plaintext, key_matrix):
    i = 0
    for i in range(len(plaintext)):
        plaintext = plaintext.replace("J", "I")
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext = plaintext + "X"
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + "X" + plaintext[i+1:]
    for i in range(0, len(plaintext), 2):
        row1 = key_matrix.index(plaintext[i-1]) // 5
        col1 = key_matrix.index(plaintext[i-1]) % 5
        row2 = key_matrix.index(plaintext[i]) // 5
        col2 = key_matrix.index(plaintext[i]) % 5
        if row1 == row2:
            ciphertext = ciphertext + key_matrix[row1*5+((col1+1)%5)] + key_matrix[row2*5+((col2+1)%5)]
        elif col1 == col2:
            ciphertext = ciphertext + key_matrix[((row1+1)%5)*5+col1] + key_matrix[((row2+1)%5)*5+col2]
        else:
            ciphertext = ciphertext + key_matrix[row1*5+col2] + key_matrix[row2*5+col1]
    return ciphertext

plaintext = "Hide the gold in the tree stump"
key_matrix = key_matrix_generation("playfair example")
ciphertext = playfair_encryption(plaintext, key_matrix)
print(ciphertext)

def playfair_decryption(ciphertext, key_matrix):
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1 = key_matrix.index(ciphertext[i]) // 5
        col1 = key_matrix.index(ciphertext[i]) % 5
        row2 = key_matrix.index(ciphertext[i+1]) // 5
        col2 = key_matrix.index(ciphertext[i+1]) % 5
        if row1 == row2:
            plaintext = plaintext + key_matrix[row1*5+((col1-1)%5)] + key_matrix[row2*5+((col2-1)%5)]
        elif col1 == col2:
            plaintext = plaintext + key_matrix[((row1-1)%5)*5+col1] + key_matrix[((row2-1)%5)*5+col2]
        else:
            plaintext = plaintext + key_matrix[row1*5+col2] + key_matrix[row2*5+col1]
    return plaintext

#ciphertext = "BMODZBXDNABEKUDMUIXMMOUVIF"
#key_matrix = key_matrix_generation("playfair example")
#plaintext = playfair_decryption(ciphertext, key_matrix)
#print(plaintext)



