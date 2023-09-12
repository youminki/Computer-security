# affine cipher
# E(x) = (ax + b)mod m
# m : size of the alphabet
# (a, b) : keys of the cipher
def egcd(a, b):
    x, y, u, v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
    
def encrypt(text, key):
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])
def decrypt(cipher, key):
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])
msg = input("plaintext : ")
key = [7, 20] # key값을 바꿔보며 프로그램이 어떻게 작동하는지 확인해 보자.
enc_text = encrypt(msg, key)
print('ciphertext : {}'.format(enc_text))
print('decrypted text : {}'.format(decrypt(enc_text, key)))


#======================================================
# 주석추가 버전

# Affine 암호화 및 복호화를 위한 코드입니다.
# Affine 암호는 다음과 같은 수식으로 텍스트를 암호화하고 복호화합니다:
# E(x) = (ax + b) mod m
# 여기서,
# - x는 평문의 각 문자를 나타냅니다.
# - a와 b는 암호화 및 복호화에 사용되는 키입니다.
# - m은 알파벳의 크기를 나타냅니다 (예: 26, 알파벳의 경우).

# 확장 유클리드 알고리즘을 사용하여 역 모듈로 역을 찾습니다.
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y
# 모듈로 역을 계산합니다.
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m
# 평문을 암호화합니다.
def encrypt(text, key):
    text = text.upper().replace(' ', '') # 평문을 대문자로 변환하고 공백을 제거합니다.
    encrypted_text = '' # 암호화된 결과를 저장할 빈 문자열을 초기화합니다.
    # 평문의 각 문자를 암호화합니다.
    for char in text:
        encrypted_char = (key[0] * (ord(char) - ord('A')) + key[1]) % 26 # 각 문자를 ASCII 값으로 변환한 후 'A'의 ASCII 값을 빼고, 키를 적용하여 암호화합니다.
        encrypted_text += chr(encrypted_char + ord('A')) # 암호화된 문자를 다시 대문자 알파벳으로 변환하고 결과에 추가합니다.
    return encrypted_text
# 암호문을 복호화합니다.
def decrypt(cipher, key):
    decrypted_text = '' # 복호화된 결과를 저장할 빈 문자열을 초기화합니다.
    # 암호문의 각 문자를 복호화합니다.
    for char in cipher:
        decrypted_char = (modinv(key[0], 26) * (ord(char) - ord('A') - key[1])) % 26 # 각 문자를 ASCII 값으로 변환한 후 'A'의 ASCII 값을 빼고, 역 모듈로와 키를 적용하여 복호화합니다.
        decrypted_text += chr(decrypted_char + ord('A')) # 복호화된 문자를 다시 대문자 알파벳으로 변환하고 결과에 추가합니다.
    return decrypted_text
msg = input("plaintext : ") # 사용자로부터 평문을 입력 받습니다.
key = [7, 20] # 암호화에 사용할 키를 설정합니다.
enc_text = encrypt(msg, key) # 입력된 평문을 설정된 키를 사용하여 암호화합니다.
print('ciphertext : {}'.format(enc_text)) # 암호화된 결과를 출력합니다.
dec_text = decrypt(enc_text, key) # 암호문을 다시 복호화하여 원래 평문을 복원합니다.
print('decrypted text : {}'.format(dec_text)) # 복호화된 결과를 출력합니다.
