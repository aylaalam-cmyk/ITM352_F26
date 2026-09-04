from cryptography.fernet import Fernet

key = Fernet.generate_key()
cypher_suite = Fernet(key)

encoded_text = cypher_suite.encrypt(b"Hello World")
print("Encoded text:", encoded_text)
decoded_text = cypher_suite.encrypt(encoded_text)
print("decoded text:", decoded_text)