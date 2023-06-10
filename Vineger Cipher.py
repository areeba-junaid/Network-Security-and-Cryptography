def generate_key(user_message):
    keyword="ciel"
    index=0
    generated_key=""
    for i in user_message:
        index=(index+(len(keyword)-1)+1)%(len(keyword))
        if(i==" "):
           generated_key=generated_key + " "
           index=index-1
        elif(i.isupper()):
            generated_key=generated_key + (keyword[index]).upper() 
        else:
            generated_key=generated_key + (keyword[index])
        index=index+1
    return generated_key
    
def Encryption(message,key):

    encrypted_message=''
    for i in range(len(key)):
        if (key[i].isupper() and key!=" "):
            index=ord(message[i])-65
            encrypted_message=encrypted_message + chr((ord(key[i])+ index-65)%26 +65)
        elif(key[i].islower() and key!=" "):
            index=ord(message[i])-97
            encrypted_message=encrypted_message + chr((ord(key[i])+ index-97)%26 +97)
        if(key[i] == " "):
            encrypted_message=encrypted_message + " "
    return encrypted_message


def Decryption(message,key):

    decrypted_message=''
    for i in range(len(key)):
        if (key[i].isupper() and key!=" "): 
            decrypted_message=decrypted_message + chr((ord(message[i])-ord(key[i])+26)%26 + 65)
        elif(key[i].islower() and key!=" "):
             decrypted_message=decrypted_message + chr((ord(message[i])-ord(key[i])+26)%26 + 97)
        if(key[i] == " "):
            decrypted_message=decrypted_message + " "
    return decrypted_message
if __name__=="__main__":
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
    
