# substitution cipher
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = "fcpevqkzgmtrayonujdlwhbxsi"

def encrypt(text, key ):
    result = " "
    for letter in text:
        if letter.lower() in alphabet:
            result += key[alphabet.find(letter.lower())]
        else:
            result += letter
    return(result)

msg = input("plaintext : ")
print(encrypt(msg, key))



#======================================================
# 주석추가 버전

alphabet = 'abcdefghijklmnopqrstuvwxyz' # 알파벳 소문자를 나타내는 문자열입니다.
key = "fcpevqkzgmtrayonujdlwhbxsi" # 치환 암호에 사용할 치환 키(key)입니다.

# 주어진 키를 사용하여 평문을 암호화하는 함수입니다.
def encrypt(text, key):
    result = " "  # 암호화된 결과를 저장할 빈 문자열을 초기화합니다.
    
    for letter in text:
        if letter.lower() in alphabet:  # 입력 문자가 알파벳인 경우만 처리합니다.
            index = alphabet.find(letter.lower())  # 입력 문자의 알파벳 인덱스를 찾습니다.
            encrypted_letter = key[index]  # 치환 키를 사용하여 암호화된 문자를 찾습니다.
            result += encrypted_letter  # 암호화된 문자를 결과 문자열에 추가합니다.
        else:
            result += letter  # 입력 문자가 알파벳이 아닌 경우 그대로 결과 문자열에 추가합니다.
    
    return result  # 암호화된 결과를 반환합니다.

msg = input("plaintext : ") # 사용자로부터 평문을 입력받습니다.
encrypted_msg = encrypt(msg, key) # 입력된 평문을 설정된 치환 키를 사용하여 암호화합니다.
print(encrypted_msg) # 암호화된 결과를 출력합니다.
