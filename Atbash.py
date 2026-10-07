print("Шифр Атбаш")
def create_atabash_cipher():
    # Создание шифра для английского алфавита
    eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    eng_cipher = eng_alphabet[::-1]  # Реверс алфавита
    # Создание шифра для русского алфавита
    rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    rus_cipher = rus_alphabet[::-1]  # Реверс алфавита
    return eng_alphabet, eng_cipher, rus_alphabet, rus_cipher
def encrypt_text(text, eng_alphabet, eng_cipher, rus_alphabet, rus_cipher):
    encrypted_text = []
    for char in text:
        if char.upper() in eng_alphabet:
            index = eng_alphabet.index(char.upper())
            encrypted_char = eng_cipher[index]
            encrypted_text.append(encrypted_char if char.isupper() else encrypted_char.lower())
        elif char in rus_alphabet:
            index = rus_alphabet.index(char)
            encrypted_text.append(rus_cipher[index])
        else:
            encrypted_text.append(char)  # Оставляем символ без изменений, если это не буква
    return ''.join(encrypted_text)
def decrypt_text(encrypted_text, eng_alphabet, eng_cipher, rus_alphabet, rus_cipher):
    decrypted_text = []
    for char in encrypted_text:
        if char.upper() in eng_cipher:
            index = eng_cipher.index(char.upper())
            decrypted_char = eng_alphabet[index]
            decrypted_text.append(decrypted_char if char.isupper() else decrypted_char.lower())
        elif char in rus_cipher:
            index = rus_cipher.index(char)
            decrypted_text.append(rus_alphabet[index])
        else:
            decrypted_text.append(char)  # Оставляем символ без изменений, если это не буква
    return ''.join(decrypted_text)
# Пример использования
if __name__ == "__main__":
    eng_alphabet, eng_cipher, rus_alphabet, rus_cipher = create_atabash_cipher()
    while True:
        message = input("Введите сообщение(ДЛЯ РУССКОГО-CAPSLOCK) для шифрования (или '.....' для выхода): ")
        if message.strip().upper() == ".....":
            print("Выход из программы.")
            break
        encrypted_message = encrypt_text(message, eng_alphabet, eng_cipher, rus_alphabet, rus_cipher)
        print("Зашифрованное сообщение:", encrypted_message)
        decrypted_message = decrypt_text(encrypted_message, eng_alphabet, eng_cipher, rus_alphabet, rus_cipher)
        print("Расшифрованное сообщение:", decrypted_message)
