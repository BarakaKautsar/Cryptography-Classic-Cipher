#program to simulate enigma machine

import string
from collections import deque

def encode_letter(letter):
    rotor1, rotor2, rotor3, reflector = init_Rotor()
    # Step 1: pass through first three rotors
    letter = rotor1[string.ascii_uppercase.index(letter)]
    letter = rotor2[string.ascii_uppercase.index(letter)]
    letter = rotor3[string.ascii_uppercase.index(letter)]
    # Step 2: Pass through reflector
    letter = string.ascii_uppercase[reflector.index(letter)]
    # Step 3: pass through rotors in reverse
    letter = string.ascii_uppercase[rotor3.index(letter)]
    letter = string.ascii_uppercase[rotor2.index(letter)]
    letter = string.ascii_uppercase[rotor1.index(letter)]
    return letter

def encode_message(message):
    rotor1, rotor2, rotor3, reflector = init_Rotor()
    message = message.upper()
    encoded_message = ''
    for letter in message:
        if letter in string.ascii_uppercase:
            encoded_message += encode_letter(letter)
        else:
            encoded_message += letter
    return encoded_message

# Define the rotors and reflector

def init_Rotor():
    rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT' # Reflector B
    return rotor1, rotor2, rotor3, reflector



def decode_message (message):
    rotor1, rotor2, rotor3, reflector = init_Rotor()
    message = message.upper()
    decoded_message = ''
    for letter in message:
        if letter in string.ascii_uppercase:
            decoded_message += decode_letter(letter)
        else:
            decoded_message += letter
    return decoded_message

def decode_letter(letter):
    rotor1, rotor2, rotor3, reflector = init_Rotor()
    # Step 1: pass through first three rotors
    letter = rotor1[string.ascii_uppercase.index(letter)]
    letter = rotor2[string.ascii_uppercase.index(letter)]
    letter = rotor3[string.ascii_uppercase.index(letter)]
    # Step 2: reflect through the reflector
    letter = string.ascii_uppercase[reflector.index(letter)]
    # Step 5: pass back through the rotors in reverse
    letter = string.ascii_uppercase[rotor3.index(letter)]
    letter = string.ascii_uppercase[rotor2.index(letter)]
    letter = string.ascii_uppercase[rotor1.index(letter)]
    return letter

def groupbyFive (string): #group of 5 characters
    string = string.upper()
    string = string.replace(" ","")
    string = ' '.join(string[i:i+5] for i in range(0, len(string), 5))
    return(string)

def main():
    message = input('Enter message: ')
    encoded_message = encode_message(message)
    print('Encoded message: ', encoded_message)
    decoded_message = decode_message(encoded_message)
    print('Decoded message: ', decoded_message)

if __name__ == '__main__':
    main()








            

