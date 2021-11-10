# One Time Pad Message Encryption
This python program provides functions for One Time Pad encryption on text files and messages.

---
### Overview of The Encryption    
  The One Time Pad is a very simple encryption scheme that when ran using 
   a properly random key, is extremely secure (it is not secure without a random key).
   The encryption and decryption are actually the same function. First the key has to 
   be exactly as long as the message. The message and the key are converted into binary
   and the bitwise xor operation is applied, the result is taken as the cyphertext (or the
   recovered plaintext if you are doing the operation to the cyphertext already)

#### OTP Encryption Function
```python
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

```

This function when ran on a message will return an encrypted string of binary. The decryption function works
in exactly the same way, except that it accepts binary strings as input instead of text only like the encryption function. However, both functions accept keys that are text or binary. 

Here is some test code for the OTP functions:

```
    a = '"The Big Oxmox advised her not to do so, because there were thousands of bad Commas"'
    b = generate_key(a)
    print('Encrypting The Following: ', a, '\n') 
    print('Key: ', b, '\n')
    print('Result: ', otp_encrypt(a,b), '\n')
    print('Trying to Read: ', binary_to_text(otp_encrypt(a,b)))
    print('Converted Back: ', binary_to_text(otp_decrypt(otp_encrypt(a,b), b)))
```
And here is the output from it:

```
Encrypting The Following:  "The Big Oxmox advised her not to do so, because there were thousands of bad Commas" 

Key:  1000100110001110100011101011101101111000010011000101011101000100001010011110111011111111101100111111001000000110001011111110111010110010001
0011010111010111100010010101010111100000011010001011000010100010001000101000101001101111111110110001100000000000100001100000001010100110111111110
1010101111111010010111011010111101011101101111001111110010111001111011010111001011111000011010100101110101011010111110111000111011100011010001110
1101011011001111011011100110111011001110011101001010111001010000101001101001110000100011101000011110001100000000101110101100011100011011000001100
01010010000101

Result:  0011001010101001011100010100001100010000010111010111000100110100011101010001010010010101010111011001000101000111101001010111011010
1101000011010000010011100110100001001011001011010010101000111001001100011011101001110010111100100001100001110001000010000000011010100010111
1000011000110101110111110101100011101111110001010110110010001010001011111011111101000010001111110100011000110000000011010101100110011010000
0110000100100110101110001110000100011010111110100001011110101111000010000000110101011010100010010010000001011010010000100001001111101010011
01011100111111110100010010100011000101100

Trying to Read:  ♂cvY}♦T bKG;3!♥dd'P.,u↔3@J♠^dd▬∟/lIJ|_Z☻oC/<☻9@Q]☼ ◄`GhvrA‼☻$♠§5K;↔&oe☺^+O)?H2

Converted Back:  "The Big Oxmox advised her not to do so, because there were thousands of bad Commas"
```
