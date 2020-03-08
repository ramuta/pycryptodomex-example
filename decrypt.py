# AES 256 encryption/decryption using pycryptodome library
# Code taken and slightly modified from this article (author Lane Wagner):
# https://qvault.io/2020/02/06/aes-256-cipher-python-cryptography-examples/
from encrypt import decrypt

if __name__ == "__main__":
    password = input("Password: ")

    # Copy the cyphertext dictionary here (instead of this dict)
    encrypted = {'cipher_text': 'QsLv4NsUWwn8EHpkrAzv9LubHvdOpO155Nk=',
                 'salt': 'P03yo9n/a3aispQT6HqwAw==',
                 'nonce': 'k1OIgz37GttK8UE4Jwvq6A==',
                 'tag': '+gBagtNsGPGUmq7JE7M7/Q=='}

    # Let us decrypt using our original password
    decrypted = decrypt(encrypted, password)
    print(bytes.decode(decrypted))
