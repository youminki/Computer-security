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

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
for key in range(len(LETTERS)):
    translated = ' '
    for symbol in ciphertext:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num -= key
            if num < 0:
                num += len(LETTERS)
            translated += LETTERS[num]
        else:
            translated += symbol
    print('hacking key #%s: %s' % (key, translated))
    
    
    
    
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

msg = input("plaintext: ") # 사용자로부터 평문을 입력받습니다.
key = input("key: ") # 사용자로부터 시프트 키를 입력받습니다.
ciphertext = encrypt(msg, int(key)) # 입력된 평문을 주어진 키를 사용하여 암호화합니다.
print(ciphertext) # 암호화된 결과를 출력합니다.

LETTERS = 'abcdefghijklmnopqrstuvwxyz'  # 소문자 알파벳을 포함하는 문자열을 정의합니다.
# 가능한 모든 시프트 키에 대해 복호화를 시도합니다.
for key in range(len(LETTERS)):
    translated = ' '  # 복호화된 문자열을 초기화합니다.
    for symbol in ciphertext:  # 암호문을 한 문자씩 순회합니다.
        if symbol in LETTERS:  # 문자가 소문자 알파벳에 속한다면:
            num = LETTERS.find(symbol)  # 문자의 인덱스(0부터 25까지)를 찾습니다.
            num -= key  # 시프트된 위치를 역으로 계산합니다.
            if num < 0:  # 만약 음수라면 (알파벳 끝에서 반대 방향으로 넘어갔다면):
                num += len(LETTERS)  # 알파벳 길이를 더해 원래 위치로 되돌립니다.
            translated += LETTERS[num]  # 복호화된 문자를 결과에 추가합니다.
        else:  # 문자가 소문자 알파벳에 속하지 않는다면 (특수문자 등):
            translated += symbol  # 그대로 결과에 추가합니다.
    # 현재 시프트 키로 복호화한 결과를 출력합니다.
    print('hacking key #%s: %s' % (key, translated))
