# DES
# !pip uninstall pycrypto
# !pip install pycryptodome

from Crypto.Cipher import DES

key = b'12345678' # 8 bytes
iv = b'12345678'
cipher1 = DES.new(key, DES.MODE_CFB, iv)

msg = input("plaintext : ")
plaintext = bytes(msg, 'utf-8')
ciphertext = cipher1.encrypt(plaintext)
print('ciphertext : ', ciphertext)

cipher2 = DES.new(key, DES.MODE_CFB, iv)
print("decryting ...", cipher2.decrypt(ciphertext))