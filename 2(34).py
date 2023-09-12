def vigenere(message, key):
    message = message.lower()
    message = message.replace(' ', '')
    m = len(key)
    cipher_text = ' '
    for i in range(len(message)):
        letter = message[i]
        k = key[i % m]
        cipher_text += chr ((ord(letter) - 97 + k) % 26 + 97)
        
    return cipher_text
msg = input("plaintext : ")
key = input("key : ")

key = [ord(letter) - 97 for letter in key]
ciphertext = vigenere(msg, key)
print('cipher text : ', ciphertext)

key = [-1 * k for k in key]
plaintext = vigenere(ciphertext, key)
print('Plain text : ', plaintext)




#======================================================
# 주석추가 버전

# 주어진 메시지를 비즈네르 암호를 사용하여 암호화하는 함수입니다.
def vigenere(message, key):
    message = message.lower() # 메시지를 모두 소문자로 변환합니다.
    message = message.replace(' ', '') # 메시지에서 공백을 제거합니다.
    m = len(key)  # 암호화 키의 길이를 저장합니다.
    cipher_text = ' '  # 암호화된 결과를 저장할 빈 문자열을 초기화합니다.
    for i in range(len(message)):
        letter = message[i]  # 현재 문자를 가져옵니다.
        k = key[i % m]  # 암호화 키에서 현재 위치에 해당하는 키를 가져옵니다.
        # 암호화를 수행하고 결과를 결과 문자열에 추가합니다.
        # 각 문자를 'a' (ASCII 97)를 기준으로 시프트하고, 키를 더한 뒤, 26으로 나눈 나머지를 구합니다.
        # 마지막으로 다시 'a'를 더하여 알파벳 문자로 변환합니다.
        cipher_text += chr((ord(letter) - 97 + k) % 26 + 97)
    return cipher_text  # 암호화된 결과를 반환합니다.

msg = input("plaintext : ") # 사용자로부터 평문을 입력받습니다.
key = input("key : ") # 사용자로부터 암호화 키를 입력받습니다.

key = [ord(letter) - 97 for letter in key] # 입력된 키를 ASCII 값으로 변환하고 'a' (ASCII 97)를 빼서 키를 숫자 리스트로 변환합니다.
ciphertext = vigenere(msg, key) # 입력된 평문을 설정된 암호화 키를 사용하여 암호화합니다.
print('cipher text : ', ciphertext) # 암호화된 결과를 출력합니다.

key = [-1 * k for k in key] # 복호화를 위해 키를 반전합니다.
plaintext = vigenere(ciphertext, key) # 암호문을 다시 복호화하여 원래 평문을 복원합니다.
print('Plain text : ', plaintext) # 복호화된 결과를 출력합니다.
