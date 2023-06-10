def generate_key(user_message):
    keyword="012"
    index=0
    generated_key=""
    for i in user_message:
        index=(index+(len(keyword)-1)+1)%(len(keyword))
        if(i==" "):
           generated_key=generated_key + " "
           index=index-1
        else:
            generated_key=generated_key + (keyword[index])
        index=index+1
    return generated_key
def Encryption(message,key):

    encrypted_message=''
    for i in range(len(key)):
        if(key[i] == " "):
            encrypted_message=encrypted_message + " "
        else:
            index=ord(message[i])-65
            encrypted_message=encrypted_message + Monoalphabetic_ciphers[int(key[i])][index]
    return encrypted_message
def Decryption(message,key):

    decrypted_message=''
    for i in range(len(key)):
        if(key[i] == " "):
            decrypted_message=decrypted_message + " "
        else:
             index= Monoalphabetic_ciphers[int(key[i])].index(message[i])
             decrypted_message=decrypted_message + chr(index+65)
    return decrypted_message
if __name__=="__main__":
    Monoalphabetic_ciphers=[['K','D','N','H','P','A','W','X','C','Z','I','M','Q','J','B','Y','E','T','U','G','V','R','F','O','S','L'],
    ['P','A','G','U','K','H','J','B','Y','D','S','O','E','M','Q','N','W','F','Z','I','T','C','V','L','X','R'],
    ['J','M','F','Z','R','N','L','D','O','W','G','I','A','K','E','S','U','C','Q','V','H','Y','X','T','P','B']]
    print("==================================")
    user_data=input("\n Enter Your Data: ")
    print("\n Your Data Is: {}".format(user_data) )
    print("==================================")
    print("-----------------------------------")
    key=generate_key(user_data)
    print("\nYour Key: "+key)
    send_data=Encryption(user_data,key)
    print("\nYour Send Data Is: {}".format(send_data))
    recieve_data=Decryption(send_data,key)
    print("\nYour Recieve Data Is: {}".format(recieve_data))
    print("-----------------------------------")