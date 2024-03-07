from cryptography import x509
from cryptography.hazmat.backends import default_backend

server_csr_file = open('server.csr', 'rb')
csr = x509.load_pem_x509_csr(server_csr_file.read(), default_backend())

# ca_csr_file = open('ca.csr', 'rb')
# ca_csr = x509.load_pem_x509_csr(ca_csr_file.read(), default_backend())

ca_public_key_file = open('ca.crt', 'rb')
ca_public_key = x509.load_pem_x509_certificate(ca_public_key_file.read(), default_backend())

from getpass import getpass
from cryptography.hazmat.primitives import serialization

ca_private_key_file = open('ca-private-key.pem', 'rb')
ca_private_key = serialization.load_pem_private_key(
    ca_private_key_file.read(),
    getpass().encode('utf-8'),
    default_backend(),
)

from pki_helpers import sign_csr
sign_csr(csr, ca_public_key, ca_private_key, 'server.crt')
#sign_csr(ca_csr, ca_public_key, ca_private_key, 'ca.crt')