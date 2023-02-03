#program to simulate enigma machine

import string

def encode_letter(letter):
    rotor1, rotor2, rotor3, reflector = init_Rotor()
    # Step 1: pass through first three rotor
    letter = rotor1[string.ascii_uppercase.index(letter)]
    letter = rotor2[string.ascii_uppercase.index(letter)]
    letter = rotor3[string.ascii_uppercase.index(letter)]
    # Step 4: Pass through reflector
    letter = string.ascii_uppercase[reflector.index(letter)]
    # Step 5: pass through rotors in reverse
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
            encoded_message += encode_letter(letter, rotor1, rotor2, rotor3)
        else:
            encoded_message += letter
    return encoded_message

# Define the rotors and reflector

def init_Rotor():
    rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
    rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
    reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
    return rotor1, rotor2, rotor3, reflector



def decode_message (message):
    rotor1, rotor2, rotor3, reflector = init_Rotor()
    message = message.upper()
    decoded_message = ''
    for letter in message:
        if letter in string.ascii_uppercase:
            decoded_message += decode_letter(letter, rotor1, rotor2, rotor3)
        else:
            decoded_message += letter
    return decoded_message

def decode_letter(letter):
    rotor1, rotor2, rotor3, reflector = init_Rotor()
    # Step 1: pass through first rotor
    letter = rotor1[string.ascii_uppercase.index(letter)]
    # Step 2: pass through second rotor
    letter = rotor2[string.ascii_uppercase.index(letter)]
    # Step 3: pass through third rotor
    letter = rotor3[string.ascii_uppercase.index(letter)]
    # Step 4: reflect through the reflector
    letter = string.ascii_uppercase[reflector.index(letter)]
    # Step 5: pass back through the third rotor
    letter = string.ascii_uppercase[rotor3.index(letter)]
    # Step 6: pass back through the second rotor
    letter = string.ascii_uppercase[rotor2.index(letter)]
    # Step 7: pass back through the first rotor
    letter = string.ascii_uppercase[rotor1.index(letter)]
    return letter

def groupbyFive (string): #group of 5 characters
    string = string.upper()
    string = string.replace(" ","")
    string = ' '.join(string[i:i+5] for i in range(0, len(string), 5))
    return(string)

def main():
    message = input('Enter message: ')
    encoded_message = encode_message(message, rotor1, rotor2, rotor3)
    print('Encoded message: ', encoded_message)
    decoded_message = decode_message(encoded_message, rotor1, rotor2, rotor3)
    print('Decoded message: ', decoded_message)

if __name__ == '__main__':
    main()








            

