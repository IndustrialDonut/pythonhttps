import os
import requests

def get_secret_message():
    url = 'http://10.0.0.42:5683' #os.environ['SECRET_URL']
   # url = 'http://127.0.0.1:5683'
    response = requests.get(url)
    print(f"The secret message is: {response.text}")


if __name__ == '__main__':
    get_secret_message()