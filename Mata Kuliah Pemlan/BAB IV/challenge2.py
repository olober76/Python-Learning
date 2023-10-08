def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
        else:
            encrypted_text += char
    return encrypted_text

sentence = "Praktikum Pemrograman Lanjut Teknik Komputer Kelas C"
key = 10
encrypted_sentence = encrypt(sentence, key)
print(encrypted_sentence)
