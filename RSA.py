from primePy import primes
import math
def finding_e(phi):
    e=2
    while(e<phi):
        if (math.gcd(e,phi)==1):
            break
        e=e+1
    return e 


def finding_d(e,phi):
    k=0
    while(True):
        d=(1+ k*phi)/e
        if (d.is_integer()):
            break
        k=k+1
    return int(d)


def Encryption(user_data,e,n):
    p_ascii=""
    for i in user_data:
        if (i.isupper()):
            num=ord(i)-65 + 1
            p_ascii= p_ascii + str(num)
        elif(i.islower()):
            num=ord(i)-97 + 1
            p_ascii= p_ascii + str(num)
    Encrypted=(int( p_ascii)**e)% n
    print("==================================")
    print(f'\nUser Data in Ascii:{p_ascii}')
    print(f'Your Encrpted Data:{Encrypted}')
    return Encrypted


def Decryption(C,d,n):
    plain_text=''
    Decrypted=(C**d)% n
    str_decrypted=str(Decrypted)
    for i in str_decrypted:
        num= int(i)+97-1
        plain_text= plain_text + chr(num)
    print("==================================")
    print(f'\nYour Decrypted Data: {Decrypted}')
    print(f'Plain Text: {plain_text}')


if _name=="main_":


    print("==================================")
    p=int(input("Enter First Prime number: "))
    while(primes.check(p)==False):
        p=int(input("\n Enter First Prime number Again: "))
    q=int(input("Enter Second Prime number (Not equal to First Prime no): "))
    while(primes.check(q)==False or p==q):
        q=int(input("Enter Second Prime number again: "))
    n=p*q
    phi=(p-1)*(q-1)
    print("The value of phi is: {}".format(phi))
    e=finding_e(phi)
    d=finding_d(e,phi)
    print("==================================")
    print(f'Your public key (e,n)= ({e}, {n})')
    print(f'Your private key (d,n)= ({d}, {n})')
    user_data=input(f"Enter Your Data (lenght less than {n}:): ")
    while(len(user_data) > n):
        user_data=input(f"Out of Range...Enter Your Data Again: ): ")
    Encrypted=Encryption(user_data,e,n)
    Decryption(Encrypted,d,n)