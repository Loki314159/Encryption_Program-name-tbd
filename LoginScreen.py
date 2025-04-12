#Tkinter will be the framework we will make this project work from
#tk is a nice shorthand for the full word
import tkinter as tk
#In this project, message boxes will be used to communicate with the user
from tkinter import messagebox
#We will need OS for the logo
import os


# ---------------------------------------------------------------#
"""
    Purpose: To create the window and call the mainloop()
    Requirement: This program must have been imported
    Promise: It will return True when a login is successful
"""
# ---------------------------------------------------------------#
def start():
    #loginWindow will be the name of the login page
    #It is set to global so it is universally accessible
    global loginWindow
    #We then call the setupWindow method to construct the login page
    loginWindow = setupWindow()
    #Here I define the window title rather than the default 'tk'
    loginWindow.title("Login")
    #And these lines change the logo to the school's logo.
    #First, we get the local drive where the login screen is hosted
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    #then use the local location and the name of the logo, in this case
    #'School_logo_Lake_G.ico'
    #NOTE: The Logo needs to remain in the SAME FOLDER as the code
    icon_path = os.path.join(BASE_DIR, 'School_logo_Lake_G.ico')
    #Finally, we set the icon as the window's icon.
    loginWindow.iconbitmap(icon_path)
    #Then call the mainloop to give it control over the system
    loginWindow.mainloop()
    #When the screen is destroyed; i.e. a login is successful,
    # the program returns 'True' to the program that called it.
    return True


# ---------------------------------------------------------------#
"""
    Purpose: To construct the window by adding widgets
    Requirement: Being called
    Promise: A Login window looking like that in the documentation will be constructed
            The window will not be able to be closed using the 'X' in the top right
            The password text box will display '*' instead of English characters
            Pressing <Return> in either text box will call the Login function
            Pressing the Login button will call the Login function
"""
# ---------------------------------------------------------------#
def setupWindow():
    #First we create the window
    loginWindow = tk.Tk()
    #The window is sized 250px long, 100 high
    loginWindow.geometry("250x100")
    #When the user presses the close button - top right X on any window,
    #this instead calls the disable_close method, built into this program.
    loginWindow.protocol("WM_DELETE_WINDOW", disable_close)

    #Now we set some configuration for the rows and columns
    #I have defined each column to have 3 rows
    loginWindow.rowconfigure([0, 1, 2], minsize=1)
    #and there are 2 columns
    loginWindow.columnconfigure([0, 1], minsize=1)

    # ------------------------------- #
    # Start adding widgets.
    # ------------------------------- #

    #The first widget has to do with the Username Label and Text Entry
    #first, both are created
    unameLabel = tk.Label(text="Username: ", width=10)
    loginWindow.unameText = tk.Entry(master=loginWindow, width=25)
    #Here the "<Return>" (enter) button is bound to calling the 'login' method
    loginWindow.unameText.bind("<Return>", login)
    #Then these rae placed on the window - spanning the cell east to west (sticky = "ew")
    #There is also some padding around them for user view
    unameLabel.grid(row=0, column=0, sticky="ew", pady=5, padx=1)
    loginWindow.unameText.grid(row=0, column=1, sticky="ew", pady=5, padx=1)

    #Here we do the same for the Password Label and Text Entry
    #Practically the same as above
    pwordLabel = tk.Label(text="Password: ", width=10)
    #One difference here, we hide the password text with show="*"
    loginWindow.pwordText = tk.Entry(master=loginWindow, width=25, show="*")
    loginWindow.pwordText.bind("<Return>", login)
    pwordLabel.grid(row=1, column=0, sticky="ew", pady=5, padx=1)
    loginWindow.pwordText.grid(row=1, column=1, sticky="ew", pady=5, padx=1)

    #Finally create the Button and put it on the bottom row
    enterButton = tk.Button(text="Login", width=15, command=login)
    enterButton.grid(row=2, column=0, columnspan=2)

    #When created, we return this object back to the method that called it so it can be displayed.
    return loginWindow


# ---------------------------------------------------------------#
"""
    Purpose:    To read saved credentials from a file and return them
    Requirement:credentials.txt must contain credentials in the format:
                    username:<<UserName>>
                    password:<<Password>>
    Promise:    To return the 2 values stored beside the ':'
"""
# ---------------------------------------------------------------#

def readCredentials():
    #Create the variables for use in reading the files.
    #This protects against the program crashing if something is wrong with the file
    #These also need to be so excessively complicated that there is no chance that the
    #user would select them as possible, actual choices
    savedUName = "dumyValue...MG^wUR!EHY2HqG1THhTay8^TR8GfacQXqbD6PSH1CuABNZh$vX6Pz%FXhr3e"
    savedPWord = "dumyValue...svPDgYhU4G8W^tLKhBe$F1hM&7Bv&TqW5a%Xf@U@T*%ej1Qkvb6^pX^SKkgZ"

    #Open the file for reading the details in
    credentialsFile = open("credentials.txt", "r")

    #For every line in the file, meaning we treat each line separately
    for line in credentialsFile:
    #We split at the point of the ":"
    #Using maxsplit means, if the user puts a ":" in their password, it is still used.
    #This turns 'line' into a list rather than a string
        line = line.split(":", 1)
    #If the first part of the line is 'username"
        if line[0] == "username":
    #This must correspond to the username so we save the following in that variable.
    #We also are removing any new-line by replacing the new-line char (\n) with nothing
            savedUName = line[1].replace('\n', '')
    #Do the same for the password
        if line[0] == "password":
            savedPWord = line[1].replace('\n', '')

    #Close the credentials file
    credentialsFile.close()

    #and return both values
    return (savedUName, savedPWord)


# ---------------------------------------------------------------#
"""
    Purpose: To display a message box when the user tries to close the window
    Requirement: User clicks the 'x' on the top right of the window
    Promise: An appropriate message box will be displayed to the user
"""
# ---------------------------------------------------------------#

def disable_close():
    #This message box uses the warning type
    #It is to be displayed when the user tries to close the window when they have not logged in.
    messagebox.showwarning("No Closing", "Sorry, you didn't say the magic words... \nTry again")


# ---------------------------------------------------------------#
"""
    Purpose: To command the test if the login details are correct
    Requirement: To be called
    Promise: If the login details are correct, the window closes
"""
# ---------------------------------------------------------------#

def login(event=None):
    if testLogin():
        loginWindow.destroy()


# ---------------------------------------------------------------#
"""
    Purpose: To test the details as user has entered against saved details
    Requirement:    The User has entered some Username and Password
                    There is a username and password saved in a text file
    Promise:    To return True if the saved credentials  match those of the User
                To return False if they are not the same
"""
# ---------------------------------------------------------------#
def testLogin():
    #First, get the Username and Password from the saved file.
    #This is done in another place - the readCredentials() method
    savedUName, savedPWord = readCredentials()

    #Then we get the user entered data from the 2 text boxes
    userUName = loginWindow.unameText.get()
    userPWord = loginWindow.pwordText.get()

    #No we compare the credentials.
    #If they are the same - both user-entered Usernames and Passwords match their
    # saved counterparts, then display an appropriate message box.
    if savedUName == userUName and savedPWord == userPWord:
        messagebox.showinfo("Login Permitted.", "Login Permitted.\nProceeding to Main Program.")
    #In this case, we return True to move forward
        return True
    #If either or both of these credentials are not the same,
    # display an appropriate message box and
    # return False.
    #Note: This is a showwarning box, not a showinfo one like above.
    else:
        messagebox.showwarning("Invalid Cridentials","Sorry, supplied Username and Password\ndo not match reccords. \n\nTry again")
        return False