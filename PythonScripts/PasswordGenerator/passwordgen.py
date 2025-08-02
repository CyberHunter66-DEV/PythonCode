import string
import random
import os

enteredlength = input("Password Length: ")
uselowercase = input("Use Lower Case Letters? y/n: ")
useuppercase = input("Use Upper Case Letters? y/n: ")
usedigits = input("Use Numbers? y/n: ")
usespecialcharacters = input("Use Special Characters? y/n: ")

# checks if the user wants to use lowercase letters
if uselowercase == "y" or uselowercase == "yes" or uselowercase == "Y" or uselowercase == "Yes":
    islowercase = 0
else:
    islowercase = 1

# checks if the user wants to use uppercase letters
if useuppercase == "y" or useuppercase == "yes" or useuppercase == "Y" or useuppercase == "Yes":
    isuppercase = 0
else:
    isuppercase = 1

# checks if the user wants to use numbers
if usedigits == "y" or usedigits == "yes" or usedigits == "Y" or usedigits == "Yes":
    isdigits = 0
else:
    isdigits = 1

# checks if the user wants to use special characters
if usespecialcharacters == "y" or usespecialcharacters == "yes" or usespecialcharacters == "Y" or usespecialcharacters == "Yes":
    ispunctuation = 0
else:
    ispunctuation = 1

# checks if its a valid length and returns error is its not
if enteredlength.isdigit() and int(enteredlength) > 0:
    length = int(enteredlength)

    def passwordgenerator(length, islowercase, isuppercase, isdigits, ispunctuation):
        validcharacters = []  # creates a list to store characters for generation
        password = ""  # creates a string to store the password

        # if lowercase is 0(yes) it adds lowercase letters to the validcharacters list
        if islowercase == 0:
            for a in string.ascii_lowercase:
                validcharacters.append(a)

        # if uppercase is 0(yes) it adds uppercase letters to the validcharacters list
        if isuppercase == 0:
            for b in string.ascii_uppercase:
                validcharacters.append(b)

        # if to use numbers is 0(yes) it adds numbers to the validcharacters list
        if isdigits == 0:
            for c in string.digits:
                validcharacters.append(c)

        # if specialletters is 0(yes) it adds special characters to the validcharacters list
        if ispunctuation == 0:
            for d in string.punctuation:
                validcharacters.append(d)

        # checks if user entered(yes) to one of choices otherwise it returns an error
        if len(validcharacters) > 0:
            while len(password) < length:
                for i in random.choice(validcharacters):
                    password = password + i

        else:
            print("please enter valid options for generation".title())

        if len(password) > 0:  # if password is longer than 0 it prints it (pretty useless comparison)
            print(f"Heres Your Password: {password}")

        # asks user if to save file or not
        savefile = input("Save File To Desktop? y/n: ")

        # if user entered one of those values it saves the file
        if savefile == "y" or savefile == "yes" or savefile == "Y" or savefile == "Yes":
            issavefile = 0
        else:
            issavefile = 1

        if issavefile == 0:  # if savefile is 0(yes)
            filename = ""  # creates a string to store the entered filename to create the path
            username = os.getlogin()  # gets username for the path

            filename = input(
                # asks user to enter file name
                "Enter Filename You Would Like To Save Your Password To: ")
            for driveletter in string.ascii_uppercase:  # finds a valid drive letter
                if os.path.exists(f"{driveletter}:/Users/{username}/Desktop"):
                    # the valid drive letter gets saved to a value to avoid errors
                    validdriveletter = driveletter
                    savingpath = f"{validdriveletter}:/Users/{username}/Desktop/{filename}.txt"
                else:
                    continue
            # if file already exists it asks to overwrite or change name or discard
            if os.path.exists(savingpath):
                overwriteconfirmation = input(
                    "File Already Exists, Enter 1 to Overwrite, 2 To Change Filename, Or Anything To Discard: ")
                if overwriteconfirmation == "1":  # overwrites file if 1 is entered
                    with open(savingpath, "w") as passwordfile:
                        passwordfile.write(password)
                        print(f"Password Overwritten to {savingpath}")
                elif overwriteconfirmation == "2":  # asks for a new file name to write file
                    nfilename = input("New Filename: ")
                    nsavingpath = f"{validdriveletter}:/Users/{username}/Desktop/{nfilename}.txt"
                    # if you try to enter same name again it will ask you again
                    if os.path.exists(nsavingpath):
                        nnfilename = input(
                            "if you use the same filename again it will be overwritten: ".title())
                        nnsavingpath = f"{validdriveletter}:/Users/{username}/Desktop/{nnfilename}.txt"
                        # if you still enter same name AGAIN it will force overwrite
                        with open(nnsavingpath, "w") as passwordfile:
                            passwordfile.write(password)
                            print(f"Password Written to {nnsavingpath}")
                    else:  # if you entered a valid new name that doesnt exist it will create a new file
                        with open(nsavingpath, "x") as passwordfile:
                            passwordfile.write(password)
                            print(f"Password Saved to {nsavingpath}")

                else:  # if you choose 3rd option it will discard the password
                    print("discarding password...".title())
            else:  # if you enter a valid filename that doesnt exist it will just make it
                with open(savingpath, "x") as passwordfile:
                    passwordfile.write(password)
                    print(f"Password Saved to {savingpath}")

    passwordgenerator(length, islowercase, isuppercase,
                      isdigits, ispunctuation)  # calls the password generator func
else:
    # error printed if enteredlength is not valid
    print("Please enter a valid length".title())
