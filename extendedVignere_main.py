import vigenereExtended
import string
from tkinter.filedialog import askopenfilename

def main():
    # Get the message to encode
    message = vigenereExtended.plaintext_file_read_binary(askopenfilename())
    # Get the key
    key = input('Enter the key: ')
    key = vigenereExtended.generateKeySting(message, key)
    print(key)
    # Encode the message
    encoded_message = vigenereExtended.encrypt(message, key)
    # Print the encoded message
    print('The encoded message is:', encoded_message)
    # Print the encoded message in groups of 5 characters
    #print('The encoded message in groups of 5 characters is:', groupbyFive(encoded_message))
    # Decode the message
    #decoded_message = vigenereExtended.decrypt(encoded_message, key)
    # Print the decoded message
    #print('The decoded message is:', decoded_message)
    # Print the decoded message in groups of 5 characters
    #print('The decoded message in groups of 5 characters is:', groupbyFive(decoded_message))

main()