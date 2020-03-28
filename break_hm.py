class Break_HM:

    # Suppose the hacker has access to the public key
    # and the encrypted  text, he can break the encryption
    def __init__(self, b, encrypted_text):
        self.b = b
        self.encrypted_text = encrypted_text

    def break_mh(self):
        result = [0 for i in self.encrypted_text]

        for dec_num in range(1, 256):
            bin_num = bin(dec_num)[2:].zfill(8)

            sum = 0
            for bit_post, bit in enumerate(bin_num):
                if int(bit) == 1:
                    sum += self.b[bit_post]

            for index, e in enumerate(self.encrypted_text):
                if (e == sum):
                    result[index] = bin_num
                    self.encrypted_text[index] = 0

        print("Encrypted message has been broken... and is:\n", result)
