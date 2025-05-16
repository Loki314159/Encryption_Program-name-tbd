from tkinter import messagebox
import numpy as np
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
    except Exception as e:
                messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
    return ciphertext

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
    except Exception as e:
                messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
    return plaintext