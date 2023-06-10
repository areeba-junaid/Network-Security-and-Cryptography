def Encryption(user_data,key):
    encrypted=' '
    for letter in user_data:
        if (letter==' '):
            shifted=" "
        elif(letter.islower()):
                shifted=chr( ( ord (letter) + key -97 ) %26 + 97)
        elif(letter.isupper()):
                shifted=chr( ( ord (letter) + key -65 ) %26 + 65)
        
        encrypted =encrypted + shifted
    print("\n Your Encrypted message is: {} ".format(encrypted))
    return encrypted

def Decryption(send_message,key):
    decrypted=' '
    for letter in send_message:
        if (letter==' '):
            shifted=" "
        elif(letter.islower()):
                shifted=chr( (26 + (ord (letter) - key -97))%26 + 97)
        elif(letter.isupper()):
                shifted=chr( (26 + (ord (letter) - key -65))%26 + 65)
        decrypted =decrypted + shifted
    print("\n Your Decrypted message is: {} ".format(decrypted))
    print("\n===================================")
   

if __name__=="__main__":
    key=3
    print("==================================")
    user_data=input("\n Enter your data:    ")
    print("\n Your data is: {}".format(user_data) )
    print("==================================")
    send_message=Encryption(user_data,key)
    recieve_message=Decryption(send_message,key)
