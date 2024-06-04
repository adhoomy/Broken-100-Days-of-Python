alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cipher_text = []
    for letter in text:
        cipher_text.append(alphabet[(alphabet.index(letter)+shift)%26])
    final_cipher = str()
    for letter in cipher_text:
        final_cipher += letter
    print(f"The encoded text is {final_cipher}")

def decrypt(text, shift):
    decipher_text = []
    for letter in text:
        decipher_text.append(alphabet[(alphabet.index(letter)-shift)%26])
    final_decipher = str()
    for letter in decipher_text:
        final_decipher += letter
    print(f"The decoded text is {final_decipher}")

def keepGoing(choice):
    if choice == "yes":
        return True
    elif choice == "no":
        return False
    else:
        choice = (input('Would you like to continue encoding or decoding, please type "yes" or "no":\n')).lower()
        return keepGoing(choice)

go = True
while go==True:
    direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')
    if direction=="encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
        choice = (input('Would you like to continue encoding or decoding, please type "yes" or "no":\n')).lower()
        go=keepGoing(choice)
    elif direction=="decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
        choice = (input('Would you like to continue encoding or decoding, please type "yes" or "no":\n')).lower()
        go=keepGoing(choice)
    else:
        direction = input('Type "encode" to encrypt, type "decode" to decrypt:\n')