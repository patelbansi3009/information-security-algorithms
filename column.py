import math
import numpy as num
file1 = open("plaintext.txt", "r")
file2 = open("cipher.txt","w")
ptext=file1.read().replace(" ","")
key = input("Enter The Key=").replace(" ","")
key=key.lower()

if(key.isalpha()==0):
    print("Enter a valid string without any numbers")
    exit(0)

key=list(key)
print("#####ENCRYPTION#####")

alpha=[]
for one in range(97,123):       #A-Z List
    alpha.append(chr(one))

ind=0
count=0
key_list=[]

for i in range(len(key)):
    key_list.append(0)

for i in alpha:
    if(i in key):
        ind=key.index(i)
        key_list[ind]=count
        count+=1
    else:
        continue
print("Encryption Key Matrix="+str(key_list))
#encryption
row=math.ceil(len(ptext) / len(key))
matrix = [['$' for i in range(len(key))] for j in range(row)]
count=0

for i in range(row):        #plain text insertion into matrix

    for j in range(len(key)):
        if(count==len(ptext)):
            break
            break
        else:
            matrix[i][j]=ptext[count]
            count+=1
enc_text=""
matrix=num.array(matrix)

for i in key_list:      #column by column access
    temp=matrix[:,i]
    for j in temp:
        enc_text=enc_text+j;

print("\nEncrypted Text = "+enc_text+"\n")
print("Length of The String="+str(len(ptext))+"\n")
print("Total Number of Rows="+str(row)+"\n")
file2.write(enc_text)
#DECRYPTION

print("#####DECRYPTION#####\n")
file1 = open("plaintext.txt","w")
file2 = open("cipher.txt" , "r")
ctext=file2.read()

cmatrix=[['' for i in range(len(key))] for j in range(row)]

count=0

for i in range(len(key)):        #cipher text insertion into matrix
    for j in range(row):
        if(count==len(ctext)):
            break
            break
        else:
            cmatrix[j][i]=ctext[count]
            count+=1

dec_list=[]
for i in range(len(key)):       #decryption list creation
    dec_list.append(0)

count=0
for i in key_list:
    temp=key_list.index(i)      #decryption key matrix
    dec_list[i]=count
    count+=1

print("Decryption Key Matrix="+str(dec_list)+"\n")

dec_text=""
cmatrix=num.array(cmatrix)

t1=[]
for i in dec_list:      #decryption matrix
    temp=cmatrix[:,i]
    t1.append(list(temp));

dec_text=""
for i in range(row):
    for j in range(len(key)):   #decrypted text
        dec_text=dec_text+t1[j][i]

dec_text=dec_text.replace("$","")

print("Your Decrypted Text="+dec_text)
file1.write(dec_text)