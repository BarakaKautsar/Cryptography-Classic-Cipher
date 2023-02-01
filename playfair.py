#playfair cipher

import string

def key_matrix_generation(key):
    key = key.upper()
    key = key.replace("J", "I")
    key = key.replace(" ", "")
    key_matrix = []
    matrix_5by5 = [[0 for i in range (5)] for j in range(5)]
    for c in key:
        if c not in key_matrix:
            key_matrix.append(c)
    for c in string.ascii_uppercase.replace("J", ""):
        if c not in key_matrix:
            key_matrix.append(c)
    index = 0
    for i in range(0,5):
        for j in range(0,5):
            matrix_5by5[i][j] = key_matrix[index]
            index+=1
    return matrix_5by5

key_matrix = key_matrix_generation("playfair example")
#print(key_matrix)

def ceiling_division(a, b):
    return int(-(-a // b))



def diagraph_generation(plaintext):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.replace("J", "I")
    diagraph = [[[0 for i in range (ceiling_division(len(plaintext),2))] for j in range(2)]]
    
    
    for i in range(0, len(plaintext), 2):
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + "X" + plaintext[i+1:]

    diagraph = [[plaintext[i],plaintext[i+1]] for i in range(0,len(plaintext),2)]
    return diagraph

diagraph = diagraph_generation("Hide the gold in the tree stump")
#print(diagraph)

def diagraph_encryption(diagraph, key_matrix):
    ciphertext = ""
    for i in range(0, len(diagraph)):
        row1 = 0
        col1 = 0
        row2 = 0
        col2 = 0
        for j in range(0,5):
            for k in range(0,5):
                if diagraph[i][0] == key_matrix[j][k]:
                    row1 = j
                    col1 = k
                if diagraph[i][1] == key_matrix[j][k]:
                    row2 = j
                    col2 = k
        if row1 == row2:
            ciphertext = ciphertext + key_matrix[row1][(col1+1)%5] + key_matrix[row2][(col2+1)%5]
        elif col1 == col2:
            ciphertext = ciphertext + key_matrix[(row1+1)%5][col1] + key_matrix[(row2+1)%5][col2]
        else:
            ciphertext = ciphertext + key_matrix[row1][col2] + key_matrix[row2][col1]
    return ciphertext



plaintext = "Hide the gold in the tree stump"
key_matrix = key_matrix_generation("playfair example")
ciphertext = diagraph_encryption(diagraph, key_matrix)
print(ciphertext)

def diagraph_decryption(ciphertext, key_matrix): #can't handle odd length ciphertext
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1 = 0
        col1 = 0
        row2 = 0
        col2 = 0
        for j in range(0,5):
            for k in range(0,5):
                if ciphertext[i] == key_matrix[j][k]:
                    row1 = j
                    col1 = k
                if ciphertext[i+1] == key_matrix[j][k]:
                    row2 = j
                    col2 = k
        if row1 == row2:
            plaintext = plaintext + key_matrix[row1][(col1-1)%5] + key_matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext = plaintext + key_matrix[(row1-1)%5][col1] + key_matrix[(row2-1)%5][col2]
        else:
            plaintext = plaintext + key_matrix[row1][col2] + key_matrix[row2][col1]
    return plaintext

decryptrdtext = diagraph_decryption(ciphertext, key_matrix)
print(decryptrdtext)


#ciphertext = "BMODZBXDNABEKUDMUIXMMOUVIF"
#key_matrix = key_matrix_generation("playfair example")
#plaintext = playfair_decryption(ciphertext, key_matrix)
#print(plaintext)



