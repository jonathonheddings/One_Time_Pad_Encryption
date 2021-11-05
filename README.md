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
```
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
