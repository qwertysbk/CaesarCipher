#Caesar Cipher using lists in Python
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(x):
    b=[]
    for i in x:
        if i.isalpha():
            index=a.index(i)
            y=(index+5)%52
            b.append(a[y])
        elif i == " ":
            b.append(i)
        else:
            c=(int(i)+5)%10
            b.append(str(c))
    z=''.join(b)
    print("\n Encrypted Code= ",z)
    
def decrypt(y):
    b=[]
    for i in y:
        if i.isalpha():
            index=a.index(i)
            x=(index-5)%52
            b.append(a[x])
        elif i == " ":
            b.append(i)
        else:
            c=(int(i)-5)%10
            b.append(str(c))
    z=''.join(b)
    print("\n Decrypted Code= ",z)
    
while True:
    print("\n Menu \n 1.Encrypt 2.Decrypt")
    choice=str(input("Enter your Choice: "))
    if choice == "1":
        x=input("\n Enter Code to be Encrypted: ")
        encrypt(x)
    elif choice == "2":
        y=input("\n Enter Code to be Decrypted : ")
        decrypt(y)
    else:
        break
    
