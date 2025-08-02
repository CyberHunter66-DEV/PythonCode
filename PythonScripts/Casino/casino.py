import os
import random
import time

playerbalance = 2000
# Initial player balance
alreadytookaloan = False
# Boolean value to see if play took a loan
loanvalue = 0
# integer value as the loan
# the loan interest multiplier is in line 514 and how much the player needs to have before playing back the loan on line 525


def slots(amountofmoney):
    symbols = ["🍋", "🍇", "🍒", "💲", "🔔", "🎊", "🤡"]
    global playerbalance

    reward = 0
    if amountofmoney <= 0 or amountofmoney > 100000:
        print("Please enter an amount of money between 1 and 100000")
    if (playerbalance-amountofmoney) < 0:
        print("Insufficient funds")
    if (playerbalance-amountofmoney) >= 0 and 0 < amountofmoney <= 100000:
        newplayerbalance = playerbalance-amountofmoney
        result = ""
        print("Spinning... ")
        time.sleep(0.5)
        number1 = random.randint(1, 5000)
        if 1 <= number1 <= 293:
            result += symbols[5]
        if 294 <= number1 <= 661:
            result += symbols[4]
        if 662 <= number1 <= 1661:
            result += symbols[3]
        if 1662 <= number1 <= 2411:
            result += symbols[2]
        if 2412 <= number1 <= 3911:
            result += symbols[1]
        if 3911 <= number1 <= 5000:
            result += symbols[0]

        number2 = random.randint(1, 5000)
        if 1 <= number2 <= 90:
            result += symbols[6]
        if 90 <= number2 <= 340:
            result += symbols[5]
        if 341 <= number2 <= 700:
            result += symbols[4]
        if 701 <= number2 <= 1661:
            result += symbols[3]
        if 1662 <= number2 <= 2411:
            result += symbols[2]
        if 2412 <= number2 <= 3911:
            result += symbols[1]
        if 3911 <= number2 <= 5000:
            result += symbols[0]

        number3 = random.randint(1, 5000)
        if 1 <= number3 <= 293:
            result += symbols[5]
        if 294 <= number3 <= 661:
            result += symbols[4]
        if 662 <= number3 <= 1661:
            result += symbols[3]
        if 1662 <= number3 <= 2411:
            result += symbols[2]
        if 2412 <= number3 <= 3911:
            result += symbols[1]
        if 3911 <= number3 <= 5000:
            result += symbols[0]
        print(result)
        for a in symbols:
            if a + a == result[0:2] or a+a == result[1:3]:
                if a+a+a != result[0:3]:
                    doublegrapes1 = amountofmoney*1
                    doublelemons0 = amountofmoney*1
                    doublecherrys2 = amountofmoney*2
                    doublemoneys3 = amountofmoney*3
                    doublebells4 = amountofmoney*2
                    doublejackpots5 = amountofmoney*2
                    if a+a == "🎊🎊":
                        reward += doublejackpots5
                    if a+a == "🔔🔔":
                        reward += doublebells4
                    if a+a == "💲💲":
                        reward += doublemoneys3
                    if a+a == "🍒🍒":
                        reward += doublecherrys2
                    if a+a == "🍇🍇":
                        reward += doublegrapes1
                    if a+a == "🍋🍋":
                        reward += doublelemons0
                    print(f"+${reward}")
            if a+a+a == result[0:3]:
                triplegrapss1 = amountofmoney*10
                triplelemonss0 = amountofmoney*25
                triplecherrys2 = amountofmoney*95
                triplemoneyss3 = amountofmoney*68
                triplebellss4 = amountofmoney*800
                triplejackpotss5 = amountofmoney*1500
                if a+a+a == "🎊🎊🎊":
                    reward += triplejackpotss5
                    print("Congratulations, You Won The JACKPOT")
                if a+a+a == "🔔🔔🔔":
                    reward += triplebellss4
                    print("Congratulations, You Won The Half Jackpot")
                if a+a+a == "💲💲💲":
                    reward += triplemoneyss3
                if a+a+a == "🍒🍒🍒":
                    reward += triplecherrys2
                if a+a+a == "🍇🍇🍇":
                    reward += triplegrapss1
                if a+a+a == "🍋🍋🍋":
                    reward += triplelemonss0
                print(f"+${reward}")
        if reward == 0:
            print("Loss")
        playerbalance = newplayerbalance+reward


