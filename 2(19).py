#shift cipher
def encrypt(text, key):
    result = " "
    #transverse the plain text
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result

msg = input("plaintext : ")
key = input("key : ")
ciphertext = encrypt(msg, int(key))
print(ciphertext)








#======================================================
# 주석추가 버전
    # Shift Cipher(시저 암호)를 사용하여 주어진 문자열을 암호화하는 함수입니다.
def encrypt(text, key):
    result = " "  # 결과 문자열을 초기화합니다.
    # 주어진 문자열을 한 문자씩 순회합니다.
    for i in range(len(text)):
        char = text[i]  # 현재 문자를 가져옵니다.
        if char.isupper():  # 만약 현재 문자가 대문자라면:
            result += chr((ord(char) + key - 65) % 26 + 65)  # 대문자 알파벳을 시프트하고 결과에 추가합니다.
        else:  # 그렇지 않으면 (소문자인 경우):
            result += chr((ord(char) + key - 97) % 26 + 97)  # 소문자 알파벳을 시프트하고 결과에 추가합니다.
    return result  # 암호화된 결과 문자열을 반환합니다.