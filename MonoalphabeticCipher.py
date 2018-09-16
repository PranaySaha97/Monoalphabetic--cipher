monoalpha_cipher = {
    'a': 'm',
    'b': 'n',
    'c': 'b',
    'd': 'v',
    'e': 'c',
    'f': 'x',
    'g': 'z',
    'h': 'a',
    'i': 's',
    'j': 'd',
    'k': 'f',
    'l': 'g',
    'm': 'h',
    'n': 'j',
    'o': 'k',
    'p': 'l',
    'q': 'p',
    'r': 'o',
    's': 'i',
    't': 'u',
    'u': 'y',
    'v': 't',
    'w': 'r',
    'x': 'e',
    'y': 'w',
    'z': 'q',
    ' ': ' ',
}

inverse_monoalpha_cipher = {}
for key, value in monoalpha_cipher.items():
    inverse_monoalpha_cipher[value] = key

#Encryption

message = "Hello! I am pranay "
message.lower()
encrypted_message = []
for letter in message:
    encrypted_message.append(monoalpha_cipher.get(letter, letter))

print(''.join(encrypted_message))

#Decryption

encrypted_message = "rmij'u uamu xyj?"
decrypted_message = []
for letter in encrypted_message:
     decrypted_message.append( inverse_monoalpha_cipher.get(letter, letter))

print(''.join( decrypted_message ))