def roulette(amountofmoney, mode):
    global playerbalance

    reward = 0
    if amountofmoney <= 0 or amountofmoney >= 100000:
        print("Please enter an amount of money between 1 and 100000")
    if (playerbalance-amountofmoney) < 0:
        print("Insufficient funds")
    if mode == 1 and (playerbalance-amountofmoney) >= 0 and 0 < amountofmoney < 100000:
        newplayerbalance = playerbalance-amountofmoney
        evenorodd = input("Bet on EVEN or ODD? :")
        numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "0x001", "0x002"]
        randomchoice = random.choice(numbers)
        chooseneven = 0
        choosenodd = 0
        if evenorodd == "even" or evenorodd == "Even" or evenorodd == "EVEN" or evenorodd == "e":
            chooseneven = 1
        if evenorodd == "odd" or evenorodd == "Odd" or evenorodd == "ODD" or evenorodd == "o":
            choosenodd = 1
        if choosenodd == 1 or chooseneven == 1:
            print("Spinning... ")
            time.sleep(0.5)
            if randomchoice.isdigit() and int(randomchoice) % 2 == 0 and chooseneven == 1:
                print(f"Result: {randomchoice}")
                reward = amountofmoney*2
                print(f"+${reward}")
            elif randomchoice.isdigit() and int(randomchoice) % 2 == 1 and choosenodd == 1:
                print(f"Result: {randomchoice}")
                reward = amountofmoney*2
                print(f"+${reward}")
            else:
                print(f"Result: {randomchoice}")
                print("Loss")
        else:
            print("Please enter a valid choice")
            newplayerbalance += amountofmoney
        playerbalance = newplayerbalance+reward
    if mode == 2 and (playerbalance-amountofmoney) >= 0 and 0 < amountofmoney < 100000:
        newplayerbalance = playerbalance-amountofmoney
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                   "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
        bettedonnum = input("Enter the number from 1 to 26 to bet on: ")
        randomnumber = random.choice(numbers)
        try:
            betnumber = int(bettedonnum)
            print("Spinning the wheel of Luck... ")
            time.sleep(1)
            if 0 < betnumber <= 26:
                if bettedonnum == randomnumber:
                    print(f"The Number Is: {randomnumber}")
                    reward = amountofmoney*25
                    print(f"Congratulations, You Won ${reward}")
                else:
                    print(f"The Number Was: {randomnumber}")
                    print("Loss")
            else:
                print("Please enter a valid number between 1 and 26")
                newplayerbalance += amountofmoney
        except Exception as e:
            print(f"Error {e}, did you enter a valid integer?")
            newplayerbalance += amountofmoney
        playerbalance = newplayerbalance+reward


def plinko(amountofmoney, startposition):
    global playerbalance

    reward = 0
    if amountofmoney <= 0 or amountofmoney > 100000:
        print("Please enter an amount of money between 1 and 100000")
    if (playerbalance-amountofmoney) < 0:
        print("Insufficient funds")
    if (playerbalance-amountofmoney) >= 0 and 0 < amountofmoney <= 100000:
        newplayerbalance = playerbalance-amountofmoney
        if startposition == 1:
            print("Dropping the ball to the left... ")
            time.sleep(0.5)
            total = 0
            for i in range(16):
                numbertoadd = random.randint(1, 2)
                total = total + numbertoadd
            if total > 15:
                print(f"It fell in hole {total-16}")
                n32 = 500
                n31 = 20
                n30 = 5
                n29 = 3
                n28 = 2
                n27 = 0
                n26 = 1
                n25 = 1
                n24 = 1
                n23 = 1
                n22 = 1
                n21 = 0
                n20 = 2
                n19 = 3
                n18 = 5
                n17 = 20
                n16 = 500
                result = eval("n"+str(total))
                reward = amountofmoney*int(result)
                print(f"x{result}")
                if reward > 0:
                    print(f"+${reward}")
                else:
                    print(f"-${amountofmoney}")
        elif startposition == 2:
            print("Dropping the ball to the right... ")
            time.sleep(0.5)
            total = 0
            for i in range(16):
                numbertoadd = random.randint(1, 2)
                total = total + numbertoadd
            if total > 15:
                print(f"It fell in hole {total-16}")
                n32 = 500
                n31 = 20
                n30 = 5
                n29 = 3
                n28 = 2
                n27 = 0
                n26 = 1
                n25 = 1
                n24 = 1
                n23 = 1
                n22 = 1
                n21 = 0
                n20 = 2
                n19 = 3
                n18 = 5
                n17 = 20
                n16 = 500
                result = eval("n"+str(total))
                reward += amountofmoney*int(result)
                print(f"x{result}")
                if reward > 0:
                    print(f"+${reward}")
                else:
                    print(f"-${amountofmoney}")
        playerbalance = newplayerbalance+reward


