import requests

def get_secret_message():
    #url = 'http://10.0.0.42:5683'
    #url = 'https://10.0.0.42:5683'
    url = 'https://localhost:5683'


    response = requests.get(url, verify='certs/ca.crt')
    #response = requests.get(url, verify='certs/ca-public-key.pem')
    print(f"The secret message is: {response.text}")


if __name__ == '__main__':
    get_secret_message()