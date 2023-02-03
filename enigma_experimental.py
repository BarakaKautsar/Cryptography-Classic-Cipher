import string

def encode_letter(letter, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position):
    # Step 1: pass through first rotor
    rotor1_index = (string.ascii_uppercase.index(letter) + rotor1_position) % 26
    letter = rotor1[rotor1_index]
    # Step 2: pass through second rotor
    rotor2_index = (string.ascii_uppercase.index(letter) + rotor2_position) % 26
    letter = rotor2[rotor2_index]
    # Step 3: pass through third rotor
    rotor3_index = (string.ascii_uppercase.index(letter) + rotor3_position) % 26
    letter = rotor3[rotor3_index]
    # Step 4: reflect through the reflector
    letter = string.ascii_uppercase[reflector.index(letter)]
    # Step 5: pass back through the third rotor
    rotor3_index = (reflector.index(letter) - rotor3_position) % 26
    letter = string.ascii_uppercase[rotor3_index]
    # Step 6: pass back through the second rotor
    rotor2_index = (rotor3_index - rotor2_position) % 26
    letter = string.ascii_uppercase[rotor2_index]
    # Step 7: pass back through the first rotor
    rotor1_index = (rotor2_index - rotor1_position) % 26
    letter = string.ascii_uppercase[rotor1_index]
    return letter

def encode_message(message, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position):
    message = message.upper()
    encoded_message = ''
    for letter in message:
        if letter in string.ascii_uppercase:
            encoded_letter = encode_letter(letter, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position)
            encoded_message += encoded_letter
        else:
            encoded_message += letter
    return encoded_message

# Define the rotors and reflector
rotor1 = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
rotor2 = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
rotor3 = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

def decode_letter(letter, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position):
    # Step 1: pass through first rotor in reverse direction
    rotor1_index = (string.ascii_uppercase.index(letter) - rotor1_position) % 26
    letter = string.ascii_uppercase[rotor1_index]
    # Step 2: pass through second rotor in reverse direction
    rotor2_index = (rotor1_index - rotor2_position) % 26
    letter = string.ascii_uppercase[rotor2_index]
    # Step 3: pass through third rotor in reverse direction
    rotor3_index = (rotor2_index - rotor3_position) % 26
    letter = string.ascii_uppercase[rotor3_index]
    # Step 4: reflect through the reflector
    letter = reflector[string.ascii_uppercase.index(letter)]
    # Step 5: pass back through the third rotor in forward direction
    rotor3_index = (string.ascii_uppercase.index(letter) + rotor3_position) % 26
    letter = rotor3[rotor3_index]
    # Step 6: pass back through the second rotor in forward direction
    rotor2_index = (rotor3_index + rotor2_position) % 26
    letter = rotor2[rotor2_index]
    # Step 7: pass back through the first rotor in forward direction
    rotor1_index = (rotor2_index + rotor1_position) % 26
    letter = rotor1[rotor1_index]
    return letter

def decode_message(encoded_message, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position):
    decoded_message = ''
    for letter in encoded_message:
        if letter in string.ascii_uppercase:
            decoded_letter = decode_letter(letter, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position)
            decoded_message += decoded_letter
        else:
            decoded_message += letter
    return decoded_message



# Example usage
message = 'HELLO WORLD'
rotor1_position = 4
rotor2_position = 9
rotor3_position = 21
encoded_message = encode_message(message, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position)
print(encoded_message)


# Example usage
encoded_message = encode_message('HELLO WORLD', rotor1, rotor2, rotor3, 4, 9, 21)
decoded_message = decode_message(encoded_message, rotor1, rotor2, rotor3, rotor1_position, rotor2_position, rotor3_position)
print(decoded_message)