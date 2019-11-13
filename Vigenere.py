import re

print("1.Encryption")
print("2.Decryption")
choice=int(input("Enter A Choice="))

if(choice==1):
    file1 = open("plaintext.txt", "r")
    file2 = open("cipher.txt", "w")

    pt = file1.read().replace(" ", "").upper()
    pt = re.sub('[^a-zA-Z]', '', pt)

    key = input(("Enter the Key="))
    key = key.replace(" ", "").upper()
    key = re.sub('[^a-zA-Z]', '', key)

    if ((len(pt)) > len(key)):
        key = list(key)
        for i in range(len(pt) - len(key)):
            key.append(key[i % len(key)])

    print("\n********Key***********")
    print(str(key))
    print("**********************\n")

    print("Plain Text=" + pt +"\n")
    print("*****ENCRYPTION*******")
    ct=""

    for i in range(len(pt)):
        asci=(ord(pt[i])+ord(key[i]))%26
        asci+=ord('A')
        ct=ct+chr(asci)
    print("\nThe ENCRYPTED TEXT IS= "+ct)
    print("\n**********************")
    file2.write(ct)
    file2.close()

if(choice==2):
    file3 = open("cipher.txt", "r")
    file4=open("plaintext.txt","w")
    ctxt = file3.read()

    key = input(("Enter the Key="))
    key = key.replace(" ", "").upper()
    key = re.sub('[^a-zA-Z]', '', key)

    if ((len(ctxt)) > len(key)):
        key = list(key)
        for i in range(len(ctxt) - len(key)):
            key.append(key[i % len(key)])

    print("\n********Key***********")
    print(str(key))
    print("**********************\n")

    print("Cipher Text= "+ctxt+"\n")
    print("*****DECRYPTION*******\n")
    ctxt=list(ctxt)
    ptxt=""
    for i in range(len(ctxt)):
        txt=(ord(ctxt[i])-ord(key[i])+26)%26
        txt+=ord('A')
        ptxt+=chr(txt)

    print("The DECRTYPED Text is="+ptxt)
    file4.write(ptxt)

