#program to simulate enigma machine

from string import ascii_uppercase

class Keyboard :

    def forward(self, letter):
        signal = ascii_uppercase.find(letter)
        return signal

    def backward(self, signal):
        letter = ascii_uppercase[signal]
        return letter

