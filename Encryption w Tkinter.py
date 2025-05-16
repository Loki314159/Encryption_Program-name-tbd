import tkinter as tk
from tkinter import messagebox
import numpy as np
import base64 as b64
import RSA as rsa
import LoginScreenLite as ls
import os
import customtkinter
import random
# ---------------------------------------------------------------#
"""
    Purpose: clear out all the buttons for each encryption method
    Requirement: be called
    Promise: all widgets cleared bar method buttons and details button
"""
# ---------------------------------------------------------------#
def forgetAll():
    ciphertextBox.grid_forget()
    ciphertextLabel.grid_forget()
    plaintextBox.grid_forget()
    plaintextLabel.grid_forget()
    encryptButton.grid_forget()
    decryptButton.grid_forget()
    encryptButton.configure(text="Encrypt:")
    decryptButton.configure(text="Decrypt:")
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
    UIDBox.grid_forget()
    UIDLabel.grid_forget()
    removeUserButton.grid_forget()
    getUIDButton.grid_forget()
    
# ---------------------------------------------------------------#
"""
    Purpose: make all buttons light blue to allow the focused method be turned dark blue and focused
    Requirement: be called
    Promise: all buttons will be turned light blue
"""
# ---------------------------------------------------------------#
def blueButtons():
    trifidButton.configure(fg_color="#3f5799", text_color="black")
    caesarButton.configure(fg_color="#3f5799", text_color="black")
    RSAButton.configure(fg_color="#3f5799", text_color="black")
    b64Button.configure(fg_color="#3f5799", text_color="black")
    substitutionButton.configure(fg_color="#3f5799", text_color="black")
    changeDetailsButton.configure(fg_color="#3f5799", text_color="black")

def usernameExists(username):
    credentialsFile = open("credentials.txt", "r")
    usernameExists=False
    try:
        for line in credentialsFile:
            line = line.split("|", 2)
            if username == line[0].replace('\n', ''):
                usernameExists=True
            UID=line[2].replace('\n', '')
            newUID= int(UID)+1
    except UnboundLocalError:
        messagebox.showwarning("Unbound Local Error","Verify user inputs are accurate")
    except:
        messagebox.showwarning("Generic Error","Verify user inputs are accurate")
    credentialsFile.close()
    UIDBox.delete(0, "end")
    UIDBox.insert(0, UID)
    return usernameExists

def pipeCheck(text):
    for i in text:
        if i == "|":
            return True
    return False
# ---------------------------------------------------------------#
"""
    Purpose: Generate RSA keys using RSA.py provided in assessment files
    Requirement: be called while encrypting/decrypting
    Promise: generate RSA keys if there aren't any currently
"""
# ---------------------------------------------------------------#
def RSAGenKeys():
    if privateKeyBox.get() and publicKeyBox.get():
        return privateKeyBox.get(), publicKeyBox.get()
    privateKey, publicKey = rsa.makeRSAKey()
    privateKeyBox.delete(0, "end")# this will delete everything in the Entry box from the start (0) to the end
    privateKeyBox.insert(0, privateKey)# this will place the privateKey in the privatekeybox at the start (0)
    publicKeyBox.delete(0, "end")
    publicKeyBox.insert(0, publicKey)
    return privateKey, publicKey # returns both keys to the operation that called the function

