import tkinter as tk
import numpy as np
import base64 as b64
import RSA as rsa
import LoginScreenLite as ls
import os
import math


def resetVariables():
    global ciphertext
    global cipherList
    global cipherNumbers
    global plaintext
    global plainList
    global plainNumbers
    global xCoordinate
    global yCoordinate
    global zCoordinate
    global cipherKey
    global asciiList
    global publicKey
    global privateKey
    ciphertext=""
    cipherList=[]
    cipherNumbers=[]
    plaintext=""
    plainList=[]
    plainNumbers=[]
    xCoordinate = []
    yCoordinate = []
    zCoordinate = []
    cipherKey=[]
    asciiList=list(""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ\n""")
    publicKey=""
    privateKey=""
resetVariables()

def forgetAll():
    ciphertextBox.grid_forget()
    ciphertextLabel.grid_forget()
    plaintextBox.grid_forget()
    plaintextLabel.grid_forget()
    encryptButton.grid_forget()
    decryptButton.grid_forget()
    encryptButton.config(text="Encrypt:")
    decryptButton.config(text="Decrypt:")
    keyBox.grid_forget()
    keyLabel.grid_forget()
    shiftBox.grid_forget()
    shiftLabel.grid_forget()
    publicKeyBox.grid_forget()
    publicKeyLabel.grid_forget()
    privateKeyBox.grid_forget()
    privateKeyLabel.grid_forget()
    changePasswordButton.grid_forget()
    changeUsernameButton.grid_forget()
    newUserButton.grid_forget()
    usernameBox.grid_forget()
    usernameLabel.grid_forget()
    passwordBox.grid_forget()
    passwordLabel.grid_forget()
    uidBox.grid_forget()
    uidLabel.grid_forget()
    removeUserButton.grid_forget()

def lightBlueButtons():
    trifidButton.config(bg="lightblue", fg="black")
    caeserButton.config(bg="lightblue", fg="black")
    RSAButton.config(bg="lightblue", fg="black")
    b64Button.config(bg="lightblue", fg="black")
    substitutionButton.config(bg="lightblue", fg="black")
    changeDetailsButton.config(bg="lightblue", fg="black")

def RSAGenKeys():
    if privateKeyBox.get() and publicKeyBox.get():
        return privateKeyBox.get(), publicKeyBox.get()
    privateKey, publicKey = rsa.makeRSAKey()
    privateKeyBox.delete(0, tk.END)
    privateKeyBox.insert(0, privateKey)
    publicKeyBox.delete(0, tk.END)
    publicKeyBox.insert(0, publicKey)
    return privateKey, publicKey


def trifid():
    print("trifid")
    forgetAll()
    lightBlueButtons()
    trifidButton.config(bg="blue", fg="white")
    decryptButton.config(command=trifidDecrypt)
    encryptButton.config(command=trifidEncrypt)
    keyLabel.grid(column=1, row=2, sticky="nw")
    keyBox.grid(column=1, row=2)
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")

def caeser():
    forgetAll()
    lightBlueButtons()
    print("caeser")
    caeserButton.config(bg="blue", fg="white")
    decryptButton.config(command=caeserDecrypt)
    encryptButton.config(command=caeserEncrypt)
    shiftBox.grid(column=1, row=2)
    shiftLabel.grid(column=1, row=2, sticky="nw")
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")

def RSA():
    forgetAll()
    lightBlueButtons()
    print("RSA")
    RSAButton.config(bg="blue", fg="white")
    decryptButton.config(command=RSAPrivDecrypt, text="Priv Decrypt")
    encryptButton.config(command=RSAPubEncrypt, text="Pub Encrypt")
    decryptButton.grid(column=1, row=2, sticky="s")
    encryptButton.grid(column=1, row=2, sticky="n")
    publicKeyBox.grid(column=1, row=1)
    publicKeyLabel.grid(column=1, row=1, sticky="nw")
    privateKeyBox.grid(column=1, row=3)
    privateKeyLabel.grid(column=1, row=3, sticky="nw")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")

def base64():
    forgetAll()
    lightBlueButtons()
    print("base64")
    b64Button.config(bg="blue", fg="white")
    decryptButton.config(command=base64Decrypt)
    encryptButton.config(command=base64Encrypt)
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")

def substitution():
    forgetAll()
    lightBlueButtons()
    print("substitution")
    substitutionButton.config(bg="blue", fg="white")
    decryptButton.config(command=substitutionDecrypt)
    encryptButton.config(command=substitutionEncrypt)
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")

def changeDetails():
    forgetAll()
    lightBlueButtons()
    print("changeDetails")
    changeDetailsButton.config(bg="blue", fg="white")
    usernameBox.grid(column=1, row=0)
    usernameLabel.grid(column=1, row=0, sticky="nw")
    passwordBox.grid(column=1, row=1)
    passwordLabel.grid(column=1, row=1, sticky="nw")
    uidBox.grid(column=1, row=2)
    uidLabel.grid(column=1, row=2, sticky="nw")
    
    changePasswordButton.grid(column="1", row="3", sticky="n")
    changeUsernameButton.grid(column="1", row="3", sticky="s")
    newUserButton.grid(column="1", row="4", sticky="n")
    removeUserButton.grid(column="1", row="4", sticky="s")


def trifidEncrypt(): # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼—½¿Ƚ♥
    resetVariables()
    plainList=list(plaintextBox.get())
    keyList=list(keyBox.get().replace("♥","\n"))
    np.insert(keyList, 1, 125, axis=0)
    cipherKey=np.reshape(keyList,(5,5,5))
    for i in plainList:
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if cipherKey[x][y][z] == i:
                        xCoordinate.append(x)
                        yCoordinate.append(y)
                        zCoordinate.append(z)
    for i in range(len(plainList)):
        cipherList.append(cipherKey[xCoordinate[i]][yCoordinate[i-1]][zCoordinate[i-2]])
    ciphertext="".join(cipherList)
    ciphertextBox.delete(0, tk.END)
    ciphertextBox.insert(0, ciphertext)

def caeserEncrypt():
    resetVariables()
    ciphertext=""
    shift=int(shiftBox.get())
    plaintext=plaintextBox.get()
    for i in plaintext:
        plainNumbers.append(asciiList.index(i))
    cipherNumbers = [x+shift for x in plainNumbers]
    for i in cipherNumbers:
        ciphertext+=asciiList[i%len(asciiList)]
    ciphertextBox.delete(0, tk.END)
    ciphertextBox.insert(0, ciphertext)

def RSAPubEncrypt():
    resetVariables()
    RSAGenKeys()
    ciphertext=""
    plaintext=plaintextBox.get()
    publicKey=publicKeyBox.get()

    splitPlaintext = [plaintext[i:i+200] for i in range(0, len(plaintext), 200)] #https://www.geeksforgeeks.org/python-divide-string-into-equal-k-chunks/
    print(splitPlaintext)
    for i in splitPlaintext:
        ciphertext+= rsa.encryptRSA(i, publicKey) + "♥♥♥♥♥"
    print(ciphertext)
        
    ciphertextBox.delete(0, tk.END)
    ciphertextBox.insert(0, ciphertext)

def base64Encrypt():
    resetVariables()
    plaintext=plaintextBox.get()
    ciphertext=b64.b64encode(plaintext.encode()).decode("ascii")
    ciphertextBox.delete(0, tk.END)
    ciphertextBox.insert(0, ciphertext)

def substitutionEncrypt():
    resetVariables()
    ciphertext=""
    plaintext=plaintextBox.get()
    for i in plaintext:
        plainList.append(ord(i))
    for i in plainList:
        ciphertext+=(str(i) + " ")
    ciphertextBox.delete(0, tk.END)
    ciphertextBox.insert(0, ciphertext)


def trifidDecrypt(): # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ♥
    resetVariables()
    cipherList=list(ciphertextBox.get())
    keyList=list(keyBox.get().replace("♥","\n"))
    np.insert(keyList, 1, 125, axis=0)
    cipherKey=np.reshape(keyList,(5,5,5))
    for i in cipherList:
        for x in range(5):
            for y in range(5):
                for z in range(5):
                    if cipherKey[x][y][z] == i:
                        xCoordinate.append(x)
                        yCoordinate.append(y)
                        zCoordinate.append(z)
    for i in range(len(cipherList)):
        plainList.append(cipherKey[xCoordinate[i]][yCoordinate[ (i+1) % len(cipherList)]][zCoordinate[ (i+2) % len(cipherList)]])
    plaintext="".join(plainList)
    plaintextBox.delete(0, tk.END)
    plaintextBox.insert(0, plaintext)

def caeserDecrypt():
    resetVariables()
    plaintext=""
    shift=int(shiftBox.get())*-1
    ciphertext=ciphertextBox.get() 
    for i in ciphertext:
        cipherNumbers.append(asciiList.index(i))
    plainNumbers = [x+shift for x in cipherNumbers]
    for i in plainNumbers:
        plaintext+=asciiList[i%len(asciiList)]
    plaintextBox.delete(0, tk.END)
    plaintextBox.insert(0, plaintext)

def RSAPrivDecrypt():
    resetVariables()
    RSAGenKeys()
    ciphertext=ciphertextBox.get()
    privateKey=privateKeyBox.get()
    plaintext=""
    
    cipherList=ciphertext.split("♥♥♥♥♥")
    print(cipherList)
    for i in cipherList:
        if i != "":
            plaintext+=rsa.decryptRSA(i, privateKey)
    plaintextBox.delete(0, tk.END)
    plaintextBox.insert(0, plaintext)

def base64Decrypt():
    resetVariables()
    ciphertext=ciphertextBox.get()
    plaintext=b64.b64decode(ciphertext)
    plaintext=plaintext.decode("ascii")
    plaintextBox.delete(0, tk.END)
    plaintextBox.insert(0, plaintext)

def substitutionDecrypt():
    resetVariables()
    plaintext=""
    cipherList=ciphertextBox.get().split()
    for i in cipherList:
        plaintext+=chr(int(i))
    plaintextBox.delete(0, tk.END)
    plaintextBox.insert(0, plaintext)


def changePassword():
    print("changepass")
    password=passwordBox.get()
    uid=uidBox.get()
    
    credentialsFile = open("credentials.txt", "r")
    newCredentialsFile = open("newcredentials.txt", "a") #append will automatically create file if it doesnt exist already
    newuid="0"
    if password=="":
        return
    if uid=="":
        return
    for line in credentialsFile:
        line = line.split(":", 2)
        print(line)
        if uid == line[2].replace('\n', ''):
            line[1] = password
        newCredentialsFile.write(line[0] + ":" + line[1] + ":" + str(newuid) + "\n")
        newuid= int(line[2])+1
    
    newCredentialsFile.close()
    credentialsFile.close()
    os.remove("credentials.txt")
    os.rename("newcredentials.txt", "credentials.txt")

def changeUsername():
    print("changeuser")
    username=usernameBox.get()
    uid=uidBox.get()
    
    credentialsFile = open("credentials.txt", "r")
    newCredentialsFile = open("newcredentials.txt", "a") #append will automatically create file if it doesnt exist already
    newuid="0"
    if username=="":
        print("uname")
        return
    if uid=="":
        print("uid")
        return
    for line in credentialsFile:
        line = line.split(":", 2)
        print(line)
        if uid == line[2].replace('\n', ''):
            line[0] = username
            print("heehe")
        newCredentialsFile.write(line[0] + ":" + line[1] + ":" + str(newuid) + "\n")
        newuid= int(line[2])+1
    
    newCredentialsFile.close()
    credentialsFile.close()
    os.remove("credentials.txt")
    os.rename("newcredentials.txt", "credentials.txt")

def newUser():
    print("newuser")
    password=passwordBox.get()
    username=usernameBox.get()

    credentialsFile = open("credentials.txt", "r")
    if username == "":
        credentialsFile.close()
        return
    if password == "":
        credentialsFile.close()
        return
    for line in credentialsFile:
        line = line.split(":", 2)
        print(line)
        if username == line[0].replace('\n', ''):
            return
        uid=line[2].replace('\n', '')
    credentialsFile.close()

    newuid= int(uid)+1
    credentialsFile = open("credentials.txt", "a")
    credentialsFile.write(username + ":" + password + ":" + str(newuid) + "\n")    
    credentialsFile.close()

def removeuser():
    print("removeuser")
    username=usernameBox.get()
    uid=uidBox.get()
    
    credentialsFile = open("credentials.txt", "r")
    newCredentialsFile = open("newcredentials.txt", "a") #append will automatically create file if it doesnt exist already
    newuid="0"
    replacedUsers=0
    for line in credentialsFile:
        line = line.split(":", 2)
        if uid == line[2].replace('\n', '') or username == line[0].replace("\n", ""):
            newuid= int(line[2])
            replacedUsers+=1
        else:
            newCredentialsFile.write(line[0] + ":" + line[1] + ":" + str(newuid) + "\n")
            
        newuid= int(line[2]) + 1 - replacedUsers
    
    newCredentialsFile.close()
    credentialsFile.close()
    os.remove("credentials.txt")
    os.rename("newcredentials.txt", "credentials.txt")


if ls.start():
    window=tk.Tk()
    window.minsize(200, 300)
    window.maxsize(200, 300)

    trifidButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= trifid, text="Trifid")
    caeserButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= caeser, text="Caeser")
    RSAButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= RSA, text="RSA")
    b64Button=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= base64, text="Base 64")
    substitutionButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= substitution, text="Substitution")
    
    changeDetailsButton=tk.Button(height=1, width=4, borderwidth=2, bg="lightblue", command= changeDetails, text="Details")

    trifidButton.grid(column=0, row=0, sticky="nsew")
    caeserButton.grid(column=0, row=1, sticky="nsew")
    RSAButton.grid(column=0, row=2, sticky="nsew")
    b64Button.grid(column=0, row=3, sticky="nsew")
    substitutionButton.grid(column=0, row=4, sticky="nsew")
    
    changeDetailsButton.grid(column=1, row=0, sticky="ne")

    plaintextLabel=tk.Label(text="Plaintext:")
    plaintextBox=tk.Entry(textvariable="", justify="left")

    ciphertextLabel=tk.Label(text="Ciphertext:")
    ciphertextBox=tk.Entry(textvariable="", justify="left")

    usernameBox=tk.Entry(textvariable="", justify="left")
    passwordBox=tk.Entry(textvariable="", justify="left")
    uidBox=tk.Entry(textvariable="", justify="left")
    usernameLabel=tk.Label(text="Username:")
    passwordLabel=tk.Label(text="Password:")
    uidLabel=tk.Label(text="UID:")

    encryptButton=tk.Button(text="Encrypt", bg="hotpink")
    decryptButton=tk.Button(text="Decrypt", bg="hotpink")

    changePasswordButton=tk.Button(height=1, width=12, borderwidth=2, bg="lightblue", command= changePassword, text="changePassword")
    changeUsernameButton=tk.Button(height=1, width=12, borderwidth=2, bg="lightblue", command= changeUsername, text="changeUsername")
    newUserButton=tk.Button(height=1, width=6, borderwidth=2, bg="lightblue", command= newUser, text="newUser")
    removeUserButton=tk.Button(height=1, width=10, borderwidth=2, bg="lightblue", command= removeuser, text="removeuser")

    keyBox=tk.Entry(textvariable="")
    keyLabel=tk.Label(text="Key:")

    shiftBox=tk.Entry(textvariable="")
    shiftLabel=tk.Label(text="Shift:")

    privateKeyBox=tk.Entry(textvariable="")
    privateKeyLabel=tk.Label(text="Private Key:")

    publicKeyBox=tk.Entry(textvariable="")
    publicKeyLabel=tk.Label(text="Public Key:")


    window.mainloop()