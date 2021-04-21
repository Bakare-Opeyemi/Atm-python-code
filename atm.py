import datetime
from numpy.random import randint
date = datetime.datetime.now()
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi','passwordMike','passwordLove']
accountNumbers = ['0123456789','7303373210','0970632760']
accountBalances = [500,200,1000]

##Function to generate account number
def generateAccount():
    k =[str(randint(10)) for i in range(10)]
    accountNumber ="".join(k)
    return accountNumber


## Function To register
def register():
    regname = input('Please Enter your name: ')
    regpassword = input('Please Enter your password: ')
    confirmPassword = input('Confirm Password: ')
    while regpassword != confirmPassword:
        print("Passwords don't match!")
        regpassword = input('Please Enter your password: ')
        confirmPassword = input('Confirm Password: ')
    else:
        print('Password Confirmed!')
        accountNo = generateAccount()
        allowedUsers.append(regname)
        allowedPassword.append(regpassword)
        accountNumbers.append(accountNo)
        accountBalances.append(0)
        print('Your zuri bank account number is ', accountNo)
    return regname, regpassword

##Function to Login
def login():
    loginName = input('Please Enter your name: ')
    loginPassword = input('Please Enter your password: ')
    i=0
    while i<3:
        i = i+1
        if loginName in allowedUsers:
            userId = allowedUsers.index(loginName)
            if loginPassword != allowedPassword[userId]:
                print('Incorrect username or password')
                response = int(input('Press 1 to try again or 0 to signUp \nPlease Enter Your Response: '))
                if response==1:
                    loginName = input('Please Enter your name: ')
                    loginPassword = input('Please Enter your password: ')
                elif response == 0:
                    register()
                else:
                     print('Invalid Response! ')
            else:
                print('Login Successful')
        else:
            print('Incorrect username or password!')
            print('Consider signing up')
            loginName, loginPassword = register()
            break
    else:
        print('Maximum of three trials possible! You have been reported to the relevant authorities on suspicions of fraud.')
    return loginName, loginPassword
##Welcome Address
print('Welcome to Zuri Bank')
print('Would you like to login or register?')
login_or_Register_prompt = int(input('Enter 1 to login, 0 to sign up: '))
if login_or_Register_prompt ==1:
    name, password = login()
elif login_or_Register_prompt == 0:
    name, password = register()
else:
    print('Invalid response')
    name = ''
    password = ''

if(name in allowedUsers):
    userId = allowedUsers.index(name)
    if(password== allowedPassword[userId]):
        # Let verified user see current date and time and access services
        print('Date: ',date.date())
        print('Time: ', date.time())
        print('Welcome ' + str(name))
        print('These are the available options: ')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. Airtime Top up')
        print('5. View Account Number')
        print('6. Check Account Balance')

        selectedOption = int(input('Please select an option: '))

        if(selectedOption == 1):
            #Withdraw and update account Balance if withdrawal amount is less than or equal to account balance
            withdrawal = int(input('How much would you like to withdraw? \n'))
            if withdrawal <= accountBalances[userId]:
                print('Take your cash')
                accountBalances[userId] -= withdrawal
            else:
                print('Insufficient funds! Please deposit some funds')
        elif(selectedOption == 2):
            #Deposit and update account balance
            deposit = int(input('How much would you like to deposit? \n'))
            accountBalances[userId] += deposit
            print('Curent Balance: ', deposit)

        elif(selectedOption == 3):
            #complaint resolution
            complain = input('What issue will you like to report? \n')
            print('Thank you for contacting us')

        elif(selectedOption == 4):
            #Airtime top Up if top up amount is less than or equal to account balance
            network = int(input('Please select your network provider.\n Enter 1 for MTN \n 2 for airtel \n 3 for Etisalat \n 4 for Glo \n Your response: '))
            response = input('Enter your mobile number: ')
            topUp = int(input('Enter the amount of airtime you would like to purchase: '))
            if topUp <= accountBalances[userId]:
                print('Your airtime top Up was successful')
                accountBalances[userId] -= topUp
            else:
                print('Insufficient funds! Please deposit some funds')

        elif(selectedOption == 5):
            #View account Number if correct password is given
            passw = input('Enter your password to view account number: ')
            if passw == allowedPassword[userId]:
                print('Your account Number is ', accountNumbers[userId])
            else:
                print('Incorrect Password! Please try again')

        elif(selectedOption == 6):
            #view aaccount balance if correct password is given
            passw = input('Enter your password to view your account Balance: ')
            if passw == allowedPassword[userId]:
                print('Your balance is ', accountBalances[userId])
            else:
                print('Incorrect Password!')

        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, please try again')
        
