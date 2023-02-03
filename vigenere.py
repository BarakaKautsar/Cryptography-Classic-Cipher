def generateKeySting(string,key):
    key = list(key)
    keyString = []
    for i in range (len(string)):
        keyString.append(key[i % len(key)])
    return("".join(keyString))

def encrypt(plaintext,key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = []
    keyString = generateKeySting(plaintext,key).upper()
    for i in range (len(plaintext)):
        x = ((ord(plaintext[i])+ord(keyString[i])) % 26) + ord("A")
        ciphertext.append(chr(x))
    return("".join(ciphertext))

def decrypt (ciphertext,key):
    ciphertext=ciphertext.upper()
    key=key.upper()
    plaintext = []
    keyString = generateKeySting(ciphertext,key).upper()
    for i in range(len(ciphertext)):
        x = ((ord(ciphertext[i])-ord(keyString[i])+26) % 26) + ord("A")
        plaintext.append(chr(x))
    return("".join(plaintext))