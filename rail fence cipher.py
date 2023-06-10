import numpy as np

def Encryption(key,message):
    rail=[[] for i in range(key)]
    Encrypted=""
    row=0
    for letter in message:
        if(row==key-1):
            flag=1
        elif(row==0):
            flag=0
        if(flag==0):
            rail[row].append(letter)
            row=row+1
        else:   
            rail[row].append(letter)
            row=row-1
    rail_flat=[x for row in rail for x in row]
    Encrypted = ''.join(map(str, rail_flat))
    return Encrypted  
 
def Decryption(send_data,key):
    column=int(len(send_data)/key)
    table=list(send_data) 
    table=np.asarray(table)
    d_table=np.reshape(table,(key,column))
    decrypt=""
    for c in  range(0,column):
        for r in range(0, key):
            if(d_table[r][c]!= "*"):
                decrypt=decrypt + d_table[r][c]
    return decrypt

if __name__=="__main__":
    print("==================================")
    user_data=input("\n Enter Your Data: ")
    key=2
    print("\n Your Key is: ",key)
    print("==================================")
    print("-----------------------------------")
    while(len(user_data)%key!=0):
            user_data=user_data + "*"
    send_data=Encryption( key,user_data)
    print("\nYour Sent(Encrypted) Data Is: {}".format(send_data))
    recieve_data=Decryption(send_data,key)
    print("\nYour Recieve Data Is: {}".format(recieve_data))
    print("-----------------------------------")
    