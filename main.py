from цезарь import caesar_decrypt

ciphertext = "F xj fk x cfib"
# Сюда свой текст надо
shift = 3
#На сколько букв
plaintext = caesar_decrypt(ciphertext, shift)
print(plaintext)
