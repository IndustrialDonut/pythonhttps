from flask import Flask 
from cryptography.fernet import Fernet
import base64

SECRET_KEY = "a" * 32
SECRET_MESSAGE = "fluffy tail"
app = Flask(__name__)

key = base64.urlsafe_b64encode(SECRET_KEY.encode())
my_cipher = Fernet(key)

@app.route('/')
def get_secret_message():
    return my_cipher.encrypt(SECRET_MESSAGE.encode())