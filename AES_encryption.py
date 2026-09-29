from pyaes import AESModeOfOperationECB
import numpy as np

tohex = np.vectorize(lambda x: int(x, 16))

# 05 de ad be ef 42 00 68 61 63 6b 65 64 6b 65 79


def myin(filename):
    with open(filename, 'r') as f:
        rows = [line.split() for line in f if line.strip()]
    return np.array([[int(x, 16) for x in row] for row in rows], dtype=np.uint8)

plaintext = myin(r"plaintext-unknown_key.txt")
with open("recovered_key-unknown.txt", 'r') as f:
    recovered_key = bytes.fromhex(f.readline())


aes = AESModeOfOperationECB(recovered_key)

# compair encrypted_cipher with provided cipher text data
ciphertext = myin(r"ciphertext-unknown_key.txt")
i = 0
j = 0
len_pt = len(plaintext)
for i in range(0, len_pt, 1):
    plaintext_block = plaintext[i].tobytes()
    ciphertext_block = ciphertext[i].tobytes()

    encrypted_cipher = aes.encrypt(plaintext_block)

    if encrypted_cipher != ciphertext_block:
        print(f"\
            idx {i} did not match:\n\
            Derived Cipher:\t{encrypted_cipher.hex(" ")}\n\
            Provided Cipher:\t{ciphertext_block.hex(" ")}\
        ") 
    else:
        i+=1
    recovered_plaintext = aes.decrypt(ciphertext_block)

    if recovered_plaintext != plaintext_block:
        print(f"\
            idx {i} did not match:\n\
            Derived Plaintext:\t{recovered_plaintext.hex(" ")}\n\
            Provided Plaintext:\t{plaintext_block.hex(" ")}\
        ")
    else:
        j+=1


result = (i==len_pt & j==len_pt)
if result:
    print("Sucess")
else:
    print("Some mismatch")

