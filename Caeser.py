from tkinter import messagebox
def caesarEncrypt(shift, plaintext):
    ciphertext=""
    plainNumbers=[]
    asciiList=list(''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ\n''')
    for i in plaintext:
        try:
            plainNumbers.append(asciiList.index(i))#using the list I provide, shift the letters around, this list can be configured at will
        except ValueError:
            messagebox.showwarning("Value Error",f"Bad character, {repr(i)} not in asciiList")
        except Exception as e:
            messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
    cipherNumbers = [x+shift for x in plainNumbers] #add shift to all characters in plaintext
    for i in cipherNumbers:
        ciphertext+=asciiList[i%len(asciiList)] #swaps out the numbers for their respective character found in the asciilist (the mod operator prevents out of bound requests)
    return ciphertext

def caesarDecrypt(shift, ciphertext):
    asciiList=list(''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬¯°±²Þµ¶·œ¹º»¼ʧ½¿Ƚ\n''')
    cipherNumbers=[]
    plaintext=""
    for i in ciphertext:
        try:
            cipherNumbers.append(asciiList.index(i))#using the list I provide, shift the letters around, this list can be configured at will
        except ValueError:
            messagebox.showwarning("Value Error",f"Character {repr(i)} not in asciiList")
        except Exception as e:
            messagebox.showwarning("Generic Error",f"Error occured: {str(e)}")
    plainNumbers = [x-shift for x in cipherNumbers] #use negative shift to all characters in plaintext because it is decryption
    for i in plainNumbers:
        plaintext+=asciiList[i%len(asciiList)] #using % to avoid shifts too large being a problem
    return plaintext