#playfair cipher

import string
import tkinter as TK
from tkinter.filedialog import askopenfilename


#function to read any file and return the text in it
def plaintext_file_read(filename):
    with open(filename, "r") as f:
        plaintext = f.read()
    return plaintext

def save_ciphertext(filename, ciphertext):
    with open(filename, "w") as f:
        f.write(ciphertext)

def groupbyFive (string): #group of 5 characters
    string = string.upper()
    string = string.replace(" ","")
    string = ' '.join(string[i:i+5] for i in range(0, len(string), 5))
    return(string)


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
    
    
    for i in range(0, len(plaintext)-1, 2):
        if plaintext[i] == plaintext[i+1]:
            plaintext = plaintext[:i+1] + "X" + plaintext[i+1:]

    diagraph = [[plaintext[i],plaintext[i+1]] for i in range(0,len(plaintext)-1,2)]
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

#plaintext = plaintext_file_read(askopenfilename())
#key_matrix = key_matrix_generation("playfair example")
#ciphertext = diagraph_encryption(diagraph, key_matrix)
#print(ciphertext)

def playfair_encryption(plaintext, key):
    key_matrix = key_matrix_generation(key)
    diagraph = diagraph_generation(plaintext)
    ciphertext = diagraph_encryption(diagraph, key_matrix)
    return ciphertext


def playfair_decryption(ciphertext, key_matrix): #can't handle odd length ciphertext
    plaintext = ""
    key_matrix = key_matrix_generation(key_matrix)
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



#decryptedtext = diagraph_decryption(ciphertext, key_matrix)
#print(decryptedtext)




#ciphertext = "BMODZBXDNABEKUDMUIXMMOUVIF"
#key_matrix = key_matrix_generation("playfair example")
#plaintext = playfair_decryption(ciphertext, key_matrix)
#print(plaintext)

def main():
    plaintext = (input("Enter plaintext file: "))
    key = input("Enter key: ")
    ciphertext = playfair_encryption(plaintext, key)
    ciphertext = groupbyFive(ciphertext)
    print(ciphertext)
    save_ciphertext("ciphertext.txt", ciphertext)
    key_matrix = key_matrix_generation(key)
    plaintext = playfair_decryption(ciphertext, key_matrix)
    print(plaintext)

