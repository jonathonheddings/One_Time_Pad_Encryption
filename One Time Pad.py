#       #               #               #               #               #
#
#   The One Time Pad
#       The One Time Pad is a very simple encryption scheme that when ran using 
#   a properly random key, is extremely secure (it is not secure without a random key).
#   The encryption and decryption are actually the same function. First the key has to 
#   be exactly as long as the message. The message and the key are converted into binary
#   and the bitwise xor operation is applied, the result is taken as the cyphertext (or the
#   recovered plaintext if you are doing the operation to the cyphertext already)
#           
#
#       #               #               #               #               #

import math
import random

punctuation = {' ', ',', '.', '"', '\\', '\'', '\'', '/', '!', '@', '#', '$', '%', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '?', '~', '`', '<', '>'}
textfile = 'dummytext.txt'
test = 'test.txt'

# This function reads a plaintext file into a string
def read_plaintext(txtfile):
    filteredtext = ""
    with open(txtfile) as f:
        plaintext = f.readlines()
        for line in plaintext:
            for character in line.lower():
                if character != '\n': filteredtext += character
    return filteredtext


#### 
#    Here we create some functions for converting and working with binary bytes 
####

def seperate_binary(bin_string):
    count = 0
    store = ''
    lst = []
    for x in bin_string:
        count += 1
        store += x
        if(count == 7):
            lst.append(store)
            store = ''
            count = 0
    return lst

# This function converts text to binary for XOR operator
def text_to_binary(text):
    binary = ""
    for letter in text:
        if(letter in punctuation):
            binary += "0"
            #if letter == '\'': binary += '0'
            pass
        try:
            binary += (bin(ord(letter))[2:])
        except:
            print('ERROR: TEXT HAS ILLEGAL CHARACTERS')
            return None
    return binary


# This function converts an appropriate binary string into a string of 
def binary_to_text(binary):
    lst = seperate_binary(binary)
    message = ''
    for byte in lst:
        n = 6
        store = 0
        for x in byte:
            store += int(x) * (2**n)
            n -= 1
        message += chr(store)
    return message


# This function returns the bitwise exclusive or of a given byte in string form
def byte_xor(byte1, byte2):
    store = ''
    for i in range(len(byte1)):
        store += str((int(byte1[i]) + int(byte2[i])) % 2)
    return store


# This function generates a key of equal length to the message, IT IS INSECURE, 
#       and by using it as your keygen for the One Time Pad, you are vulnerable 
#       to attacks on RNG based keygen systems
def generate_key(message):
    key = ''
    for bin in text_to_binary(message):
        key += str(random.randint(0, 1))
    return key



#### 
#    Here we create some functions to encrypt and decrypt One Time Pads 
####

# This function encrypts the plaintext file with the key; it accepts text for a plaintext only
#   (if you want to encrypt binary use the decrypt function), and both text and binary keys
#   Then it makes sure everything is the right size and performs the bitwise xor to encrypt
def otp_encrypt(plaintext, key):
    # Checks whether or not the key is already in binary form for initialization 
    #       of the lists containing the binary bytes
    if(len(plaintext) != len(key)):
        if(len(key) % len(plaintext) == 0):
            key_bin = seperate_binary(key)
    else:
        key_bin = seperate_binary(text_to_binary(key))   
    plain_bin = seperate_binary(text_to_binary(plaintext))
    
    # The xor operation is applied to each byte and returned
    cyphertext = ''
    for i in range(len(plain_bin)):
        cyphertext += byte_xor(plain_bin[i], key_bin[i])

    # Returns the cyphertext in binary
    return cyphertext


# This function decrypts the cyphertext using a known key
#   It is virtually the same as the encrypt function because modulo 2 addition
#   will bring back the message by adding the key to the cyphertext. The only 
#   difference is that it only accepts a binary text, but it accepts text or binary keys
def otp_decrypt(cyphertext, key):
    if(len(cyphertext) != len(text_to_binary(key))):
        if(len(key) % len(cyphertext) == 0):
            key_bin = seperate_binary(key)
    else:
        key_bin = seperate_binary(text_to_binary(key))   
    cyph_bin = seperate_binary(cyphertext)

    cyphertext = ''
    for i in range(len(cyph_bin)):
        cyphertext += byte_xor(cyph_bin[i], key_bin[i])
    return cyphertext
 

# This is a test. It takes a string input and generates a binary key of equal size, runs 
#       the algorithm and then runs it again in reverse to decrypt
if(__name__ == "__main__"):
    a = '"The Big Oxmox advised her not to do so, because there were thousands of bad Commas"'
    b = generate_key(a)
    print('Encrypting The Following: ', a, '\n') 
    print('Result: ', otp_encrypt(a,b))