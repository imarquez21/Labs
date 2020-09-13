import getpass

allowed_chars = ['-','_','#','$']
from datetime import datetime

users = []

test_user = {
    'birthdate': "12/12/1987",
    'username': "test_user9",
    'email': "email@test.com",
    'password': "Cisco123"
        }

new_user = {
    'birthdate': "",
    'username': "",
    'email': "",
    'password': ""
        }

def validateDate(birth_date):

    isValid = True
    try:
        born = datetime.strptime(birth_date, '%d/%m/%Y')
        #print("Your born date is "+str(born))
    except ValueError:
        print("Invalid Date Format, format must be dd/mm/yyyy")
        isValid = False

    return isValid

def computeAge(birth_date):
    date = datetime.strptime(birth_date, "%d/%m/%Y")
    today = date.today()

    user_age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))

    #print("Your age is: "+str(computedAge))

    return user_age

def validateUsername(username):

    usernameValid = False

    isAlphaNumeric = username.isalnum()

    characters_list = list(username)

    if len(username) < 8:
        print("The username must be at least 8 characters long.")
    else:
        if isAlphaNumeric:
            print("You are missing one of the following allowed special characters '-', '_', '#' and '$'")
        else:
            for character in characters_list:
                if not character.isalnum():
                    if character in allowed_chars:
                        hasAllowedSpecial = True
                        usernameValid = True
                        new_user['username'] = username
                    else:
                        print("The character '"+character+"' is not allowed, please enter one of the allowed special characters.")


    return usernameValid

def getUsername():

    usernamePending = True

    while usernamePending:
        print("Please enter username, requirements:")
        print("1) It must contain at least 8 characters")
        print("2) It must have at least one digit")
        print("3) It can only contain the following allowed characters, '-', '_', '#' and '$'")
        username = input("Username: ")
        if username:
            new_username = validateUsername(username)
            if new_username:
                usernamePending = False
        else:
            print("The entry was empty, try again.")


    return username

def getBirthDate():

    pendingBirthDate = True

    while pendingBirthDate:
        birth_date = input("Enter your birthdate, format (dd/mm/yyyy): ")
        if birth_date:
            if validateDate(birth_date):
                age = computeAge(birth_date)
                if 18 < age < 80:
                    new_user['birthdate'] = birth_date
                    pendingBirthDate = False
                else:
                    print("Improper Age to Create an Account.")
                    print("Terminating Script")
                    exit()
            else:
                print("Invalid Birth Date, terminating script.")
                exit()
        else:
            print("The entry was empty, try again.")

    return birth_date

def validatePassword(passphrase1, passphrase2):

    passwordMatch = False

    if passphrase1 != passphrase2:
        print("Passwords must match.")
    else:
        new_user['password'] = passphrase1
        passwordMatch = True


    return passwordMatch

def getPassword():

    passwordPending = True

    while passwordPending:
        print("Please set a Password. Note, no characters will be printed on the screen as you type.")
        passphrase1 = getpass.getpass("Type a password: ")
        if passphrase1:
            passphrase2 = getpass.getpass("Re-Type your Password: ")
            if passphrase2:
                if validatePassword(passphrase1, passphrase2):
                    passwordPending = False
                    new_password = passphrase1
                else:
                    passwordPending = True
            else:
                print("The entry was empty, try again")
        else:
            print("The entry was empty, try again")

    return passphrase1


def emailExist(email):

    isnewEmail = True

    users_dict_empty = not users

    if users_dict_empty:
        isnewEmail = True
    else:
        for user in users:
            if user['email'].lower() == email.lower():
                isnewEmail = False
                break
            else:
                isnewEmail = True

    return isnewEmail


def getemail():

    pendingEmail = True

    while pendingEmail:
        user_email = input("Type in an email address: ")
        if user_email:
            if not emailExist(user_email):
                print("We have an account with that email address already.")
                print("Provide a different email address.")
            else:
                new_email = user_email
                pendingEmail = False
        else:
            print("The entry is empty, try again.")


    return new_email

def initalizeNewUser():

    new_user = {
        'birthdate': "",
        'username': "",
        'email': "",
        'password': ""
    }
    return new_user

def registerUser():

    new_user = initalizeNewUser()

    new_user['birthdate'] = getBirthDate()
    new_user['username'] = getUsername()
    new_user['password'] = getPassword()
    new_user['email'] = getemail()

    users.append(new_user)

    return 0


def registerUsers():

    moreUsers = True

    while moreUsers:
        registerUser()
        anotherUser = input("Would you like to register another User [Y/N]: ")
        if anotherUser.lower() == "y":
            moreUsers = True
        else:
            moreUsers = False
            printUsers()

    return 0

def printUsers():

    print("Printing all Registered Users: \n")

    for user in users:
        for key in user.keys():
            print(key + ": " + user[key])
        print("\n")


    return 0

def main():
    print("Script Start")

    #users.append(test_user)
    #printUsers()
    
    registerUsers()

    print("Script End")
    return 0
if __name__ == '__main__':
    main()