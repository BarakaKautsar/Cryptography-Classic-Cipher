#program of enigma machine cipher

# Importing the required libraries
import string
import random

# Defining the class
class EnigmaMachine:
    # Defining the constructor
    def __init__(self, rotors, reflector, plugboard):
        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard

    # Defining the function for encrypting the message
    def encrypt(self, message):
        # Converting the message to uppercase
        message = message.upper()
        # Removing the spaces from the message
        message = message.replace(" ", "")
        # Converting the message to a list
        message = list(message)
        # Creating an empty list for storing the encrypted message
        encrypted_message = []
        # Looping through each character in the message
        for character in message:
            # Checking if the character is a letter
            if character in string.ascii_letters:
                # Checking if the character is in the plugboard
                if character in self.plugboard:
                    # Replacing the character with the character in the plugboard
                    character = self.plugboard[character]
                # Looping through each rotor
                for rotor in self.rotors:
                    # Replacing the character with the character in the rotor
                    character = rotor[character]
                # Replacing the character with the character in the reflector
                character = self.reflector[character]
                # Looping through each rotor in reverse
                for rotor in self.rotors[::-1]:
                    # Replacing the character with the character in the rotor
                    character = rotor[character]
                # Checking if the character is in the plugboard
                if character in self.plugboard:
                    # Replacing the character with the character in the plugboard
                    character = self.plugboard[character]
            # Adding the character to the encrypted message
            encrypted_message.append(character)
        # Returning the encrypted message
        return "".join(encrypted_message)

    # Defining the function for decrypting the message
    def decrypt(self, message):
        # Converting the message to uppercase
        message = message.upper()
        # Removing the spaces from the message
        message = message.replace(" ", "")
        # Converting the message to a list
        message = list(message)
        # Creating an empty list for storing the decrypted message
        decrypted_message = []
        # Looping through each character in the message
        for character in message:
            # Checking if the character is a letter
            if character in string.ascii_letters:
                # Checking if the character is in the plugboard
                if character in self.plugboard:
                    # Replacing the character with the character in the plugboard
                    character = self.plugboard[character]
                # Looping through each rotor in reverse
                for rotor in self.rotors[::-1]:
                    # Replacing the character with the character in the rotor
                    character = rotor[character]
                # Replacing the character with the character in the reflector
                character = self.reflector[character]
                # Looping through each rotor
                for rotor in self.rotors:
                    # Replacing the character with the character in the rotor
                    character = rotor[character]
                # Checking if the character is in the plugboard
                if character in self.plugboard:
                    # Replacing the character with the character in the plugboard
                    character = self.plugboard[character]
            # Adding the character to the decrypted message
            decrypted_message.append(character)
        # Returning the decrypted message
        return "".join(decrypted_message)

# Defining the function for creating the rotors
def create_rotors():
    # Creating a list of the alphabet
    alphabet = list(string.ascii_uppercase)
    # Creating an empty list for storing the rotors
    rotors = []
    # Looping through each rotor
    for i in range(3):
        # Creating a copy of the alphabet
        rotor = alphabet.copy()
        # Shuffling the rotor
        random.shuffle(rotor)
        # Converting the rotor to a dictionary
        rotor = dict(zip(alphabet, rotor))
        # Adding the rotor to the list of rotors
        rotors.append(rotor)
    # Returning the list of rotors
    return rotors

# Defining the function for creating the reflector
def create_reflector():
    # Creating a list of the alphabet
    alphabet = list(string.ascii_uppercase)
    # Creating a copy of the alphabet
    reflector = alphabet.copy()
    # Shuffling the reflector
    random.shuffle(reflector)
    # Converting the reflector to a dictionary
    reflector = dict(zip(alphabet, reflector))
    # Returning the reflector
    return reflector

# Defining the function for creating the plugboard
def create_plugboard():
    # Creating a list of the alphabet
    alphabet = list(string.ascii_uppercase)
    # Creating an empty list for storing the plugboard
    plugboard = {}
    # Looping through each letter in the alphabet
    for letter in alphabet:
        # Checking if the letter is in the plugboard
        if letter not in plugboard:
            # Creating a copy of the alphabet
            available_letters = alphabet.copy()
            # Removing the letter from the available letters
            available_letters.remove(letter)
            # Looping through each letter in the available letters
            for available_letter in available_letters:
                # Checking if the letter is in the plugboard
                if available_letter not in plugboard:
                    # Adding the letter to the plugboard
                    plugboard[letter] = available_letter
                    # Adding the available letter to the plugboard
                    plugboard[available_letter] = letter
                    # Breaking out of the loop
                    break
    # Returning the plugboard
    return plugboard

# Defining the function for creating the enigma machine
def create_enigma_machine():
    # Creating the rotors
    rotors = create_rotors()
    # Creating the reflector
    reflector = create_reflector()
    # Creating the plugboard
    plugboard = create_plugboard()
    # Creating the enigma machine
    enigma_machine = EnigmaMachine(rotors, reflector, plugboard)
    # Returning the enigma machine
    return enigma_machine

# Creating the enigma machine
enigma_machine = create_enigma_machine()

# Getting the message from the user
message = input("Enter the message: ")
# Encrypting the message
encrypted_message = enigma_machine.encrypt(message)
# Printing the encrypted message
print("Encrypted message:", encrypted_message)
# Decrypting the message
decrypted_message = enigma_machine.decrypt(encrypted_message)
# Printing the decrypted message
print("Decrypted message:", decrypted_message)
