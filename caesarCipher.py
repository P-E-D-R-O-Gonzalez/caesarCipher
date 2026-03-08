# CaesarCipher .py - Encrypts and decrypts messages using the Caesar cipher.

dic = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}

def encrypt(array,key):
    enc = "" # holds the encrypted message
    for letter in array: # goes over each letter in the message
        if letter.isalpha():
            if letter in dic.values(): # checks if it a valid letter
                for index, ltr in dic.items(): # get the letter's index and value
                    if ltr == letter:
                        enc += dic[(index + key) % 26] # shift the letter by the key value and add it to the encrypted message
            else:
                enc += letter
        else:
            enc += letter
    return enc


def decrypt(array):
    for i in range(25): # brute forces all possible key values
        potential = ""
        for letter in array: # goes over each letter in the message
            if letter.isalpha():
                if letter in dic.values(): # checks if it a valid letter
                    for index, ltr in dic.items(): # get the letter's index and value
                        if ltr == letter:
                            potential += dic[(index - i) % 26] # shift the letter by the key value and add it to the encrypted message
                else:
                    potential += letter
            else:
                potential += letter

        print("Key: " + str(i) + " Message: " + potential) # print the potential message for the current key value


def decryptWithKey(array,key):
    return encrypt(array,-key)
    # your subtracting key from index to get OG msg so we reverse it

def main():
    print("Caesar Cipher Program\n")
    action = input("Encrypt/Decrpyt enter D or E: ")
    if action.upper() == "E":
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        ltrsOfMSG = list(message.upper())
        print(encrypt(ltrsOfMSG,shift))
    elif action.upper() == "D":
        ciphertext = input("Enter the message to decrypt: ")
        ltrsOfCipher = list(ciphertext.upper())
        ask = input("Do you happen to know the key already? (Y/N): ")
        if ask.upper() == "Y":
            key = int(input("Enter the key value: "))
            print(decryptWithKey(ltrsOfCipher,key))
        else:
            decrypt(ltrsOfCipher)


main()
