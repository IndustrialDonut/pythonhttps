import requests
from cryptography import fernet
import base64

keyphrase = "a" * 32
key = base64.urlsafe_b64encode(keyphrase.encode())
#print(key)
cipher = fernet.Fernet(key)


def get_secret_message():
    url = 'http://10.0.0.42:5683'
    r = requests.get(url)
    #print(r.text)
    try:
        decrypted_message = cipher.decrypt(r.content)
        print(f"The codeword is: {decrypted_message}")
    except:
        print("Could not decrypt message, check that your symmetric key matches")


if __name__ == '__main__':
    get_secret_message()