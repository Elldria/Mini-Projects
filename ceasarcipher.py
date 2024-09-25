

message = input('Enter text to encrypt here ----> ')
shift = int(input('Enter shift amount ----> '))



#Converts character to ascii value
converter = [ord(char) for char in message]
#Shifts letters by desired number
encryption = [e + shift for e in converter]

#converts numbers to characters
encrypted_text = [chr(number) for number in encryption]
text = ''.join(encrypted_text)
print(text)
#ocnverts character to ascii value
deconversion = [ord(char) for char in text]

#shifts back to original value
decryption = [d - shift  for d in deconversion]
#Converts value to character
decrypted_text = [chr(number) for number in decryption]
text = ''.join(decrypted_text)

print(text)

