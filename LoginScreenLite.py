import tkinter as tk
from tkinter import messagebox
import os


def start():
    global loginWindow
    loginWindow = setupWindow()
    loginWindow.title("Login")
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(BASE_DIR, 'School_logo_Lake_G.ico')
    loginWindow.iconbitmap(icon_path)
    loginWindow.mainloop()
    return True

def setupWindow():
    loginWindow = tk.Tk()
    loginWindow.geometry("250x100")
    loginWindow.minsize(250,100)
    loginWindow.maxsize(250,100)
    loginWindow.protocol("WM_DELETE_WINDOW", disable_close)
    loginWindow.rowconfigure([0, 1, 2], minsize=1)
    loginWindow.columnconfigure([0, 1], minsize=1)
    unameLabel = tk.Label(text="Username: ", width=10)
    loginWindow.unameText = tk.Entry(master=loginWindow, width=25)
    loginWindow.unameText.bind("<Return>", login)
    unameLabel.grid(row=0, column=0, sticky="ew", pady=5, padx=1)
    loginWindow.unameText.grid(row=0, column=1, sticky="ew", pady=5, padx=1)
    pwordLabel = tk.Label(text="Password: ", width=10)
    loginWindow.pwordText = tk.Entry(master=loginWindow, width=25, show="*")
    loginWindow.pwordText.bind("<Return>", login)
    pwordLabel.grid(row=1, column=0, sticky="ew", pady=5, padx=1)
    loginWindow.pwordText.grid(row=1, column=1, sticky="ew", pady=5, padx=1)


    enterButton = tk.Button(text="Login", width=15, command=login)
    enterButton.grid(row=2, column=0, columnspan=2)

    return loginWindow


def disable_close():
    messagebox.showwarning("No Closing", "Sorry, you didn't say the magic words... \nTry again")

def login(event=None):
    if testLogin():
        loginWindow.destroy()

def testLogin():
    userUName = loginWindow.unameText.get()
    userPWord = loginWindow.pwordText.get()# get the value from the entry box

    credentialsFile = open("credentials.txt", "r")

    for line in credentialsFile:
        line = line.split("|", 2)# the formatting oof the credentials file is username|password|uid therefore the seperation will allow each value to be interacted with independently
        knownUName = line[0].replace('\n', '')# there should not me newline characters
        knownPWord = line[1].replace('\n', '')
        if userUName == knownUName and userPWord == knownPWord:
            credentialsFile.close() #Not sure if python would automatically close it, seems like a good idea though
            messagebox.showinfo("Login Permitted.", "Login Permitted.\nProceeding to Main Program.")
            return True

    credentialsFile.close()
    messagebox.showwarning("Invalid Cridentials","Sorry, supplied Username and Password\ndo not match reccords. \n\nTry again")
    return False
    #return true if its good and false if EOF error (iterate over everything)
    