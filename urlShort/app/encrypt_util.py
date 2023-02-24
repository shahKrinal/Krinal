import hashlib
import base64
from cryptography.fernet import Fernet


def encrypt(password, data):
    password = password
    password_in_bytes = bytes(password, "utf-8")
    m = hashlib.md5(password_in_bytes).hexdigest()
    key = base64.urlsafe_b64encode(m.encode('utf-8'))
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode("ascii"))
    encrypted_data = base64.urlsafe_b64encode(encrypted_data).decode("ascii")
    return encrypted_data


def decrypt(password, data):
    password = password
    password_in_bytes = bytes(password, "utf-8")
    data = base64.urlsafe_b64decode(data)
    m = hashlib.md5(password_in_bytes).hexdigest()
    key = base64.urlsafe_b64encode(m.encode('utf-8'))
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data).decode("ascii")
    return decrypted_data
