# 31 March, 2025
# This code was made using ChatGPT4 and heavily modified by Mr James Boyce.
# This code is available to you for use in Assignment 3.
# It is NOT a requirement for you to use this code, it is made available for you, if you choose to use it.

#NOTE - RSA has some interesting restrictions when it comes to message length.
#Test your code THOROUGHLY!

# This imports the various portions of the Crypto Library for use in the program.
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def makeRSAKey():
    """Generates a new RSA Key pair."""

    Key = RSA.generate(2048)  # Generate a 2048-bit RSA key pair
    privateKey = Key.export_key()  # Export the private key
    publicKey = Key.publickey().export_key()  # Export the corresponding public key

    return privateKey, publicKey  # Return both keys


def encryptRSA(plainText, publicKey):
    """Encrypts the given text using RSA with the provided public Key."""

    Key = RSA.import_key(publicKey)  # Import the public key
    cipher = PKCS1_OAEP.new(Key)  # Create an RSA cipher with OAEP padding
    cipherText = cipher.encrypt(plainText.encode('utf-8'))  # Encrypt the text

    return base64.b64encode(cipherText).decode('utf-8')  # Encode the result in base64


def decryptRSA(cipherText, privateKey):
    """Decrypts the given RSA-encrypted text using the provided private Key."""

    Key = RSA.import_key(privateKey)  # Import the private key
    cipher = PKCS1_OAEP.new(Key)  # Create an RSA cipher with OAEP padding
    decoded = base64.b64decode(cipherText.encode('utf-8'))  # Decode the base64 input
    plainText = cipher.decrypt(decoded).decode('utf-8')  # Decrypt and convert to a string

    return plainText  # Return the original text


# Example Usage
def main():
    privateKey, publicKey = makeRSAKey()

    plainText = """Banana"""

    encryptedRSA = encryptRSA(plainText, publicKey)
    decryptedRSA = decryptRSA(encryptedRSA, privateKey)

    print(f"RSA Private Key:\n{privateKey}")
    print(f"RSA Public Key:\n{publicKey}")
    print(f"RSA Encrypted:\n{encryptedRSA}")
    print(f"RSA Decrypted:\n{decryptedRSA}")

#This allows the code to be tested on its own
if __name__ == "__main__":
    main()
