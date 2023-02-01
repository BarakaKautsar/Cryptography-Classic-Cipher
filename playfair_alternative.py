import string


atoz = string.ascii_lowercase.replace("j", ".")
print(atoz)

plaintext = "hidethegoldinthetreestump"
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




            
        
        



print(key_matrix)
ciphertextpairs = []
#rule 1: if the letters are the same, insert an x between them

i = 0
plaintextpairs = []
while i < len(plaintext):
    if plaintext[i] == plaintext[i+1]:
        plaintext = plaintext[:i+1] + "X" + plaintext[i+1:]
    plaintextpairs.append(plaintext[i:i+2])
    i += 2


print (plaintextpairs)



#rule 2: if the letters are in the same row, replace them with the letters to their immediate right respectively

for pair in plaintextpairs:
    applied_rule = False
    for row in key_matrix:
        if pair[0] in row and pair[1] in row:
            j0 = row.find(pair[0])
            print(j0)
            j1 = row.find(pair[1])
        
            ciphertextpair = row[(j0+1)%5] + row[((j1+1)%5)]
            ciphertextpairs.append(ciphertextpair)
            applied_rule = True
    
    if applied_rule:
        continue


#rule 3: if the letters are in the same column, replace them with the letters immediately below respectively
    for j in range(5):
        column = "".join([key_matrix[i][j] for i in range(5)])
        if pair[0] in row and pair[1] in row:
            i0 = column.find(pair[0])
            i1 = column.find(pair[1])
        
            ciphertextpair = column[(i0+1)%5] + column[((i1+1)%5)]
            ciphertextpairs.append(ciphertextpair)
            applied_rule = True
    
    if applied_rule:
        continue
 
#rule 4: if the letters are not in the same row or column, replace them with the letters on the same row respectively
#but at the other pair of corners of the rectangle defined by the original pair. The order is important – the first
#letter of the encrypted pair is the one that lies on the same row as the first letter of the plaintext pair.
    i0 = 0
    i1 = 0
    j0 = 0
    j1 = 0

    for i in range(5):
        rpw = key_matrix[i]
        if pair[0] in row:
            i0 = i
            j0 = row.find(pair[0])
        
        if pair[1] in row:
            i1 = i
            j1 = row.find(pair[1])

    ciphertextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
    ciphertextpairs.append(ciphertextpair)

print("plaintext : hidethegoldinthetreestump")
print("ciphertext: " +"".join(ciphertextpairs))

