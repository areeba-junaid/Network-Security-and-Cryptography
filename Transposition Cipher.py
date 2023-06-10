
import numpy as np
def generate_keyTable(key,message,row,column):
    table=[]
    for letter in message:
        table.append(letter)
    table=np.asarray(table)
    key_table=np.reshape(table,(row,column))
    return key_table
def num():
     keylist=list(key)
     keylist.sort()
     key_num="" 
     for i in key:
        key_num=key_num+str(keylist.index(i))
     return key_num

def Encryption(key,row):
     
     Encrypted=""
     for column in key_num:
        column=int(column)
        for r in range(row):
                Encrypted=Encrypted + E_table[r][column]  
     return Encrypted

def Decryption(send_data,key,row,column):
     start=0
     
     D_table=[] 
     decrypted=""
     while(start<=len(send_data)-1):
        st1=send_data[start:start+row]
        st1=list(st1)
        D_table.append(st1)
        start=start + row
     for r in range(0,row):
        for column in key_num:
                column=int(column)
                if(D_table[column][r]!="*"):
                    decrypted=decrypted + D_table[column][r]  
     return decrypted


if __name__=="__main__":
    print("==================================")
    user_data=input("\n Enter Your Data: ")
    key="mega"
    print("\n Your Key is: ",key)
    print("==================================")
    print("-----------------------------------")
    while(len(user_data)%len(key)!=0):
        user_data=user_data + "*"
    column=len(key)
    row=int((len(user_data)/len(key)))
    key_num=num()
    E_table=generate_keyTable(key,user_data,row,column)
    print("Generated Key Table :\n\n {}".format(E_table))
    send_data=Encryption( key_num,row)
    print("\nYour Send Data Is: {}".format(send_data))
    recieve_data=Decryption(send_data,key_num,row,column)
    print("\nYour Recieve Data Is: {}".format(recieve_data))
    print("-----------------------------------")
    