#one time pad key generated from text file with the key as long as the plaintext
import random

def uploadKey(keyFile):
    key = open(keyFile,"r")
    key = key.read()
    key = key.upper()
    return(key)

def downloadKey(filename,key): #save key to text file with name GeneratedkeyFile
    with open(filename, 'w') as f:
        f.write(key)
    

def generateKeySting(string,key):
    key = list(key)
    keyString = []
    string = string.upper()
    string = string.replace(" ","")
    startpoint = random.randint(0,len(key)) - len(string)
    for i in range (startpoint, startpoint+len(string)):
        keyString.append(key[i % len(key)])
    return("".join(keyString))

def encrypt(plaintext,key):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ","")
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

def main():
    keyFile = "key.txt"
    key_1 = uploadKey(keyFile)
    key = generateKeySting("hello world",key_1)
    plaintext = "hello world"
    print(key)
    ciphertext = encrypt(plaintext,key)
    print(ciphertext)
    print(key)
    print(decrypt(ciphertext,key))
    downloadKey("GeneratedkeyFile.txt",key)

if __name__ == "__main__":
    main()