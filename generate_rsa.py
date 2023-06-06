import requests
import re
import math
import sympy
import random
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

def get_url_content(def_url):
    # Get site content
    html_content = requests.get(def_url).text
    # Trim site content to 0s ans 1s only
    pattern = r"[01]"
    matches = re.findall(pattern, html_content)
    clean_text = "".join(matches)
    return clean_text

def get_inverse_mod(x,p):
    return pow(x, -1, p)

def find_p_q(p_q_len, trng_output):
    # Finding random p, q from the binary sequence
    # Generating them by assembling randomly found bits from the trng_output
    number = ""
    while len(number) < p_q_len:
        #number is a string here, composed of other strings = 0s and 1s
        number += str(random.choice(trng_output))
    # number_int is a converted number to int
    number_int = int(number, 2)
    prim_number = sympy.prevprime(number_int)
    return prim_number

def find_e(phi):
    f_e = 3
    while math.gcd(f_e, phi) != 1:
        # print("math.gcd(f_e, phi) != 1")
        # print("f_e: ", f_e)
        f_e += 1 
    # print("math.gcd(f_e, phi) == 1")
    # print("f_e: ", f_e)
    return f_e

def find_d(e, phi):
    d =  get_inverse_mod(e, phi)
    return d

def generate_rsa_keys(keylen):
    url = 'http://instaqram.pl/'
    trng_output = get_url_content(url)
    p_q_len = int (keylen / 2)
    p, q = 0, 0

    while p.bit_length() != p_q_len:
        p = find_p_q(p_q_len, trng_output)
    # print("p:", p)
    # print("bit length p: ", p.bit_length())

    while q.bit_length() != p_q_len:
        q = find_p_q(p_q_len, trng_output)
    # print("q:", q)
    # print("bit length q: ", q.bit_length())

    phi = (p - 1)*(q - 1)
    n = p*q
    e = find_e(phi)
    d = find_d(e, phi)

    private_key = rsa.RSAPrivateNumbers(
        p=p,
        q=q,
        d=d,
        dmp1=d % (p - 1),
        dmq1=d % (q - 1),
        iqmp=rsa.rsa_crt_iqmp(p, q),
        public_numbers=rsa.RSAPublicNumbers(e=e, n=n)
    ).private_key()

    public_key = rsa.RSAPublicNumbers(
        e=e,
        n=n,
    ).public_key()

    return private_key, public_key


########################################################

# Generate keys
private_key, public_key = generate_rsa_keys(2048)

# Convert private_key to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Convert public_key to PEM format
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write keys to file
with open('./A/keys/private_key.pem', 'wb') as f:
    f.write(private_pem)

with open('./A/keys/public_key.pem', 'wb') as f:
    f.write(public_pem)
