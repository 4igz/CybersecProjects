from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_file(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_data = pad(data, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    return encrypted_data

def decrypt_file(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(data)
    unpadded_data = unpad(decrypted_data, AES.block_size)
    return unpadded_data

if __name__ == "__main__":
    # Keys must be 16, 24, or 32 bytes long. If the key is less than 32 bytes,
    # it will be padded with 0s, if longer then it will be truncated
    key = input("Enter the key: ")
    if len(key) > 32:
        key = key[:32]
    else:
        key = key.ljust(32, "0")
    # input always returns a string, so we need to encode it to bytes
    key = key.encode()

    file = input("Enter the file path: ")
    # Get bytes from file to encrypt
    with open(file, "rb") as f:
        data = f.read()

    print("Encrypting file...")
    encrypted_data = encrypt_file(data, key)
    with open("encrypted_file", "wb") as f:
        f.write(encrypted_data)
    print("File encrypted.")

    print("Decrypting file...")
    decrypted_data = decrypt_file(encrypted_data, key)
    with open("decrypted_file", "wb") as f:
        f.write(decrypted_data)
    print("File decrypted.")