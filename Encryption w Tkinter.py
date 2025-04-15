import tkinter as tk
import numpy as np
import base64 as b64
import RSA as rsa
import LoginScreen as ls


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
    encryptButton2.grid_forget()
    decryptButton2.grid_forget()
    keyBox.grid_forget()
    keyLabel.grid_forget()
    shiftBox.grid_forget()
    shiftLabel.grid_forget()
    publicKeyBox.grid_forget()
    publicKeyLabel.grid_forget()
    privateKeyBox.grid_forget()
    privateKeyLabel.grid_forget()

def lightBlueButtons():
    trifidButton.config(bg="lightblue", fg="black")
    caeserButton.config(bg="lightblue", fg="black")
    RSAButton.config(bg="lightblue", fg="black")
    b64Button.config(bg="lightblue", fg="black")
    substitutionButton.config(bg="lightblue", fg="black")

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
    ciphertextBox.grid(column=1, row=4, sticky="w")
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0, sticky="w")
    plaintextLabel.grid(column=1, row=0, sticky="nw")

def caeser():
    forgetAll()
    lightBlueButtons()
    print("caeser")
    caeserButton.config(bg="blue", fg="white")
    decryptButton.config(command=caeserDecrypt)
    encryptButton.config(command=caeserEncrypt)
    shiftBox.grid(column=1, row=2, sticky="w")
    shiftLabel.grid(column=1, row=2, sticky="nw")
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4, sticky="w")
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0, sticky="w")
    plaintextLabel.grid(column=1, row=0, sticky="nw")

def RSA():
    forgetAll()
    lightBlueButtons()
    print("RSA")
    RSAButton.config(bg="blue", fg="white")
    decryptButton.config(command=RSAPubDecrypt, text="Pub Decrypt")
    encryptButton.config(command=RSAPubEncrypt, text="Pub Encrypt")
    decryptButton2.config(command=RSAPrivDecrypt, text="Priv Decrypt")
    encryptButton2.config(command=RSAPrivEncrypt, text="Priv Encrypt")
    decryptButton.grid(column=1, row=2, sticky="nw")
    encryptButton.grid(column=1, row=2, sticky="ne")
    decryptButton2.grid(column=1, row=2, sticky="sw")
    encryptButton2.grid(column=1, row=2, sticky="se")
    publicKeyBox.grid(column=1, row=1, sticky="w")
    publicKeyLabel.grid(column=1, row=1, sticky="nw")
    privateKeyBox.grid(column=1, row=3, sticky="w")
    privateKeyLabel.grid(column=1, row=3, sticky="nw")
    ciphertextBox.grid(column=1, row=4, sticky="w")
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0, sticky="w")
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
    ciphertextBox.grid(column=1, row=4, sticky="w")
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0, sticky="w")
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
    ciphertextBox.grid(column=1, row=4, sticky="w")
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0, sticky="w")
    plaintextLabel.grid(column=1, row=0, sticky="nw")


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
    plaintext=plaintextBox.get()
    publicKey=publicKeyBox.get()
    rsa.encryptRSA(plaintext, publicKey)
    ciphertextBox.delete(0, tk.END)
    ciphertextBox.insert(0, ciphertext)

def RSAPrivEncrypt():
    resetVariables()
    RSAGenKeys()
    plaintext=plaintextBox.get()
    privateKey=privateKeyBox.get()
    rsa.encryptRSA(plaintext, privateKey)
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

def RSAPubDecrypt():
    resetVariables()
    RSAGenKeys()
    ciphertext=ciphertextBox.get()
    publicKey=publicKeyBox.get()
    rsa.decryptRSA(ciphertext, publicKey)
    plaintextBox.delete(0, tk.END)
    plaintextBox.insert(0, plaintext)

def RSAPrivDecrypt():
    resetVariables()
    RSAGenKeys()
    ciphertext=ciphertextBox.get()
    privateKey=privateKeyBox.get()
    rsa.decryptRSA(ciphertext, publicKey)
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

window=tk.Tk()
window.columnconfigure([0, 1], minsize=25)
window.rowconfigure([0], minsize=10)

trifidButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= trifid, text="Trifid")
caeserButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= caeser, text="Caeser")
RSAButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= RSA, text="RSA")
b64Button=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= base64, text="Base 64")
substitutionButton=tk.Button(height=3, width=9, borderwidth=4, bg="lightblue", command= substitution, text="Substitution")

trifidButton.grid(column=0, row=0)
caeserButton.grid(column=0, row=1)
RSAButton.grid(column=0, row=2)
b64Button.grid(column=0, row=3)
substitutionButton.grid(column=0, row=4)

plaintextLabel=tk.Label(text="Plaintext:")
plaintextBox=tk.Entry(textvariable="", justify="left")

ciphertextLabel=tk.Label(text="Ciphertext:")
ciphertextBox=tk.Entry(textvariable="", justify="left")

encryptButton=tk.Button(text="Encrypt", bg="hotpink")
decryptButton=tk.Button(text="Decrypt", bg="hotpink")
encryptButton2=tk.Button(text="Encrypt", bg="hotpink")
decryptButton2=tk.Button(text="Decrypt", bg="hotpink")

keyBox=tk.Entry(textvariable="")
keyLabel=tk.Label(text="Key:")

shiftBox=tk.Entry(textvariable="")
shiftLabel=tk.Label(text="Shift:")

privateKeyBox=tk.Entry(textvariable="")
privateKeyLabel=tk.Label(text="Private Key:")

publicKeyBox=tk.Entry(textvariable="")
publicKeyLabel=tk.Label(text="Public Key:")


window.mainloop()

