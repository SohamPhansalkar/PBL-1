import hashlib

def encrypt_password(password):
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest()