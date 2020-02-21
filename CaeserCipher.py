print ("Enter a Value=")
print ("1) Encrypt")
print ("2) Decrypt")
choice=int(input())
key=int(input("Enter The Key="))
print ("Key="+str(key))

s=""

if(choice==1):
    f1=open("plain.txt","r")
    f2=open("cipher.txt","w")
    while True:
        ch=f1.read(1)
        if ch == '':
            break
        asc=ord(ch)
        cipher=(asc+key)%128
        s=s+(chr(cipher))
        
    f2.write(s)
    
if(choice==2):
    f1=open("cipher.txt","r")
    f2=open("plain.txt","w")
    while True:
        ch=f1.read(1)
        if ch == '':
            break
        asc=ord(ch)
        cipher=((asc-key)+128)%128
        s=s+(chr(cipher))
        
    #s=s.strip(s[-1])
    f2.write(s)
    