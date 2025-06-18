from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b"secret data"

# Generate a random key
key = get_random_bytes(16)

# Encryption
cipher = AES.new(key, AES.MODE_OFB)
cipher_text = cipher.encrypt(data)
iv = cipher.iv

print(f"Cipher Text: {cipher_text.hex()}")
print(f"IV: {iv.hex()}")
print(f"Key: {key.hex()}")
