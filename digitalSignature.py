from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import sys


def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as f:
        f.write(private_key)

    with open("public.pem", "wb") as f:
        f.write(public_key)

    print("Keys saved as 'private.pem' and 'public.pem'")


def sign_file(filename):
    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    with open(filename, "rb") as f:
        message = f.read()

    hash_obj = SHA256.new(message)
    signature = pkcs1_15.new(private_key).sign(hash_obj)

    with open("signature.bin", "wb") as f:
        f.write(signature)

    print(f"File '{filename}' signed as 'signature.bin'")


if __name__ == "__main__":
    command = sys.argv[1]

    if command == "generate":
        generate_keys()
    elif command == "sign":
        if len(sys.argv) < 3:
            print("Usage: python digitalSignature.py [generate|sign] <filepath>")
            sys.exit(1)
        else:
            sign_file(sys.argv[2])
    else:
        print("Unknown command. Use: generate, sign.")
