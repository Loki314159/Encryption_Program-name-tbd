import tkinter as tk
import numpy as np
import base64 as b64
import RSA as rsa
import LoginScreenLite as ls
import os
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
# ---------------------------------------------------------------#
"""
    Purpose: make all buttons light blue to allow the focused method be turned dark blue and focused
    Requirement: be called
    Promise: all buttons will be turned light blue
"""
# ---------------------------------------------------------------#
def lightBlueButtons():
    trifidButton.config(bg="lightblue", fg="black")
    caesarButton.config(bg="lightblue", fg="black")
    RSAButton.config(bg="lightblue", fg="black")
    b64Button.config(bg="lightblue", fg="black")
    substitutionButton.config(bg="lightblue", fg="black")
    changeDetailsButton.config(bg="lightblue", fg="black")
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
    privateKeyBox.delete(0, tk.END)# this will delete everything in the Entry box from the start (0) to the end (tk.END)
    privateKeyBox.insert(0, privateKey)# this will place the privateKey in the privatekeybox at the start (0)
    publicKeyBox.delete(0, tk.END)
    publicKeyBox.insert(0, publicKey)
    return privateKey, publicKey # returns both keys to the operation that called the function
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
    print("trifid")
    forgetAll()
    lightBlueButtons()
    trifidButton.config(bg="blue", fg="white")
    decryptButton.config(command=trifidDecrypt)
    encryptButton.config(command=trifidEncrypt)# changes the configuration of the button so that it calls the specified command
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
    lightBlueButtons()
    print("caesar")
    caesarButton.config(bg="blue", fg="white")
    decryptButton.config(command=caesarDecrypt)
    encryptButton.config(command=caesarEncrypt)
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
# ---------------------------------------------------------------#
"""
    Purpose: set widgets to be for the base64 method
    Requirement: base64 button pressed
    Promise: initialise base64 and common widgets
"""
# ---------------------------------------------------------------#
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
# ---------------------------------------------------------------#
"""
    Purpose: set widgets to be for the substitution method
    Requirement: Substitution button pressed
    Promise: initialise substitution and common widgets
"""
# ---------------------------------------------------------------#
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
# ---------------------------------------------------------------#
"""
    Purpose: set widgets for user management
    Requirement: details button pressed
    Promise: initialise details and common widgets
"""
# ---------------------------------------------------------------#
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

# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with trifid method
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt, key is 125 characters and all characters in the plaintext are also in the key
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def trifidEncrypt(): # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼—½¿Ƚ♥
    ciphertext=""   # example key^^^
    plainList=list(Textboxformatter(plaintextBox.get("1.0", tk.END))) # gets the text from the plaintext Text field before removing the unnecessary newline character to avoid incorrect encryption
    keyList=list(keyBox.get().replace("♥","\n")) #allows keys to have ♥ instead of newline character, purely a cosmetic change
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
    ciphertextBox.delete("1.0", tk.END) # the formatting to delete things from Text widgets is slightly different to Entry widgets as shown previously, this deletes everything in it
    ciphertextBox.insert("1.0", ciphertext) # similar difference here, just inserts ciphertext
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with caesar method
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt, shift is not null
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def caesarEncrypt():
    ciphertext=""
    asciiList=list(''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ\n''')
    shift=int(shiftBox.get()) #grab key and make sure I can do math with it
    plaintext=Textboxformatter(plaintextBox.get("1.0", tk.END))
    plainNumbers=[]
    for i in plaintext:
        plainNumbers.append(asciiList.index(i)) #using the list I provide, shift the letters around, this list can be configured at will
    cipherNumbers = [x+shift for x in plainNumbers] #add shift to all characters in plaintext
    for i in cipherNumbers:
        ciphertext+=asciiList[i%len(asciiList)] #swaps out the numbers for their respective character found in the asciilist (the mod operator prevents out of bound requests)
    ciphertextBox.delete("1.0", tk.END)
    ciphertextBox.insert("1.0", ciphertext)
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with RSA method using the public key
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def RSAPubEncrypt():
    privateKey, publicKey = RSAGenKeys()
    ciphertext=""
    plaintext=Textboxformatter(plaintextBox.get("1.0", tk.END))
    blockSize = 200 # specifies how large a text can be in characters before it will be split into another chunk
    splitPlaintext = [plaintext[i:i+blockSize] for i in range(0, len(plaintext), blockSize)] #https://www.geeksforgeeks.org/python-divide-string-into-equal-k-chunks/
    #^ this allows RSA to be performed on text of any length given the valid characters sizes, after testing it broke with 214 bytes of text and not with 213, all valid characters are 1 byte so just chars = bytes and 200 seems fine
    for i in splitPlaintext:
        ciphertext+= rsa.encryptRSA(i, publicKey) + "♥♥♥♥♥" #using hearts as a delineator because it will not appear in encrypted RSA ever
    
    ciphertextBox.delete("1.0", tk.END)
    ciphertextBox.insert("1.0", ciphertext)
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with base 64 method
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def base64Encrypt():
    ciphertext=""
    plaintext=Textboxformatter(plaintextBox.get("1.0", tk.END))
    ciphertext=b64.b64encode(plaintext.encode()).decode("ascii") #turn plaintext into base 64
    ciphertextBox.delete("1.0", tk.END)
    ciphertextBox.insert("1.0", ciphertext)
# ---------------------------------------------------------------#
"""
    Purpose: Encrypt plaintext with substitution method
    Requirement: Encrypt button be pressed, there is a plaintext to encrypt
    Promise: place encrypted plaintext in ciphertext box
"""
# ---------------------------------------------------------------#
def substitutionEncrypt():
    ciphertext=""
    plaintext=Textboxformatter(plaintextBox.get("1.0", tk.END))
    for i in plaintext:
        ciphertext+=(str(ord(i)) + " ") #combine and get all the ascii values for the plaintext 
    ciphertextBox.delete("1.0", tk.END)
    ciphertextBox.insert("1.0", ciphertext)

# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with trifid method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt, key is the same as the one used to encrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def trifidDecrypt(): # !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ♥
    cipherList=list(Textboxformatter(ciphertextBox.get("1.0", tk.END)))
    keyList=list(keyBox.get().replace("♥","\n")) #allows keys to have ♥ instead of newline character, purely a cosmetic change
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
    plaintextBox.delete("1.0", tk.END)
    plaintextBox.insert("1.0", plaintext)
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with caesar method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt, shift is the same as the one used to encrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def caesarDecrypt():
    asciiList=list(''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ\n''')
    plaintext=""
    shift=int(shiftBox.get()) #grab key and make sure I can do math with it
    ciphertext=Textboxformatter(ciphertextBox.get("1.0", tk.END)) 
    cipherNumbers=[]
    for i in ciphertext:
        cipherNumbers.append(asciiList.index(i))#using the list I provide, shift the letters around, this list can be configured at will
    plainNumbers = [x-shift for x in cipherNumbers] #use negative shift to all characters in plaintext because it is decryption
    for i in plainNumbers:
        plaintext+=asciiList[i%len(asciiList)] #using % to avoid shifts too large being a problem
    plaintextBox.delete("1.0", tk.END)
    plaintextBox.insert("1.0", plaintext)
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with RSA method and the private key
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def RSAPrivDecrypt():
    privateKey, publicKey = RSAGenKeys()
    plaintext=""
    ciphertext=Textboxformatter(ciphertextBox.get("1.0", tk.END))
    cipherList=ciphertext.split("♥♥♥♥♥") #take apart the ciphertext that was crafted and then perform the decryption
    print(cipherList)
    for i in cipherList:
        if i != "": #null part would make it break, this stops that
            plaintext+=rsa.decryptRSA(i, privateKey) #stitch back all of the pieces together
    plaintextBox.delete("1.0", tk.END)
    plaintextBox.insert("1.0", plaintext)
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with base 64 method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def base64Decrypt():
    plaintext=""
    ciphertext=Textboxformatter(ciphertextBox.get("1.0", tk.END))
    plaintext=b64.b64decode(ciphertext).decode("ascii") #turn ciphertext from base 64
    plaintextBox.delete("1.0", tk.END)
    plaintextBox.insert("1.0", plaintext)
# ---------------------------------------------------------------#
"""
    Purpose: Decrypt ciphertext with substitution method
    Requirement: Decrypt button be pressed, there is a ciphertext to decrypt
    Promise: place decrypted ciphertext in plaintext box
"""
# ---------------------------------------------------------------#
def substitutionDecrypt():
    plaintext=""
    cipherList=Textboxformatter(ciphertextBox.get("1.0", tk.END)).split() #take apart the list and return the characters for each value
    for i in cipherList:
        plaintext+=chr(int(i))
    plaintextBox.delete("1.0", tk.END)
    plaintextBox.insert("1.0", plaintext)

