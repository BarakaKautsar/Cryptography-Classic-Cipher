#one-time pad program with key generated from a file and the key is as long as the plaintext  

def file_to_key(plaintext, filename):
    key = ""
    with open(filename, "r") as f:
        for i in range(len(plaintext)):
            line = f.readline()
            if line == "":
                f.seek(0)
                line = f.readline()
            key += line[0]
    return key

def otp():
    plaintext = input("Enter plaintext: ")
    plaintext = plaintext.lower()
    plaintext = plaintext.replace(" ", "")
    key = ""
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr((ord(plaintext[i]) + ord(key[i])) % 26 + 65)
    print("Ciphertext: " + ciphertext)

otp()
