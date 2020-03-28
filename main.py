from cryptography.decryption import Decryption
from cryptography.encryption import Encryption
from cryptography.break_hm import Break_HM

def main():
    print("# =========== Encryption =========== #")
    merkle_hellman = Encryption()
    merkle_hellman.read_user_input()

    print("\n# =========== Decryption =========== #")
    merkle_hellman_dec = Decryption(merkle_hellman.w, merkle_hellman.q, merkle_hellman.r,
                                    merkle_hellman.encrypted_text)
    merkle_hellman_dec.decrypt()

    print("\n# =========== Break =========== #")
    merkle_hellman_break = Break_HM(merkle_hellman.b, merkle_hellman.encrypted_text)
    merkle_hellman_break.break_mh()

if __name__ == '__main__':
    main()
