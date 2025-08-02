strnumber = input("Please enter you number: ")
if strnumber.isdigit() and int(strnumber) > 0:
    intnumber = int(strnumber)

    def isprime(intnumber):
        if intnumber < 2:
            print("any number bellow 2 is not a prime".title())
        elif intnumber == 2:
            print(True)
        elif intnumber % 2 == 0:
            print(False)
        else:
            for i in range(3, int(intnumber ** 0.5) + 1, 2):
                if intnumber % i == 0:
                    print(False)
                    break
            else:
                print(True)

    isprime(intnumber)

else:
    print("please enter a valid natural number".title())