# ---------------------------------------------------------------#
"""
    Purpose: changes password of user based on the uid provided
    Requirement: there is a given uid and has a valid user and the password is not null
    Promise: change only the password of the user with the given uid
"""
# ---------------------------------------------------------------#
def changePassword():
    print("changepass")
    password=passwordBox.get()
    uid=uidBox.get()# simple get function from Entry boxes, takes in whatever was the user input into the uid box
    
    credentialsFile = open("credentials.txt", "r")
    newCredentialsFile = open("newcredentials.txt", "w") #write will automatically create file if it doesnt exist already (which it shouldn't) and if it does, it truncates it and its fine
    newuid="0"
    if password=="":#verify the user input was not null for password or uid (it would be bad to have a null password and no user specified means it is an unnecessary operation)
        return
    if uid=="":
        return
    for line in credentialsFile:
        line = line.split("|", 2) #the pipe is the seperator that I use in the user/pass/uid file
        if uid == line[2].replace('\n', ''): #newlines bad >:(, only change the password for the person with specified uid
            line[1] = password
        newCredentialsFile.write(line[0] + "|" + line[1] + "|" + str(newuid) + "\n") #put the file back together
        newuid= int(line[2])+1 #keep the uids incrementing each time but also not break 
    
    newCredentialsFile.close() #close the document
    credentialsFile.close() #close the document
    os.remove("credentials.txt")# removes the file credentials txt to free up the name
    os.rename("newcredentials.txt", "credentials.txt")# renames the newly written credentials file to the original name
# ---------------------------------------------------------------#
"""
    Purpose: changes username of user based on the uid provided
    Requirement: there is a given uid and has a valid user and the username is not null
    Promise: change only the username of the user with the given uid
"""
# ---------------------------------------------------------------#
def changeUsername():
    print("changeuser")
    username=usernameBox.get()
    uid=uidBox.get()
    
    credentialsFile = open("credentials.txt", "r")
    newCredentialsFile = open("newcredentials.txt", "a") #write will automatically create file if it doesnt exist already (which it shouldn't) and if it does, it truncates it and its fine
    newuid="0"
    if username=="": 
        return
    if uid=="":
        return
    for line in credentialsFile:
        line = line.split("|", 2)#the pipe is the seperator that I use in the user/pass/uid file
        if uid == line[2].replace('\n', ''): #newlines bad >:(, only change the username for the person with specified uid
            line[0] = username
        newCredentialsFile.write(line[0] + "|" + line[1] + "|" + str(newuid) + "\n") #put the file back together
        newuid= int(line[2])+1 #keep the uids incrementing each time but also not break 
    
    newCredentialsFile.close()
    credentialsFile.close()
    os.remove("credentials.txt")
    os.rename("newcredentials.txt", "credentials.txt")
# ---------------------------------------------------------------#
"""
    Purpose: make new user and automatically assign it a uid
    Requirement: have a unique username and a not null password
    Promise: add user with given details to credentials.txt file
"""
# ---------------------------------------------------------------#
def newUser():
    print("newuser")
    password=passwordBox.get()
    username=usernameBox.get()

    credentialsFile = open("credentials.txt", "r") #make sure the username & password are not null
    if username == "":
        credentialsFile.close()
        return
    if password == "":
        credentialsFile.close()
        return
    for line in credentialsFile:
        line = line.split("|", 2)
        print(line)
        if username == line[0].replace('\n', ''): #if the username is already taken do nothing
            return
        uid=line[2].replace('\n', '')
    credentialsFile.close()

    newuid= int(uid)+1
    credentialsFile = open("credentials.txt", "a") #now actually write in the new user since its all good
    credentialsFile.write(username + "|" + password + "|" + str(newuid) + "\n")    
    credentialsFile.close()
# ---------------------------------------------------------------#
"""
    Purpose: remove user from credentials.txt file based on uid
    Requirement: press remove user button
    Promise: remove user with given uid from credentials.txt and reordering the following users which will change all the uid
"""
# ---------------------------------------------------------------#
def removeuser():
    print("removeuser")
    username=usernameBox.get()
    uid=uidBox.get()
    
    credentialsFile = open("credentials.txt", "r")
    newCredentialsFile = open("newcredentials.txt", "w") #write will automatically create file if it doesnt exist already (which it shouldn't) and if it does, it truncates it and its fine
    newuid="0"
    replacedUsers=0
    for line in credentialsFile:
        line = line.split("|", 2)#the pipe is the seperator that I use in the user/pass/uid file
        if uid == line[2].replace('\n', '') or username == line[0].replace("\n", ""): #newlines bad >:(, only remove user with specified uid or specified username
            newuid= int(line[2])
            replacedUsers+=1
        else:
            newCredentialsFile.write(line[0] + "|" + line[1] + "|" + str(newuid) + "\n")#put the file back together
            
        newuid= int(line[2]) + 1 - replacedUsers #keep the uids incrementing each time but also not break, now accounting for the users removed, this was the easiest solution I could think of
    
    newCredentialsFile.close()
    credentialsFile.close()
    os.remove("credentials.txt")
    os.rename("newcredentials.txt", "credentials.txt")

