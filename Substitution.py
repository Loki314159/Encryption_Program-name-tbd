from tkinter import messagebox

def substitutionEncrypt(plaintext):
    ciphertext=""
    for i in plaintext:
        try:
            ciphertext+=(str(ord(i)) + " ") #combine and get all the ascii values for the plaintext 
        except Exception as e:
            messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
    return ciphertext

def substitutionDecrypt(ciphertext):
    try:
        cipherList=ciphertext.split() #take apart the list of the characters for each value
        plaintext=""
        for i in cipherList:
            plaintext+=chr(int(i))
    except Exception as e:
        messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
    return plaintext
