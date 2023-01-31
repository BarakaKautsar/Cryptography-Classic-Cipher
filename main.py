import playfair
import sys

def main():
    key = sys.argv[1]
    plain_text = sys.argv[2]
    matrix = playfair.generate_matrix(key)
    cipher_text = playfair.encrypt(matrix, plain_text)
    print(cipher_text)
    plain_text = playfair.decrypt(matrix, cipher_text)
    print(plain_text)

if __name__ == "__main__":
    main()