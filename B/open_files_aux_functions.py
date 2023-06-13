from PIL import Image
from Crypto.Hash import SHA3_256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA
import os
import sys

def open_txt_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"File: {filepath}\n")
            print(content)

def open_jpg_jpeg_file(filepath):
    try:
        image = Image.open(filepath)
        image.show()
    except Exception as e:
        print(f"Error opening image file: {str(e)}")     

def make_hash_from_file(filepath):
    # Initialize SHA-3 object
    sha3 = SHA3_256.new()

    with open(filepath, 'rb') as file:
        # Read file contents in chunks to avoid excessive memory usage
        for chunk in iter(lambda: file.read(4096), b''):
            # Update the SHA-3 hash
            sha3.update(chunk)
    return sha3

    # # Convert the computed hash to a hexadecimal string
    # hash_value = sha3.hexdigest()

    # # Return the hash value
    # return hash_value 

def check_signature_if_valid(filepath, generated_hash):
    # check if hash of the file we want to open is equal with the hash received form A (in ./B/received_hash_files/filename.txt)

    filename = os.path.basename(filepath).split('.')[0]
    received_signature_filepath = './B/received_signatures/signature_' + filename + '.txt'

    # Get recived siganture
    with open(received_signature_filepath) as f:
        signature = f.read()

    # # Convert signature
    # try:
    #     signature_hex = bytes.fromhex(signature)
    # except:
    #     print("Signature is wrong!")
    #     sys.exit()

    # # Import public RSA key
    # try:
    #     with open("./B/As_public_key.pem", "rb") as f:
    #         public_key = RSA.importKey(f.read())
    # except:
    #     print("Public key is wrong!")
    #     sys.exit()

    # Convert signature
    signature_hex = bytes.fromhex(signature)
    # # Import public RSA key
    # with open("./B/As_public_key.pem", "rb") as f:
    #     public_key = RSA.importKey(f.read())  

    # Import public RSA key - more secure version
    try:
        with open("./B/As_public_key.pem", "rb") as f:
            public_key = RSA.importKey(f.read())
    except:
        return False     

    # Verify received signature and file
    authenticator = PKCS1_v1_5.new(public_key)
    authenticated = authenticator.verify(generated_hash, signature_hex)
    return authenticated


# check_signature_if_valid("./B/received_files/secret_info_for_Bob.txt", "lalal")