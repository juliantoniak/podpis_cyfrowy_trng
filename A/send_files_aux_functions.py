import shutil
import os
from Crypto.Hash import SHA3_256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA

def update_Bens_received_public_key():
    source_path = "./A/keys/public_key.pem"
    destination_path = "./B/As_public_key.pem"
    shutil.copy2(source_path, destination_path)

#update_Bens_received_public_key()

def make_hash_from_file(filepath):
    # Initialize SHA-3 object
    sha3 = SHA3_256.new()

    with open(filepath, 'rb') as file:
        # Read file contents in chunks to avoid excessive memory usage
        for chunk in iter(lambda: file.read(4096), b''):
            # Update the SHA-3 hash
            sha3.update(chunk)
    
    return sha3

def make_signature_with_private_key(filepath, generated_hash):
    # base_filename, _= os.path.splitext(filepath)
    filename = os.path.basename(filepath).split('.')[0]

    # Import private RSA key
    with open("./A/keys/private_key.pem", "r") as f:
        private_key = RSA.importKey(f.read())

    # Create siganture using private key
    signer = PKCS1_v1_5.new(private_key)
    signature = signer.sign(generated_hash)

    # Save siganture to file
    output_sig_file = "./A/signatures/signature_" + filename + ".txt"
    with open(output_sig_file, "w") as file:
        file.write(signature.hex())
    
    return output_sig_file

def send_original_file(filepath):
    source_path = filepath
    destination_path = "./B/received_files/" + os.path.basename(filepath)
    shutil.copy2(source_path, destination_path)

def send_signature_file(filepath):
    # Read the output file path based on the given filepath
    # output_hash_filepath = './A/hash_files/hash_' + os.path.splitext(os.path.basename(filepath))[0] + '.txt'
    source_path = filepath
    destination_path = "./B/received_signatures/" + os.path.basename(filepath)
    # print(source_path, destination_path)
    shutil.copy2(source_path, destination_path)













# filename = './A/files_to_send/cat.jpg'
# send_hash_file(filename)

    # # Convert the computed hash to a hexadecimal string
    # hash_value = sha3.hexdigest()

    # # # Build the output file path based on the given filepath
    # # output_filepath = './A/hash_files/hash_' + os.path.splitext(os.path.basename(filepath))[0] + '.txt'

    # # # Write the hash value to the output file
    # # with open(output_filepath, 'w') as output_file:
    # #     output_file.write(hash_value)

    # # Return the hash value
    # return hash_value

# filename = './A/files_to_send/cat.jpg'
# hash_value = make_hash_from_file(filename)
# print(f"Skrót SHA-3 pliku '{filename}': {hash_value}")


# filename = './A/files_to_send/cat.jpg'
# send_original_file(filename)