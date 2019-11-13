import re

file1=open("plaintext.txt","r")
file2=open("cipher.txt","w")

pt=file1.read().replace(" ","").lower()
pt=re.sub('[^a-zA-Z]', '', pt)
print("Plain Text="+pt+"\n")

pt=list(pt)
k1=int(input("Enter the value of Key 1="))
k2=int(input("Enter the value of Key 2="))
x=0
flag=0

alpha=[]
for one in range(97,123):       #A-Z List
    alpha.append(chr(one))

inv=0
for i in range(26):
    x=(k1*i)%26
    if(x==1):
        print("This Key is valid and value of x="+str(i))
        inv=i
        flag=1
        break
if(flag==0):
    print("Please enter a valid key which inverse can be possible")
    exit(0)

mat_pt=[]
mat_ct=[]

for i in range(len(pt)):
    mat_pt.append(0)
    mat_ct.append(0)

count=0
for i in pt:
    if(i in alpha):
        index=alpha.index(i)
        mat_pt[count]=index
        count+=1

ct=""
for i in range(len(pt)):
    c=(((mat_pt[i]*k1)+k2)%26)
    ct=ct+str(alpha[c])

print("\nEncrypted Text="+ct+"\n")
file2.write(ct)
ct=list(ct)

count=0
for i in ct:
    if(i in alpha):
        index=alpha.index(i)
        mat_ct[count]=index
        count+=1

pt=""
for i in range(len(ct)):
    d=(((mat_ct[i]-k2)*inv)%26)
    pt=pt+str(alpha[d])

print("Plain Text="+pt)

