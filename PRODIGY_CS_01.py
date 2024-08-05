def encrypt(text,s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + shift -65) % 26 + 65)

        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

text = input('Enter Message : ')
shift = 4
encryptedText = encrypt(text,shift)
print ("Encrypted Message : " + encryptedText)

text = encryptedText
shift = -4
decryptedText = encrypt(text,shift)
print ("decrypted Message : " + decryptedText)


