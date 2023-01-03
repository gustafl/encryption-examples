import rsa


def generate_key_pair(name):
    public_key, private_key = rsa.newkeys(1024)

    with open(f"{name.lower()}_public_key.pem", "wb") as f:
        f.write(public_key.save_pkcs1("PEM"))

    with open(f"{name.lower()}_private_key.pem", "wb") as f:
        f.write(private_key.save_pkcs1("PEM"))


def load_public_key(name):
    with open(f"{name.lower()}_public_key.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    return public_key


def load_private_key(name):
    with open(f"{name.lower()}_private_key.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())

    return private_key
