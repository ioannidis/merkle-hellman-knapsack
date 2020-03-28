class Decryption:

    _c              = []
    _r              = 1

    def __init__(self, w, q, r, encrypted_text, ):
        self.w              = w
        self.q              = q
        self.r              = r
        self.encrypted_text = encrypted_text

        self.calculate__r()
        self.calculate__c()

    # Calculate c' for each element in the encrypted text array
    def calculate__c(self):
        for x in self.encrypted_text:
            self._c.append((self._r * x) % self.q)
        print("c' array:\n", self._c)

    # Calculate r^-1
    def calculate__r(self):
        while (self.r * self._r) % self.q != 1:
            self._r += 1
        print("r^-1 = ", self._r)

    # Decryption algorithm
    def decrypt(self):
        ascii_binary = []
        for c in self._c:
            if c > self.w[7]:
                binary = str(1)
                dif = c - self.w[7]
            else:
                binary = str(0)
                dif = c
            for i in range(6, -1, -1):
                if self.compare(dif, self.w[i]) == 1:
                    binary = str(1) + binary
                    dif -= self.w[i]
                else:
                    binary = str(0) + binary
            ascii_binary.append(binary)

        print("Decrypted text in binary from is:\n", ascii_binary)

        # Convert binary to ascii and print the
        # decrypted message
        decrypted_text = ""
        for byte in ascii_binary:
            decrypted_text += chr(int(byte,2))
        print("Decrypted text is:\n", decrypted_text)

    # Compare x to y
    def compare(self, x, y):
        return 1 if x >= y else 0