# ---------------------------------------------------------------#
"""
    Purpose: check if user has valid credentials before initialising program
    Requirement: submit valid username and password
    Promise: initialise program
"""
# ---------------------------------------------------------------#
if ls.start():
    window=tk.Tk()
    window.rowconfigure(index=[0, 1, 2, 3, 4], minsize=110)
    window.columnconfigure(index=0, minsize=110)
    window.minsize(366, 550)
    #window.maxsize(366, 550)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(BASE_DIR, 'School_logo_Lake_G.ico') #Lake G ico for both windows
    window.iconbitmap(icon_path)
    window.title("EncryptionProgram") #nice name :D
    Frame1=tk.Frame(window)
    trifidButton=tk.Button(borderwidth=7, bg="lightblue", command= trifid, text="Trifid") #all the method buttons
    caesarButton=tk.Button(borderwidth=7, bg="lightblue", command= caesar, text="Caesar")
    RSAButton=tk.Button(borderwidth=7, bg="lightblue", command= RSA, text="RSA")
    b64Button=tk.Button(borderwidth=7, bg="lightblue", command= base64, text="Base 64")
    substitutionButton=tk.Button(borderwidth=7, bg="lightblue", command= substitution, text="Substitution")
    
    changeDetailsButton=tk.Button(height=1, width=7, borderwidth=3, bg="lightblue", command= changeDetails, text="Details") #detail button

    trifidButton.grid(column=0, row=0, sticky="nsew") # unlike a lot of the other widgets, we always want these ones visible and accessible so they are put into the window at the start
    caesarButton.grid(column=0, row=1, sticky="nsew")
    RSAButton.grid(column=0, row=2, sticky="nsew")
    b64Button.grid(column=0, row=3, sticky="nsew")
    substitutionButton.grid(column=0, row=4, sticky="nsew")
    changeDetailsButton.grid(column=1, row=0, sticky="ne")

    plaintextLabel=tk.Label(text="Plaintext:")
    plaintextBox=tk.Text(height=3) # the plaintext and cipihertext fields need to be Text to allow multiline messages to be easily visible for the end user
    ciphertextLabel=tk.Label(text="Ciphertext:")
    ciphertextBox=tk.Text(height=3)

    usernameBox=tk.Entry(textvariable="", justify="left") #username/password/uid boxes and labels
    passwordBox=tk.Entry(textvariable="", justify="left")
    uidBox=tk.Entry(textvariable="", justify="left")
    usernameLabel=tk.Label(text="Username:")
    passwordLabel=tk.Label(text="Password:")
    uidLabel=tk.Label(text="UID:")

    encryptButton=tk.Button(text="Encrypt", bg="hotpink") #enc/dec buttons
    decryptButton=tk.Button(text="Decrypt", bg="hotpink")

    changePasswordButton=tk.Button(height=1, width=22, borderwidth=3, bg="lightblue", command= changePassword, text="changePassword") #buttons that call their namesake function
    changeUsernameButton=tk.Button(height=1, width=22, borderwidth=3, bg="lightblue", command= changeUsername, text="changeUsername")# everything other than the command is cosmetic
    newUserButton=tk.Button(height=1, width=11, borderwidth=3, bg="lightblue", command= newUser, text="newUser")
    removeUserButton=tk.Button(height=1, width=18, borderwidth=3, bg="lightblue", command= removeuser, text="removeuser")

    keyBox=tk.Entry(textvariable="", justify="left") #trifid key box/label, independant because that way it is kept when using other methods
    keyLabel=tk.Label(text="Key:")

    shiftBox=tk.Entry(textvariable="", justify="left") #caesar shift
    shiftLabel=tk.Label(text="Shift:")

    privateKeyBox=tk.Entry(textvariable="", justify="left")
    privateKeyLabel=tk.Label(text="Private Key:") #priv/pub key

    publicKeyBox=tk.Entry(textvariable="", justify="left")
    publicKeyLabel=tk.Label(text="Public Key:")

    window.mainloop()