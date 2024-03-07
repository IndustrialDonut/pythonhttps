from pki_helpers import generate_private_key, generate_public_key, generate_csr


ca_private_key = generate_private_key('ca-private-key.pem', 'secret_password')
generate_public_key(
    private_key=ca_private_key,
    filename='ca-public-key.pem',
    country='US',
    state='CA',
    locality='LA',
    org='donut',
    hostname='donut.com',
)


server_private_key = generate_private_key('server-private-key.pem', 'server_password')
generate_csr(
    private_key=server_private_key,
    filename='server-csr.pem',
    country='US',
    state='CA',
    locality='LA',
    org='donut',
    alt_names=['10.0.0.42'],
    hostname='donut.com',
)

