def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Определение номера буквы в алфавите (0-25)
            char_code = ord(char.lower()) - ord('a')
            # Вычисление нового номера буквы после сдвига
            new_code = (char_code - shift) % 26
            # Преобразование номера буквы в символ
            new_char = chr(new_code + ord('a'))
            # Добавление символа в расшифрованный текст
            plaintext += new_char
        else:
            # Несимвольные символы (например, пробелы) не меняются
            plaintext += char
    return plaintext
