import rsa
import common


# Bill and Jill generate key pairs
common.generate_key_pair("Bill")
common.generate_key_pair("Jill")

# Load keys
jills_public_key = common.load_public_key("Jill")
jills_private_key = common.load_private_key("Jill")

# Bill writes a message to Jill
bills_message = "I love you!"

# Bill uses Jill's public key to encrypt his message
bills_encrypted_message = rsa.encrypt(bills_message.encode(), jills_public_key)

# Jill receives Bill's encrypted message and decrypts it using her private key
bills_decrypted_message = rsa.decrypt(bills_encrypted_message, jills_private_key).decode()

# Jill can now respond by encrypting her message using Bill's public key
