import requests
# from bs4 import BeautifulSoup

# url = 'http://instaqram.pl/'
# html_content = requests.get(url).text

# soup = BeautifulSoup(html_content, 'html.parser')
# clean_text = soup.get_text()

# # Delete unwanted parts to generate clean output form given url (final encoded trng)
# unwanted_parts = ["<br>", "</main>", "</body>", "</html>","\n"]
# for part in unwanted_parts:
#     clean_text = clean_text.replace(part, "")

# # print(clean_text)
# # print(len(clean_text), type(clean_text))

import re
import math
import sympy
import random

url = 'http://instaqram.pl/'

def get_url_content(def_url):
    # Pobranie zawartosci ze strony
    html_content = requests.get(def_url).text
    # Obróbka zawartosci to pozadanego formatu (obciecie niepotzrebnych znakow)
    pattern = r"[01]"
    matches = re.findall(pattern, html_content)
    clean_text = "".join(matches)
    return clean_text

def get_gcd(a,b):
    return math.gcd(a,b)

def get_inverse_mod(x,p):
    return pow(x, -1, p)

def get_previous_prime_num(x):
    return sympy.prevprime(x)

def find_p_q(keylen):
    print("tbd")
    # Finding random p, q from the binary sequence
    # Generating them by assembling randomly found bits from the clean_text
    # for bit in range():
        #jfjffj

# example with Bob and Alice; rsa module

# Bob generates a key pair, and gives the public key to Alice. This is done such that Alice knows for sure that the key is really Bob’s 
# (for example by handing over a USB stick that contains the key).
import rsa
(bob_pub, bob_priv) = rsa.newkeys(512)

#Alice writes a message, and encodes it in UTF-8. The RSA module only operates on bytes, and not on strings, so this step is necessary.
message = 'hello Bob!'.encode('utf8')

#Alice encrypts the message using Bob’s public key, and sends the encrypted message.
import rsa
crypto = rsa.encrypt(message, bob_pub)

#Bob receives the message, and decrypts it with his private key.
message = rsa.decrypt(crypto, bob_priv)
print(message.decode('utf8'))
#hello Bob!

# text to bin
x = "01000111....1010"  # Twoja zmienna binarna
liczba_binarna = int(x, 2)
print(liczba_binarna)

# generowanie p,q
for bit in range(key_len):
    number+=clean_text[[random.randint(0, len(clean_text)) - 1]]
# nastepnie konwersja do bin

#  Na końcu kod zwraca klucz publiczny (para liczb e i n) oraz klucz prywatny (para liczb d i n)
    # publicKey = (e, n)
    # privateKey = (d, n)
publicKey = rsa.RSAPublicNumbers(
        e=e,
        n=n
    ).public_key()
privateKey = rsa.RSAPrivateNumbers(
        d=d,
        n=n
    ).private_key()