# AES
from Crypto.Cipher import AES

key = b'1234567890abcdef' # 16 bytes
cipher1 = AES.new(key, AES.MODE_EAX)

nonce = cipher1.nonce

msg = input("plaintext : ")
plaintext = bytes(msg, 'utf-8')
ciphertext = cipher1.encrypt(plaintext)
print('ciphertext : ', ciphertext)

cipher2 = AES.new(key, AES.MODE_EAX, cipher1.nonce)
print("decrypting ...", cipher2.decrypt(ciphertext))
2