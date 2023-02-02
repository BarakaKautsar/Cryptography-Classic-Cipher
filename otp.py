#one time pad key generated from text file with the key as long as the plaintext
import random

def groupbyFive (string): #group of 5 characters
    string = string.upper()
    string = string.replace(" ","")
    string = ' '.join(string[i:i+5] for i in range(0, len(string), 5))
    return(string)



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
    for i in range (len(plaintext)):
        x = ((ord(plaintext[i])+ord(key[i])) % 26) + ord("A")
        ciphertext.append(chr(x))
    return("".join(ciphertext))

def decrypt (ciphertext,key):
    ciphertext=ciphertext.upper()
    ciphertext=ciphertext.replace(" ","")
    key=key.upper()
    plaintext = []
    for i in range(len(ciphertext)):
        x = ((ord(ciphertext[i])-ord(key[i])+26) % 26) + ord("A")
        plaintext.append(chr(x))
    return("".join(plaintext))

def main():
    keyFile = "key.txt"
    key = uploadKey(keyFile)
    generatedKeyString = generateKeySting("This is a test",key)
    print(generatedKeyString)
    plaintext = "This is a test"
    ciphertext = encrypt(plaintext,generatedKeyString)
    ciphertext = groupbyFive(ciphertext)
    print(ciphertext)
    plaintext = decrypt(ciphertext,generatedKeyString)
    print(plaintext)

if __name__ == "__main__":
    main()
