#This is a program intended to encrypt and decrypt a message with a caeser cipher

#Going to ask a user to decide between encrypting or decrypting


def main():
    choice = input("Would you like to encrypt or decrypt a message? \n Press 1 for encrypt and 2 for decrypt")
    choice = int(choice)
    if choice == 1:
        encrypt()
    elif choice == 2:
        x = input("Would you like to decrypt with key or brute-force it? Press 1 for key and 2 for brute-force")
        x = int(x)
        if x == 1:
            decrypt()
        elif x == 2:
            brute_force()
    else:
        print("Please enter a valid choice")

def encrypt():
    plainttext = input("Enter the message you would like to encrypt")
    key = input("Enter the key you would like to use (0-25)")
    key = int(key)
    ciphertext = ""
    for character in plainttext:
        if character.isalpha():
            if character.isupper():
                ciphertext += chr((ord(character) + key - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(character) + key - 97) % 26 + 97)
        else:
            ciphertext += character
    print(ciphertext)

def decrypt():
    ciphertext = input("enter the message would would like to decrypt")
    key = input("Enter the key used (0-25)")
    key = int(key)
    plaintext = ""
    for character in ciphertext:
        if character.isalpha():
            if character.isupper():
                plaintext += chr((ord(character) - key - 65) % 26 + 65)
            else:
                plaintext += chr((ord(character) - key - 97) % 26 + 97)
        else:
            plaintext += character
    print(plaintext)

def brute_force():
    ciphertext = input("enter the message would would like to decrypt")
    plaintext = ""
    for key in range(26):
        plaintext = ""
        for character in ciphertext:
            if character.isalpha():
                if character.isupper():
                    plaintext += chr((ord(character) - key - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(character) - key - 97) % 26 + 97)
            else:
                plaintext += character
        print(plaintext)

if __name__ == "__main__":
    main() 