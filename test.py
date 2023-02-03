import vigenereExtended

# with open("test.png", "rb") as save:
#     plain_text = save.read().decode("latin-1")
#     cipher = vigenereExtended.encrypt(plain_text,"KRIPTO")
#     with open("testencrypt.txt", "wb") as file:
#          file.write(cipher.encode('latin-1'))

with open("testencrypt.txt", "rb") as save:
    plain_text = save.read().decode("latin-1")
    cipher = vigenereExtended.decrypt(plain_text,"KRIPTO")
    with open("testdecrypt.png", "wb") as file:
         file.write(cipher.encode('latin-1'))