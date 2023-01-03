import rsa
import common


# Bill and Jill generate key pairs
common.generate_key_pair("Bill")
common.generate_key_pair("Jill")

# Load keys
bills_public_key = common.load_public_key("Bill")
bills_private_key = common.load_private_key("Bill")

# Bill writes a message to Jill.
bills_message = "I love you!"

# Bill wants to sign the message so that Jill can be sure it's from him and has not been altered

# Create a hash value from the message
hash_value = rsa.compute_hash(bills_message.encode(), 'SHA-256')

# Sign the hash value
signature = rsa.sign_hash(hash_value, bills_private_key, 'SHA-256')

# Altenative: Make compute_hash() and sign_hash() in one step
same_signature = rsa.sign(bills_message.encode(), bills_private_key, 'SHA-256')

try:
    # Jill receives the message and verifies its signature using Bill's public key
    result = rsa.verify(bills_message.encode(), signature, bills_public_key)
    print(result)  # If verification succeeds, verify() returns 'SHA-256'
except rsa.pkcs1.VerificationError:
    print("VerificationError")

# If someone changes the message before Jill reads it, the verify method will fail.
