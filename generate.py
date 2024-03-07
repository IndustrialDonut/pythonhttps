from pki_helpers import generate_private_key, generate_public_key, generate_csr


ca_private_key = generate_private_key('ca-private-key.pem', 'secret_password')
generate_public_key(
    private_key=ca_private_key,
    filename='ca.crt',
    country='US',
    state='CA',
    locality='LA',
    org='DONUT CA',
    hostname='donut-ca.com',
)

# generate_csr(
#     private_key=ca_private_key,
#     filename='ca.csr',
#     country='US',
#     state='CA',
#     locality='LA',
#     org='DONUT CA',
#     hostname='donut-ca.com',
#     alt_names=['localhost', 'doesthismatter'],
# )


server_private_key = generate_private_key('server-private-key.pem', 'server_password')
generate_csr(
    private_key=server_private_key,
    filename='server.csr',
    country='US',
    state='CA',
    locality='LA',
    org='DONUT SERVER',
    alt_names=['localhost', 'donutserver', '10.0.0.42', 'etc'],
    hostname='donut-server.com',
)

