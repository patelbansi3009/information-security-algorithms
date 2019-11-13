import sys
import numpy as np

def a1(a):
    r1 = 26
    r2 = a
    t1 = 0
    t2 = 1
    while (r2 > 0):
        q = int(r1 / r2)
        r = r1 % r2

        r1 = r2
        r2 = r
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if (r1 == 1):
        return t1 % 26
    else:
        print("Operation Not Possible")
        sys.exit(0)


l = "abcdefghijklmnopqrstuvwxyz"
l = list(l)
print("1.Encryption")
print("2.Decryption")
choice=int(input("Select a Choice="))
if(choice>2 or choice<1):
    print("Enter a valid choice")
    exit(0)
key_text = input("Enter Key Text=")
key_text = key_text.lower()
p_t = open("input.txt", "r").read()
p_t = p_t.lower()
for i in key_text:
    if (i not in l):
        key_text = key_text.replace(i, "")
p_t = p_t.replace(" ", "")
for i in p_t:
    if (i not in l):
        print(i + "no")
        p_t = p_t.replace(i, "")
b = 0
a = 1
while (True):
    if (len(key_text) <= a * a):
        b = a
        a = a * a
        break
    a = a + 1

le = a - len(key_text)
for i in range(0, le):
    key_text = key_text + l[i]

key_text = list(key_text)
key_text = np.array(key_text)
key_text = key_text.reshape(-1, b)
print("*****Key Matrix*****")
print(key_text)
k_num = np.arange(a)
k_num = k_num.reshape(-1, b)
for i in range(0, b):
    for j in range(0, b):
        index = l.index(key_text[i][j])
        k_num[i][j] = index
print("*****Key Number*****")
print(k_num)
print("********************")

if(choice==1):
    print("\n\n##############ENCRYPTION#################\n\n")
    det1 = np.linalg.det(k_num)
    det1 = int(round(det1 % 26))
    x = a1(det1)
    l2 = 1
    while (l2 != 0):
        l2 = len(p_t) % b
        if (l2 != 0):
            p_t = p_t + 'z'
    print("*****Plain Text*****")
    print("The Plain Text is="+p_t)
    p_num = np.arange(len(p_t))
    p_num = p_num.reshape(-1, b)
    p_t = list(p_t)
    p_t = np.array(p_t)
    p_t = p_t.reshape(-1, b)
    print(p_t)
    row, col = p_num.shape
    for i in range(0, row):
        for j in range(0, col):
            index = l.index(p_t[i][j])
            p_num[i][j] = index
    print("The Plain Text Number")
    print(p_num)
    print("********************")
    c_text = ""
    print("*****Answer Matrix*****")

    for i in range(0, row):
        k = p_num[i].reshape(-1, 1)
        ans = np.dot(k_num, k)
        ans = ans % 26
        print(ans)
        for i in range(0, b):
            c_text = c_text + l[ans[i][0]]
    print("**********************")
    print("The Cipher Text is= "+c_text)
    f1 = open("encrypted.txt", "w")
    f1.write(c_text)
    f1.close()
    c_text = open("encrypted.txt", "r").read()
    print("The Cipher Text Number")
    print(k_num)
    print("**********************")

if(choice==2):
    print("\n\n##############DECRYPTION#################\n\n")
    print("**********************")
    c_text = open("encrypted.txt", "r").read()
    det1 = np.linalg.det(k_num)
    invk = np.linalg.inv(k_num)
    print("Inverse Matrix")
    print(invk)
    adj = det1 * np.linalg.inv(k_num)
    det1 = int(round(det1 % 26))
    print("**********************")
    print("Determinant")
    print(det1)
    x = a1(det1)
    print("**********************")
    print("Adjoint")
    print(adj)
    print("**********************")
    rrr, ccc = adj.shape
    k111 = np.arange(rrr * ccc)
    k111 = k111.reshape(-1, b)
    for i in range(0, b):
        for j in range(0, b):
            print(int(round(adj[i][j])))
            k111[i][j] = int(round(adj[i][j]))
    invk = (x * k111) % 26
    print("**********************")
    print("Inverse Matrix")
    print(invk)
    print("**********************")

    cipher_num = np.arange(len(c_text))
    cipher_num = cipher_num.reshape(-1, b)
    c_text = list(c_text)
    c_text = np.array(c_text)
    c_text = c_text.reshape(-1, b)
    r1, c1 = c_text.shape
    for i in range(0, r1):
        for j in range(0, c1):
            cipher_num[i][j] = l.index(c_text[i][j])
    p_text = ""
    for i in cipher_num:
        z = i
        z = z.reshape(-1, 1)
        print(z)
        ans = np.dot(invk, z)
        row11, col11 = ans.shape
        for k in range(0, row11):
            ans[k][0] = int(ans[k][0])
        ans = ans % 26
        print(ans)
        for j in range(0, b):
            p_text = p_text + l[int(ans[j][0])];
    print("**********************")
    print("The Decrypted Plain Text is=" + p_text)
    file1=open("input.txt","w")
    file1.write(p_text)
    file1.close()