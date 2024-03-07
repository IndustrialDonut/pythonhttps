from pki_helpers import generate_private_key, generate_public_key, generate_csr


private_key = generate_private_key('server-private-key.pem', 'server_password') # secret_password for CA and server_password for SERVER 's private keys on disk

generate_csr(
    private_key=private_key,
    filename='server-csr.pem',
    country='US',
    state='CA',
    locality='LA',
    org='donut',
    alt_names=['10.0.0.42'],
    hostname='donut.com',
)

generate_public_key(
    private_key=private_key,
    filename='ca-public-key.pem',
    country='US',
    state='CA',
    locality='LA',
    org='donut',
    hostname='donut.com',
)