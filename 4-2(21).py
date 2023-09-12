# RSA
# !pip install pycryptodome

import binascii

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

keyPair = RSA.generate(2023)

print("public key generating ... ")
pubKey = keyPair.publickey()
print(f"  n =  { hex(pubKey.n)}")
print(f"  e =  { hex(pubKey.e)}")
pubKeyREM = pubKey.exportKey()
#print(pubKeyPEM.decode('ascii))

print("private key generating ...")
print(f"  d =  { hex(keyPair.d)}")
privKeyPEM = keyPair.exportKey()
#print(pubKeyPEM.decode('ascii))

msg = input("plaintext : ")
plaintext = bytes(msg, 'utf-8')
encryptor = PKCS1_OAEP.new(pubKey)
ciphertext = encryptor.encrypt(plaintext)
print("cipher text : ", binascii.hexlify(ciphertext))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(ciphertext)
print('original text :', decrypted)