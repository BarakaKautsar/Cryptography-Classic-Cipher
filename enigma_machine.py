#program to simulate enigma machine

from string import ascii_uppercase

class Keyboard :

    def forward(self, letter):
        signal = ascii_uppercase.find(letter)
        return signal

    def backward(self, signal):
        letter = ascii_uppercase[signal]
        return letter

class Plugboard:

    def __init__(self, pairs):
        self.left = ascii_uppercase
        self.right = ascii_uppercase
        for pair in pairs:
            