def trifidGenKeys():
    if keyBox.get():
        return keyBox.get()
    key = list(""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼—½¿Ƚ\n""")
    random.shuffle(key)
    key=''.join(key)
    keyBox.delete(0, "end")# this will delete everything in the key box from the start (0) to the end
    keyBox.insert(0, key.replace("\n", "♥"))# this will place the key in the key box at the start (0)
    return key

def caeserGenShift():
    if shiftBox.get():
        return int(shiftBox.get())
    randNum=random.randint(0, 999)
    shiftBox.delete(0, "end")# this will delete everything in the Entry box from the start (0) to the end
    shiftBox.insert(0, randNum)# this will place the shift in the shift box at the start (0)
    return randNum
# ---------------------------------------------------------------#
"""
    Purpose: Remove the newline character at the end of an input parsed through a Text widget, this is not needed for user inputs from Entry widgets
    Requirement: be called after parsing input from an Entry widget
    Promise: remove the unnecessary (sometimes problematic) newline character from inputs
"""
# ---------------------------------------------------------------#
def Textboxformatter(text):
    alteredTextList=list(text) # turn the test into a list
    alteredTextList.pop(-1) # remove the final character (which will always be a newline)
    alteredText="".join(alteredTextList) # put the list back into being a string
    return alteredText
# ---------------------------------------------------------------#
"""
    Purpose: set widgets to be for the trifid method
    Requirement: Trifid button pressed
    Promise: initialise trifid and common widgets
"""
# ---------------------------------------------------------------#
def trifid():
    forgetAll()
    blueButtons()
    trifidButton.configure(fg_color="#3f5799", text_color="white")
    decryptButton.configure(command=callTrifidDecrypt)
    encryptButton.configure(command=callTrifidEncrypt)# changes the configuration of the button so that it calls the specified command
    keyLabel.grid(column=1, row=2, sticky="nw")
    keyBox.grid(column=1, row=2, sticky="we")
    encryptButton.grid(column=1, row=1, sticky="s") # places the widget in the specified column and row where it will be alligned to the cardinal direction specified
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4) # due to lack of sticky it will be in the centre
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")
# ---------------------------------------------------------------#
"""
    Purpose: set widgets to be for the caesar method
    Requirement: Caesar button pressed
    Promise: initialise caesar and common widgets
"""
# ---------------------------------------------------------------#
def caesar():
    forgetAll()
    blueButtons()
    caesarButton.configure(fg_color="#3f5799", text_color="white")
    decryptButton.configure(command=callCaesarDecrypt)
    encryptButton.configure(command=callCaesarEncrypt)
    shiftBox.grid(column=1, row=2)
    shiftLabel.grid(column=1, row=2, sticky="nw")
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")
# ---------------------------------------------------------------#
"""
    Purpose: set widgets to be for the RSA method
    Requirement: RSA button pressed
    Promise: initialise RSA and common widgets
"""
# ---------------------------------------------------------------#
def RSA():
    forgetAll()
    blueButtons()
    RSAButton.configure(fg_color="#3f5799", text_color="white")
    decryptButton.configure(command=callRSAPrivDecrypt, text="Priv Decrypt")
    encryptButton.configure(command=callRSAPubEncrypt, text="Pub Encrypt")
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
# ---------------------------------------------------------------#
"""
    Purpose: set widgets to be for the base64 method
    Requirement: base64 button pressed
    Promise: initialise base64 and common widgets
"""
# ---------------------------------------------------------------#
def base64():
    forgetAll()
    blueButtons()
    b64Button.configure(fg_color="#3f5799", text_color="white")
    decryptButton.configure(command=callBase64Decrypt)
    encryptButton.configure(command=callBase64Encrypt)
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")
# ---------------------------------------------------------------#
"""
    Purpose: set widgets to be for the substitution method
    Requirement: Substitution button pressed
    Promise: initialise substitution and common widgets
"""
# ---------------------------------------------------------------#
def substitution():
    forgetAll()
    blueButtons()
    substitutionButton.configure(fg_color="#3f5799", text_color="white")
    decryptButton.configure(command=callSubstitutionDecrypt)
    encryptButton.configure(command=callSubstitutionEncrypt)
    encryptButton.grid(column=1, row=1, sticky="s")
    decryptButton.grid(column=1, row=3, sticky="n")
    ciphertextBox.grid(column=1, row=4)
    ciphertextLabel.grid(column=1, row=4, sticky="nw")
    plaintextBox.grid(column=1, row=0)
    plaintextLabel.grid(column=1, row=0, sticky="nw")
# ---------------------------------------------------------------#
"""
    Purpose: set widgets for user management
    Requirement: details button pressed
    Promise: initialise details and common widgets
"""
# ---------------------------------------------------------------#
def changeDetails():
    forgetAll()
    blueButtons()
    changeDetailsButton.configure(fg_color="#3f5799", text_color="white")
    usernameBox.grid(column=1, row=0)
    usernameLabel.grid(column=1, row=0, sticky="nw")
    passwordBox.grid(column=1, row=1)
    passwordLabel.grid(column=1, row=1, sticky="nw")
    UIDBox.grid(column=1, row=2)
    UIDLabel.grid(column=1, row=2, sticky="nw")
    
    changePasswordButton.grid(column="1", row="3", sticky="new")
    changeUsernameButton.grid(column="1", row="3", sticky="sew")
    getUIDButton.grid(column="1", row="3", sticky="ew")
    newUserButton.grid(column="1", row="4", sticky="new")
    removeUserButton.grid(column="1", row="4", sticky="ew")

# ---------------------------------------------------------------#
"""
    Purpose: call the trifidEncrypt function and pass is text from the plaintext box and the key from the key box
    Requirement: Encrypt button be pressed
    Promise: insert encrypted text into the ciphertext box
"""
# ---------------------------------------------------------------#
def callTrifidEncrypt(): # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼—½¿Ƚ♥
    if not Textboxformatter(plaintextBox.get("0.0", "end")):
        messagebox.showwarning("Plaintext Empty","Cannot encrypt nothing")
        return
    ciphertext=""   # example key^^^
    plaintext=Textboxformatter(plaintextBox.get("0.0", "end")) # gets the text from the plaintext Text field before removing the unnecessary newline character to avoid incorrect encryption
    key=trifidGenKeys()
    ciphertext = trifidEncrypt(key, plaintext)
    ciphertextBox.delete("0.0", "end") # the formatting to delete things from Text widgets is slightly different to Entry widgets as shown previously, this deletes everything in it
    ciphertextBox.insert("0.0", ciphertext) # similar difference here, just inserts ciphertext
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with trifid method
    Requirement: called, there is a plaintext to encrypt, key is 125 characters and all characters in the plaintext are also in the key
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def trifidEncrypt(key, plaintext):
    plainList=list(plaintext)
    keyList=list(key.replace("♥","\n")) #allows keys to have ♥ instead of newline character, purely a cosmetic choice
    try:
        cipherKey=np.reshape(keyList,(5,5,5))#reshape key into key cube 
        xCoordinate = []
        yCoordinate = []
        zCoordinate = []
        for i in plainList:
            for x in range(5):
                for y in range(5):
                    for z in range(5):
                        if cipherKey[x][y][z] == i: #turn plaintext into coordinates
                            xCoordinate.append(x)
                            yCoordinate.append(y)
                            zCoordinate.append(z)
        cipherList=[]
        for i in range(len(plainList)):
            cipherList.append(cipherKey[xCoordinate[i]][yCoordinate[i-1]][zCoordinate[i-2]]) #shift coordinates and write out the ciphertext
        ciphertext="".join(cipherList)
    except ValueError:
        messagebox.showwarning("Value Error","Key too large or too small")
    except IndexError:
        messagebox.showwarning("Index Error","Character in plaintext that is not in the key")
    except:
        messagebox.showwarning("Generic Error", "Something has broken, make sure to only input a proper key")
    return ciphertext
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with caesar method
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt, shift is not null
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def callCaesarEncrypt():
    if not Textboxformatter(plaintextBox.get("0.0", "end")):
        messagebox.showwarning("Plaintext Empty","Cannot encrypt nothing")
        return
    shift=caeserGenShift() #grab key and make sure I can do math with it
    plaintext=Textboxformatter(plaintextBox.get("0.0", "end"))
    ciphertext=caesarEncrypt(shift, plaintext)
    ciphertextBox.delete("0.0", "end")
    ciphertextBox.insert("0.0", ciphertext)

def caesarEncrypt(shift, plaintext):
    ciphertext=""
    plainNumbers=[]
    asciiList=list(''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ\n''')
    for i in plaintext:
        try:
            plainNumbers.append(asciiList.index(i))#using the list I provide, shift the letters around, this list can be configured at will
        except ValueError:
            messagebox.showwarning("Value Error",f"Bad character, {repr(i)} not in asciiList")
        except:
            messagebox.showwarning("Generic Error", "Something has broken, make sure to only input a proper numerical shift")
    cipherNumbers = [x+shift for x in plainNumbers] #add shift to all characters in plaintext
    for i in cipherNumbers:
        ciphertext+=asciiList[i%len(asciiList)] #swaps out the numbers for their respective character found in the asciilist (the mod operator prevents out of bound requests)
    return ciphertext
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with RSA method using the public key
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def callRSAPubEncrypt():
    if not Textboxformatter(plaintextBox.get("0.0", "end")):
        messagebox.showwarning("Plaintext Empty","Cannot encrypt nothing")
        return
    privateKey, publicKey = RSAGenKeys()
    plaintext=Textboxformatter(plaintextBox.get("0.0", "end"))
    ciphertext = RSAPubEncrypt(publicKey, plaintext)
    ciphertextBox.delete("0.0", "end")
    ciphertextBox.insert("0.0", ciphertext)

def RSAPubEncrypt(publicKey, plaintext):
    blockSize = 200 # specifies how large a text can be in characters before it will be split into another chunk
    ciphertext=""
    splitPlaintext = [plaintext[i:i+blockSize] for i in range(0, len(plaintext), blockSize)] #https://www.geeksforgeeks.org/python-divide-string-into-equal-k-chunks/
    #^ this allows RSA to be performed on text of any length given the valid characters sizes, after testing it broke with 214 bytes of text and not with 213, all valid characters are 1 byte so just chars = bytes and 200 seems fine
    for i in splitPlaintext:
        try:
            ciphertext+= rsa.encryptRSA(i, publicKey) + "♥♥♥♥♥" #using hearts as a delineator because it will not appear in encrypted RSA ever
        except:
            messagebox.showwarning("Generic Error", "Something has broken, make sure to only input properly formatted  output with the correct key")
    return ciphertext
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with base 64 method
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def callBase64Encrypt():
    if not Textboxformatter(plaintextBox.get("0.0", "end")):
        messagebox.showwarning("Plaintext Empty","Cannot encrypt nothing")
        return
    ciphertext=""
    plaintext=Textboxformatter(plaintextBox.get("0.0", "end"))
    ciphertext=base64Encrypt(plaintext)
    ciphertextBox.delete("0.0", "end")
    ciphertextBox.insert("0.0", ciphertext)

def base64Encrypt(plaintext):
    try:
        ciphertext=b64.b64encode(plaintext.encode()).decode("ascii") #turn plaintext into base 64
    except:
        messagebox.showwarning("Generic Error", "Something has broken")
    return ciphertext
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with substitution method
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def callSubstitutionEncrypt():
    if not Textboxformatter(plaintextBox.get("0.0", "end")):
        messagebox.showwarning("Plaintext Empty","Cannot encrypt nothing")
        return
    ciphertext=""
    plaintext=Textboxformatter(plaintextBox.get("0.0", "end"))
    ciphertext=substitutionEncrypt(plaintext)
    ciphertextBox.delete("0.0", "end")
    ciphertextBox.insert("0.0", ciphertext)

def substitutionEncrypt(plaintext):
    ciphertext=""
    for i in plaintext:
        try:
            ciphertext+=(str(ord(i)) + " ") #combine and get all the ascii values for the plaintext 
        except:
            messagebox.showwarning("Generic Error", "Something has broken")
    return ciphertext
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with trifid method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt, key is the same as the one used to encrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def callTrifidDecrypt(): # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ♥
    if not Textboxformatter(ciphertextBox.get("0.0", "end")):
        messagebox.showwarning("Ciphertext Empty","Cannot decrypt nothing")
        return
    if not keyBox.get():
        messagebox.showwarning("Key Empty","Cannot decrypt without key")
        return
    ciphertext=Textboxformatter(ciphertextBox.get("0.0", "end"))
    key=keyBox.get()
    plaintext = trifidDecrypt(key, ciphertext)
    plaintextBox.delete("0.0", "end")
    plaintextBox.insert("0.0", plaintext)

def trifidDecrypt(key, ciphertext): # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ♥
    cipherList=list(ciphertext)
    keyList=list(key.replace("♥","\n")) #allows keys to have ♥ instead of newline character, purely a cosmetic choice
    try:
        cipherKey=np.reshape(keyList,(5,5,5)) #reshape key into key cube
        xCoordinate = []
        yCoordinate = []
        zCoordinate = []
        for i in cipherList:
            for x in range(5):
                for y in range(5):
                    for z in range(5):
                        if cipherKey[x][y][z] == i: #turn plaintext into coordinates
                            xCoordinate.append(x)
                            yCoordinate.append(y)
                            zCoordinate.append(z)
        plainList=[]
        for i in range(len(cipherList)):
            plainList.append(cipherKey[xCoordinate[i]][yCoordinate[ (i+1) % len(cipherList)]][zCoordinate[ (i+2) % len(cipherList)]]) #shift coordinates back and write out the plaintext
        plaintext="".join(plainList)
        
    except ValueError:
        messagebox.showwarning("Value Error","Key too large or too small")
    except IndexError:
        messagebox.showwarning("Index Error","Character in plaintext that is not in the key")
    except:
        messagebox.showwarning("Generic Error", "Something has broken")
    return plaintext
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with caesar method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt, shift is the same as the one used to encrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def callCaesarDecrypt():
    if not Textboxformatter(ciphertextBox.get("0.0", "end")):
        messagebox.showwarning("Ciphertext Empty","Cannot decrypt nothing")
        return
    if not shiftBox.get():
        messagebox.showwarning("Shift Empty","Cannot decrypt without shift")
        return
    shift=int(shiftBox.get()) #grab key and make sure I can do math with it
    ciphertext=Textboxformatter(ciphertextBox.get("0.0", "end")) 
    plaintext=caesarDecrypt(shift, ciphertext)
    plaintextBox.delete("0.0", "end")
    plaintextBox.insert("0.0", plaintext)

def caesarDecrypt(shift, ciphertext):
    asciiList=list(''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ\n''')
    cipherNumbers=[]
    plaintext=""
    for i in ciphertext:
        try:
            cipherNumbers.append(asciiList.index(i))#using the list I provide, shift the letters around, this list can be configured at will
        except ValueError:
            messagebox.showwarning("Value Error",f"Character {repr(i)} not in asciiList")
        except:
            messagebox.showwarning("Generic Error", "Something has broken")
    plainNumbers = [x-shift for x in cipherNumbers] #use negative shift to all characters in plaintext because it is decryption
    for i in plainNumbers:
        plaintext+=asciiList[i%len(asciiList)] #using % to avoid shifts too large being a problem
    return plaintext

# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with RSA method and the private key
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def callRSAPrivDecrypt():
    if not Textboxformatter(ciphertextBox.get("0.0", "end")):
        messagebox.showwarning("Ciphertext Empty","Cannot decrypt nothing")
        return
    if not privateKeyBox.get():
        messagebox.showwarning("Private Key Empty","Cannot decrypt without privatekey")
        return
    privateKey = privateKeyBox.get()
    ciphertext=Textboxformatter(ciphertextBox.get("0.0", "end"))
    plaintext = RSAPrivDecrypt(privateKey, ciphertext)
    plaintextBox.delete("0.0", "end")
    plaintextBox.insert("0.0", plaintext)

def RSAPrivDecrypt(privateKey, ciphertext):
    try:
        cipherList=ciphertext.split("♥♥♥♥♥") #take apart the ciphertext that was crafted and then perform the decryption
    except:
        messagebox.showwarning("Generic Error", "Something has broken, ciphertext likely incorrectly formatted or broken")
    plaintext=""
    for i in cipherList:
        if i != "": #null part would make it break, this stops that
            try:
                plaintext+=rsa.decryptRSA(i, privateKey) #stitch back all of the pieces together
            except:
                messagebox.showwarning("Generic Error", "Something has broken, make sure the ciphertext is RSA encrypted with this key")
    return plaintext
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with base 64 method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def callBase64Decrypt():
    if not Textboxformatter(ciphertextBox.get("0.0", "end")):
        messagebox.showwarning("Ciphertext Empty","Cannot decrypt nothing")
        return
    plaintext=""
    ciphertext=Textboxformatter(ciphertextBox.get("0.0", "end"))
    try:
        plaintext=base64Decrypt(ciphertext)
    except ValueError:
        messagebox.showwarning("Value Error","string argument should contain only ASCII characters")
    except:
        messagebox.showwarning("Generic Error", "make sure to only input properly formatted base 64")
    plaintextBox.delete("0.0", "end")
    plaintextBox.insert("0.0", plaintext)

def base64Decrypt(ciphertext):
    plaintext=b64.b64decode(ciphertext).decode("ascii") #turn ciphertext from base 64
    return plaintext
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with substitution method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def callSubstitutionDecrypt():
    if not Textboxformatter(ciphertextBox.get("0.0", "end")):
        messagebox.showwarning("Ciphertext Empty","Cannot decrypt nothing")
        return
    plaintext=""
    ciphertext=Textboxformatter(ciphertextBox.get("0.0", "end"))
    try:
        plaintext=substitutionDecrypt(ciphertext)
    except ValueError:
        messagebox.showwarning("Value Error","Probably not numbers being decrypted")
    except:
        messagebox.showwarning("Generic Error", "Something has broken")
    plaintextBox.delete("0.0", "end")
    plaintextBox.insert("0.0", plaintext)

def substitutionDecrypt(ciphertext):
    cipherList=ciphertext.split() #take apart the list of the characters for each value
    plaintext=""
    for i in cipherList:
        plaintext+=chr(int(i))
    return plaintext
# ---------------------------------------------------------------#
"""
    Purpose: changes password of user based on the UID provided
    Requirement: there is a given UID and has a valid user and the password is not null
    Promise: change only the password of the user with the given UID
"""
# ---------------------------------------------------------------#
def changePassword():
    if not passwordBox.get() or not UIDBox.get():
        messagebox.showwarning("Password or UID empty","Cannot change password without password and UID provided")
        return
    password=passwordBox.get()
    UID=UIDBox.get()# simple get function from Entry boxes, takes in whatever was the user input into the UID box
    if pipeCheck(password):
        messagebox.showwarning("Password Pipe","Password cannot contain the pipe character, |")
        return

    credentialsFile = open("credentials.txt", "r")
    if os.name == 'nt':
        os.system('copy credentials.txt backupcredentials.txt')
    elif os.name == 'posix':
        os.system('cp credentials.txt backupcredentials.txt')
    
    UIDExists=False
    try:
        for line in credentialsFile:
            line = line.split("|", 2)
            if UID == line[2].replace('\n', ''):
                UIDExists=True
            UID=line[2].replace('\n', '')
            newUID= int(UID)+1
    except UnboundLocalError:
        messagebox.showwarning("Unbound Local Error","Verify user inputs are accurate")
    except:
        messagebox.showwarning("Generic Error","Verify user inputs are accurate")
    credentialsFile.close()

    if not UIDExists:
        messagebox.showwarning("UID Does Not Exist","UID does not exist, verify input")
        return
    
    newUID="0"
    newCredentialsFile = open("newcredentials.txt", "w") #write will automatically create file if it doesnt exist already (which it shouldn't) and if it does, it truncates it and its fine
    try:
        for line in credentialsFile:
            line = line.split("|", 2) #the pipe is the seperator that I use in the user/pass/UID file
            if UID == line[2].replace('\n', ''): #newlines bad >:(, only change the password for the person with specified UID
                line[1] = password
            newCredentialsFile.write(line[0] + "|" + line[1] + "|" + str(newUID) + "\n") #put the file back together
            newUID= int(line[2])+1 #keep the UIDs incrementing each time but also not break 
    except UnboundLocalError:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Unbound Local Error","Verify user inputs are accurate")
    except:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Generic Error","Verify user inputs are accurate")
    
    newCredentialsFile.close() #close the document
    credentialsFile.close() #close the document
    os.remove("credentials.txt")
    os.remove("backupcredentials.txt")# removes the file credentials txt to free up the name
    os.rename("newcredentials.txt", "credentials.txt")# renames the newly written credentials file to the original name
# ---------------------------------------------------------------#
"""
    Purpose: changes username of user based on the UID provided
    Requirement: there is a given UID and has a valid user and the username is not null
    Promise: change only the username of the user with the given UID
"""
# ---------------------------------------------------------------#
def changeUsername():
    if not usernameBox.get() or not UIDBox.get():
        messagebox.showwarning("Username or UID empty","Cannot change username without username and UID provided")
        return
    username=usernameBox.get()
    UID=UIDBox.get()

    if pipeCheck(username):
        messagebox.showwarning("Username Pipe","Username cannot contain the pipe character, |")
        return

    credentialsFile = open("credentials.txt", "r")
    newCredentialsFile = open("newcredentials.txt", "a") #write will automatically create file if it doesnt exist already (which it shouldn't) and if it does, it truncates it and its fine
    newUID="0"

    try:
        for line in credentialsFile:
            line = line.split("|", 2)#the pipe is the seperator that I use in the user/pass/UID file
            if UID == line[2].replace('\n', ''): #newlines bad >:(, only change the username for the person with specified UID
                line[0] = username
            newCredentialsFile.write(line[0] + "|" + line[1] + "|" + str(newUID) + "\n") #put the file back together
            newUID= int(line[2])+1 #keep the UIDs incrementing each time but also not break 
    except UnboundLocalError:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Unbound Local Error","Verify user inputs are accurate")
    except:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Generic Error","Verify user inputs are accurate")
    
    newCredentialsFile.close()
    credentialsFile.close()
    
    try:
        os.remove("credentials.txt")
        os.remove("backupcredentials.txt")
        os.rename("newcredentials.txt", "credentials.txt")
    except:
        messagebox.showwarning("Generic Error", "File deletion failed somehow, probably not an issue")
# ---------------------------------------------------------------#
"""
    Purpose: make new user and automatically assign it a UID
    Requirement: have a unique username and a not null password
    Promise: add user with given details to credentials.txt file
"""
# ---------------------------------------------------------------#
def newUser():
    if not usernameBox.get() or not passwordBox.get():
        messagebox.showwarning("Username or Password Empty","Cannot add user without both a username and a password")
        return
    password=passwordBox.get()
    username=usernameBox.get()
    if pipeCheck(password):
        messagebox.showwarning("Password Pipe","Password cannot contain the pipe character, |")
        return

    if pipeCheck(username):
        messagebox.showwarning("Username Pipe","Username cannot contain the pipe character, |")
        return

    if usernameExists(username):
        messagebox.showwarning("Bad Username", "Username already exists")
        return
    
    newUID=int(UIDBox.get()) + 1
    credentialsFile = open("credentials.txt", "a") #now actually write in the new user since its all good
    try:
        credentialsFile.write(username + "|" + password + "|" + str(newUID) + "\n")
    except:
        messagebox.showwarning("Generic Error","Verify user inputs are accurate")
    credentialsFile.close()
# ---------------------------------------------------------------#
"""
    Purpose: remove user from credentials.txt file based on UID
    Requirement: press remove user button
    Promise: remove user with given UID from credentials.txt and reordering the following users which will change all the UID
"""
# ---------------------------------------------------------------#
def removeuser():
    if not usernameBox.get() and not UIDBox.get():
        messagebox.showwarning("Username and UID Empty","Cannot remove user when no username or UID provided")
        return
    username=usernameBox.get()
    UID=UIDBox.get()
    
    if pipeCheck(username):
        messagebox.showwarning("Username Pipe","Username cannot contain the pipe character, |")
        return

    credentialsFile = open("credentials.txt", "r")
    if os.name == 'nt':
        os.system('copy credentials.txt backupcredentials.txt')
    elif os.name == 'posix':
        os.system('cp credentials.txt backupcredentials.txt')

    if not usernameExists(username):
        messagebox.showwarning("Bad Username", "Username does not exist")
        return
    newUID="0"
    replacedUsers=0
    
    newCredentialsFile = open("newcredentials.txt", "w") #write will automatically create file if it doesnt exist already (which it shouldn't) and if it does, it truncates it and its fine
    try:
        for line in credentialsFile:
            line = line.split("|", 2)#the pipe is the seperator that I use in the user/pass/UID file
            if UID == line[2].replace('\n', '') or username == line[0].replace("\n", ""): #newlines bad >:(, only remove user with specified UID or specified username
                newUID= int(line[2])
                replacedUsers+=1
            else:
                newCredentialsFile.write(line[0] + "|" + line[1] + "|" + str(newUID) + "\n")#put the file back together

            newUID= int(line[2]) + 1 - replacedUsers #keep the UIDs incrementing each time but also not break, now accounting for the users removed, this was the easiest solution I could think of
    except UnboundLocalError:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Unbound Local Error","Verify user inputs are accurate")
    except:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Generic Error","Verify user inputs are accurate")
    
    newCredentialsFile.close()
    credentialsFile.close()
    
    try:
        os.remove("credentials.txt")
        os.remove("backupcredentials.txt")
        os.rename("newcredentials.txt", "credentials.txt")
    except:
        messagebox.showwarning("Generic Error", "File deletion failed somehow, probably not an issue")

def getUID():
    if not usernameBox.get():
        messagebox.showwarning("Username Empty","UID cannot be returned from nothing")
        return
    username=usernameBox.get()

    if not usernameExists(username):
        messagebox.showwarning("Bad Username", "Username does not exist")
        return
    credentialsFile = open("credentials.txt", "r")
    if os.name == 'nt':
        os.system('copy credentials.txt backupcredentials.txt')
    elif os.name == 'posix':
        os.system('cp credentials.txt backupcredentials.txt')
    newCredentialsFile = open("newcredentials.txt", "w") #write will automatically create file if it doesnt exist already (which it shouldn't) and if it does, it truncates it and its fine
    try:
        for line in credentialsFile:
            line = line.split("|", 2)#the pipe is the seperator that I use in the user/pass/UID file
        if username == line[0].replace('\n', ''): #newlines bad >:(, only remove user with specified UID or specified username
            UID = int(line[2])
            newCredentialsFile.write(line[0] + "|" + line[1] + "|" + line[2].replace('\n', '') + "\n")
        else:
            newCredentialsFile.write(line[0] + "|" + line[1] + "|" + line[2].replace('\n', '') + "\n")#put the file back together
            UIDBox.delete(0, "end")
            UIDBox.insert(0, UID)
    except UnboundLocalError:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Unbound Local Error","Verify user inputs are accurate")
    except:
        if os.name == 'nt':
            os.system('copy backupcredentials.txt credentials.txt')
        elif os.name == 'posix':
            os.system('cp backupcredentials.txt credentials.txt')
        messagebox.showwarning("Generic Error","Verify user inputs are accurate")
    
    newCredentialsFile.close()
    credentialsFile.close()
    
    try:
        os.remove("credentials.txt")
        os.remove("backupcredentials.txt")
        os.rename("newcredentials.txt", "credentials.txt")
    except:
        messagebox.showwarning("Generic Error", "File deletion failed somehow, probably not an issue")

# ---------------------------------------------------------------#
"""
    Purpose: check if user has valid credentials before initialising program
    Requirement: submit valid username and password
    Promise: initialise program
"""
# ---------------------------------------------------------------#
if ls.start():
    window=customtkinter.CTk()
    window.rowconfigure(index=[0, 1, 2, 3, 4], minsize=110)
    window.columnconfigure(index=0, minsize=110)
    #window.minsize(366, 550)
    #window.maxsize(366, 550)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(BASE_DIR, 'School_logo_Lake_G.ico') #Lake G ico for both windows
    window.iconbitmap(icon_path)
    window.title("EncryptionProgram") #nice name :D
    trifidButton=customtkinter.CTkButton(window, border_width=1, corner_radius=3 , fg_color="#3f5799", command= trifid, text="Trifid", text_color="black") #all the method buttons
    caesarButton=customtkinter.CTkButton(window, border_width=1, corner_radius=3 , fg_color="#3f5799", command= caesar, text="Caesar", text_color="black")
    RSAButton=customtkinter.CTkButton(window, border_width=1, corner_radius=3 , fg_color="#3f5799", command= RSA, text="RSA", text_color="black")
    b64Button=customtkinter.CTkButton(window, border_width=1, corner_radius=3 , fg_color="#3f5799", command= base64, text="Base 64", text_color="black")
    substitutionButton=customtkinter.CTkButton(window, border_width=1, corner_radius=3 , fg_color="#3f5799", command= substitution, text="Substitution", text_color="black")
    
    changeDetailsButton=customtkinter.CTkButton(window, height=1, width=7, border_width=1, corner_radius=2 , fg_color="#3f5799", command= changeDetails, text="Details", text_color="black") #detail button

    trifidButton.grid(column=0, row=0, sticky="nsew") # unlike a lot of the other widgets, we always want these ones visible and accessible so they are put into the window at the start
    caesarButton.grid(column=0, row=1, sticky="nsew")
    RSAButton.grid(column=0, row=2, sticky="nsew")
    b64Button.grid(column=0, row=3, sticky="nsew")
    substitutionButton.grid(column=0, row=4, sticky="nsew")
    changeDetailsButton.grid(column=1, row=0, sticky="ne")

    plaintextLabel=customtkinter.CTkLabel(window, text="Plaintext:")
    plaintextBox=customtkinter.CTkTextbox(window, height=3) # the plaintext and cipihertext fields need to be Text to allow multiline messages to be easily visible for the end user
    ciphertextLabel=customtkinter.CTkLabel(window, text="Ciphertext:")
    ciphertextBox=customtkinter.CTkTextbox(window, height=3)

    usernameBox=customtkinter.CTkEntry(window, textvariable="", justify="left") #username/password/UID boxes and labels
    passwordBox=customtkinter.CTkEntry(window, textvariable="", justify="left")
    UIDBox=customtkinter.CTkEntry(window, textvariable="", justify="left")
    usernameLabel=customtkinter.CTkLabel(window, text="Username:")
    passwordLabel=customtkinter.CTkLabel(window, text="Password:")
    UIDLabel=customtkinter.CTkLabel(window, text="UID:")

    encryptButton=customtkinter.CTkButton(window, text="Encrypt", fg_color="#d833de") #enc/dec buttons
    decryptButton=customtkinter.CTkButton(window, text="Decrypt", fg_color="#d833de")

    changePasswordButton=customtkinter.CTkButton(window, height=1, width=22, border_width=1, fg_color="#d833de", command= changePassword, text="changePassword", text_color="black", corner_radius=2, border_spacing=10) #buttons that call their namesake function
    changeUsernameButton=customtkinter.CTkButton(window, height=1, width=22, border_width=1, fg_color="#d833de", command= changeUsername, text="changeUsername", text_color="black", corner_radius=2, border_spacing=10)# everything other than the command is cosmetic
    newUserButton=customtkinter.CTkButton(window, height=1, width=11, border_width=1, fg_color="#d833de", command= newUser, text="newUser", text_color="black", corner_radius=2, border_spacing=10)
    removeUserButton=customtkinter.CTkButton(window, height=1, width=18, border_width=1, fg_color="#d833de", command= removeuser, text="removeuser", text_color="black", corner_radius=2, border_spacing=10)
    getUIDButton=customtkinter.CTkButton(window, height=1, width=18, border_width=1, fg_color="#d833de", command= getUID, text="getUID", text_color="black", corner_radius=2, border_spacing=10)

    keyBox=customtkinter.CTkEntry(window, textvariable="", justify="left") #trifid key box/label, independant because that way it is kept when using other methods
    keyLabel=customtkinter.CTkLabel(window, text="Key:")

    shiftBox=customtkinter.CTkEntry(window, textvariable="", justify="left") #caesar shift
    shiftLabel=customtkinter.CTkLabel(window, text="Shift:")

    privateKeyBox=customtkinter.CTkEntry(window, textvariable="", justify="left")
    privateKeyLabel=customtkinter.CTkLabel(window, text="Private Key:") #priv/pub key

    publicKeyBox=customtkinter.CTkEntry(window, textvariable="", justify="left")
    publicKeyLabel=customtkinter.CTkLabel(window, text="Public Key:")

    window.mainloop()