def greeting():
    print(f"Welcome Player {os.getlogin()}")
    time.sleep(0.5)
    print("In this Casino there is:")
    time.sleep(0.5)
    print("Plinko, Roulette and Slots")
    time.sleep(0.5)
    print("Which you can access by typing the mode name")
    time.sleep(0.5)
    print("Use /help to display a list of commands")
    time.sleep(0.5)
    print("And /explain to explain any mode")
    time.sleep(0.5)
    print("Enjoy your stay here!")
    time.sleep(1)


def listofcommands():
    print("To enter a mode use commands: ")
    print("/plinko , /roulette , /slots")
    print("To display player bank balance use: ")
    print("/bal , /balance")
    print("To exit a mode use: ")
    print("/exit")
    print("To exit the Casino use: ")
    print("/quit")


def checkplayerbal():
    print(f"Player Balance is :{playerbalance}")


# game starts
greeting()
# initiates an interactive shell like the commandline shell
shell = input(">>> ")
while shell != "quit" or shell != "QUIT" or shell != "Quit":
    if shell == "/explain" or shell == "/Explain" or shell == "/EXPLAIN":
        print("Enter mode name to explain and /exit to quit")
        exit = False
        while exit != True:
            explainshell = input(">>> Which mode to explain? :")
            if explainshell == "plinko" or explainshell == "Plinko" or explainshell == "PLINKO":
                print(
                    "its just a regular plinko game that gives a value between 32 and 16")
                print("it doesnt generate a random number between 32 and 16")
                print("it works just like a plinko machine would work without a GUI")
                print(
                    "and it gives a reward depending on which 'hole' the 'ball' will land")
                print("for example: 32 and 16 are jackpots")
                print("and 21 or 27 are the losing holes")
            elif explainshell == "slots" or explainshell == "Slots" or explainshell == "SLOTS":
                print("just a normal slots machine that works like it should")
                print("and theres a jackpot with a one in 5000 chance")
                print("but i dont know if chances are accurate,")
                print("i used chat gpt to calculate the the chances")
                print(
                    "oh and also, i hit the jackpot twice while testing which is funny")
            elif explainshell == "roulette" or explainshell == "Roulette" or explainshell == "ROULETTE":
                print("a roulette game, with 2 modes")
                print("first mode is choosing odd or even, like red or black")
                print("you get double the money if you win")
                print("and second mode is betting on a single number")
                print("its high risk with very big reward")
            elif explainshell == "/exit" or explainshell == "/Exit" or explainshell == "/EXIT":
                exit = True
            else:
                pass
    if shell == "/help" or shell == "/Help" or shell == "/HELP":
        listofcommands()
    if shell == "/bal" or shell == "/balance" or shell == "/Bal" or shell == "/Balance":
        checkplayerbal()
    if shell == "/plinko" or shell == "/Plinko" or shell == "/PLINKO":
        print('Enter "play" to play, or /Exit to quit')
        exit = False
        firstrun = True
        sameamount = 0
        samestartpos = 0
        while exit != True:
            plinkoshell = input("Plinko>>> ")
            if plinkoshell == "/help" or plinkoshell == "/Help" or plinkoshell == "/HELP":
                listofcommands()
            elif plinkoshell == "/bal" or plinkoshell == "/balance" or plinkoshell == "/Bal" or plinkoshell == "/Balance":
                checkplayerbal()
            elif (plinkoshell == "play" or plinkoshell == "Play" or plinkoshell == "PLAY") and firstrun:
                stramountofmoney = input("Amount of money to bet: ")
                strstartposition = input('Drop postion left/right: ')
                startposition = 0
                if strstartposition == "left" or strstartposition == "Left" or strstartposition == "LEFT" or strstartposition == "l":
                    startposition = 1
                if strstartposition == "right" or strstartposition == "Right" or strstartposition == "RIGHT" or strstartposition == "r":
                    startposition = 2
                if stramountofmoney.isdigit() and int(stramountofmoney) > 0 and (startposition == 1 or startposition == 2):
                    amountofmoney = int(stramountofmoney)
                    plinko(amountofmoney, startposition)
                    print(
                        "Enter 1 to bet again with same amount, 'play' to bet again with other amount, or /Exit to quit")
                    firstrun = False
                    sameamount = amountofmoney
                    samestartpos = startposition
                else:
                    print("Please enter a valid amount of money/start position")
            elif (plinkoshell == "play" or plinkoshell == "Play" or plinkoshell == "PLAY" or plinkoshell == "1" or plinkoshell == 1) and firstrun == False:
                if plinkoshell == "1" or plinkoshell == 1:
                    amountofmoney = sameamount
                    startposition = samestartpos
                    plinko(amountofmoney, startposition)
                elif plinkoshell == "play" or plinkoshell == "Play" or plinkoshell == "PLAY":
                    stramountofmoney = input("Amount of money to bet: ")
                    strstartposition = input('Drop postion left/right: ')
                    startposition = 0
                    if strstartposition == "left" or strstartposition == "Left" or strstartposition == "LEFT" or strstartposition == "l":
                        startposition = 1
                    if startposition == "right" or startposition == "Right" or startposition == "RIGHT" or startposition == "r":
                        startposition = 2
                    if stramountofmoney.isdigit() and int(stramountofmoney) > 0 and (startposition == 1 or startposition == 2):
                        amountofmoney = int(stramountofmoney)
                        plinko(amountofmoney, startposition)
                        print(
                            "Enter 1 to bet again with same amount, 'play' to bet again with other amount, or /Exit to quit")

                        sameamount = amountofmoney
                        samestartpos = startposition
                else:
                    print("Please enter a valid amount of money/start position")
            elif plinkoshell == "/exit" or plinkoshell == "/Exit" or plinkoshell == "/EXIT":
                print("Exiting Plinko.....")
                exit = True
            else:
                pass
    if shell == "/slots" or shell == "/Slots" or shell == "/SLOTS":
        print('Enter "play" to play, or /Exit to quit')
        exit = False
        firstrun = True
        sameamount = 0
        while exit != True:
            slotsshell = input("Slots>>> ")
            if slotsshell == "/help" or slotsshell == "/Help" or slotsshell == "/HELP":
                listofcommands()
            elif slotsshell == "/bal" or slotsshell == "/balance" or slotsshell == "/Bal" or slotsshell == "/Balance":
                checkplayerbal()
            elif (slotsshell == "play" or slotsshell == "Play" or slotsshell == "PLAY") and firstrun:
                stramountofmoney = input("Amount of money to bet: ")
                if stramountofmoney.isdigit() and int(stramountofmoney) > 0:
                    amountofmoney = int(stramountofmoney)
                    slots(amountofmoney)
                    print(
                        "Enter 1 to bet again with same amount, 'play' to bet again with other amount, or /Exit to quit")
                    firstrun = False
                    sameamount = amountofmoney
                else:
                    print("Please enter a valid amount of money")
            elif (slotsshell == "play" or slotsshell == "Play" or slotsshell == "PLAY" or slotsshell == "1" or slotsshell == 1) and firstrun == False:
                if slotsshell == "1" or slotsshell == 1:
                    amountofmoney = sameamount
                    slots(amountofmoney)
                if slotsshell == "play" or slotsshell == "Play" or slotsshell == "PLAY":
                    stramountofmoney = input("Amount of money to bet: ")
                    if stramountofmoney.isdigit() and int(stramountofmoney) > 0:
                        amountofmoney = int(stramountofmoney)
                        slots(amountofmoney)
                        print(
                            "Enter 1 to bet again with same amount, 'play' to bet again with other amount, and /Exit to quit")
                        sameamount = amountofmoney
            elif slotsshell == "/exit" or slotsshell == "/Exit" or slotsshell == "/EXIT":
                print("Exiting Slots.....")
                exit = True
            else:
                pass
    if shell == "/roulette" or shell == "/Roulette" or shell == "/ROULETTE":
        print('Enter "play" to play, or /Exit to quit')
        exit = False
        firstrun = True
        sameamount = 0
        samemode = 0
        while exit != True:
            rolshell = input("Roulette>>> ")
            if rolshell == "/help" or rolshell == "/Help" or rolshell == "/HELP":
                listofcommands()
            elif rolshell == "/bal" or rolshell == "/balance" or rolshell == "/Bal" or rolshell == "/Balance":
                checkplayerbal()
            elif (rolshell == "play" or rolshell == "Play" or rolshell == "PLAY") and firstrun:
                strmode = input(
                    "Enter '1' to play first Mode and '2' to play second one: ")
                stramountofmoney = input("Amount of money to bet: ")
                if stramountofmoney.isdigit() and int(stramountofmoney) > 0 and (strmode == "1" or strmode == "2"):
                    mode = int(strmode)
                    amountofmoney = int(stramountofmoney)
                    roulette(amountofmoney, mode)
                    print(
                        "Enter 1 to bet again with same amount, 'play' to bet again with other amount, or /Exit to quit")
                    firstrun = False
                    sameamount = amountofmoney
                    samemode = mode
                else:
                    print("Please enter a valid mode/amount of money")
            elif (rolshell == "play" or rolshell == "Play" or rolshell == "PLAY" or rolshell == "1" or rolshell == 1) and firstrun == False:
                if rolshell == "1" or rolshell == 1:
                    amountofmoney = sameamount
                    mode = samemode
                    roulette(amountofmoney, mode)
                if rolshell == "play" or rolshell == "Play" or rolshell == "PLAY":
                    strmode = input(
                        "Enter '1' to play first Mode and '2' to play second one: ")
                    stramountofmoney = input("Amount of money to bet: ")
                    if stramountofmoney.isdigit() and int(stramountofmoney) > 0 and (strmode == "1" or strmode == "2"):
                        amountofmoney = int(stramountofmoney)
                        mode = int(strmode)
                        roulette(amountofmoney, mode)
                        print(
                            "Enter 1 to bet again with same amount, 'play' to bet again with other amount, and /Exit to quit")
                        sameamount = amountofmoney
                        samemode = mode
                    else:
                        print("Please enter a valid mode/amount of money")
            elif rolshell == "/exit" or rolshell == "/Exit" or rolshell == "/EXIT":
                print("Exiting Roulette.....")
                exit = True
            else:
                pass
    if shell == "/quit" or shell == "/Quit" or shell == "/QUIT":
        if alreadytookaloan == False:
            print("Exiting the Casino....")
            time.sleep(1)
            print("Looking forward to our next visit")
            break
        if alreadytookaloan:
            print("You exited the Casino without paying the loan")
            time.sleep(1)
            print("Now you will be hunted down by debt collectors")
            time.sleep(1)
            print("...")
            break
    if playerbalance == 0 and alreadytookaloan == False:
        print("Oh looks like you have ran out of cash")
        time.sleep(1)
        print("Do not worry, you can take a loan")
        time.sleep(1)
        print("It has a a 2x interest and will be collected automatically")
        time.sleep(1)
        takeloan = input("Would you like to take a loan? y/n: ")
        if takeloan == "y" or takeloan == "yes" or takeloan == "Yes" or takeloan == "YES" or takeloan == "Y":
            while playerbalance == 0:
                strloanamount = input(
                    "Specify loan amount between 100 and 5000: ")
                try:
                    loanamount = int(strloanamount)
                    if 100 <= loanamount <= 5000:
                        playerbalance += loanamount
                        loanvalue = loanamount * 2
                        alreadytookaloan = True
                        print(f"+${loanamount}")
                    else:
                        print("Please enter a valid amount")
                except Exception:
                    print("Please enter a valid amount")
        else:
            print("The Dealer was confused of your choice")
            print("You have been kicked out of the Casino")
            break
    if playerbalance >= (loanvalue * 2):
        if alreadytookaloan == True:
            print("Since you obtained double the loan money")
            time.sleep(1)
            print("it has been collected from your total balance")
            time.sleep(1)
            playerbalance -= loanvalue
            alreadytookaloan = False
            print(f"-${loanvalue}")
            loanvalue = 0
    if playerbalance == 0 and alreadytookaloan:
        print("Oh looks like you have ran out of money")
        time.sleep(1)
        print("And you already took a loan")
        time.sleep(1)
        print("Now you have to pay some way right? 😈")
        time.sleep(1)
        print("...................")
        break
    else:
        shell = input(">>> ")

# end :)
