from tkinter import messagebox
import base64 as b64

def base64Encrypt(plaintext):
    try:
        ciphertext=b64.b64encode(plaintext.encode()).decode("ascii") #turn plaintext into base 64
    except Exception as e:
        messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
        return
    return ciphertext

def base64Decrypt(ciphertext):
    try:
        plaintext=b64.b64decode(ciphertext).decode("ascii") #turn ciphertext from base 64
    except ValueError:
        messagebox.showwarning("Value Error","string argument should contain only ASCII characters")
    except Exception as e:
        messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
        return
    return plaintext
