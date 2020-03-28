import random
from  math import gcd

class Encryption:

    w               = []
    q               = 0
    r               = 0
    b               = []
    encrypted_text  = []

    def __init__(self):
        self.generate_w()
        self.generate_q()
        self.generate_r()
        self.generate_b()

    # Generate the super increasing array w
    def generate_w(self):
        for i in range(8):
            self.w.append( sum(self.w) + random.randint(1, 10) )
        print("w = ", self.w)

    # Generate a random number q > sum(w)
    def generate_q(self):
        num = sum(self.w)
        self.q = random.randint(num, num + 100)
        print("q = ", self.q)

    # Generate a random number r which is coprime with q
    def generate_r(self):
        while True:
            self.r = random.randint(1, self.q)
            if gcd(self.q, self.r) == 1:
                break
        print("r = ", self.r)

    # Generate b array, which is the public key
    def generate_b(self):
        self.b = [(wi * self.r) % self.q for wi in self.w]
        print("b = ", self.b)

    # Reading user input from keyboard
    def read_user_input(self):
        user_input = input("Enter text for encryption: ")

        # Convert each letter of user input to the corresponding
        # ascii decimal number
        ascii_decimal = [ord(x) for x in user_input]
        print("Ascii decimal representation:\n", ascii_decimal)

        # Convert each  decimal number to the corresponding
        # ascii binary number
        ascii_binary = [bin(x)[2:].zfill(8) for x in ascii_decimal]
        print("Binary representation:\n", ascii_binary)

        # Begin encryption
        self.encrypt(ascii_binary)

    # Encrypt the binary representation of the user input
    # and print the result
    def encrypt(self, ascii_binary):
        for byte in ascii_binary:
            sum = 0
            for i, x in enumerate(byte):
                sum += int(x) * self.b[i]
            self.encrypted_text.append(sum)
        print("Encrypted text:\n", self.encrypted_text)
