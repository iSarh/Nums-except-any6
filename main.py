num = int(input("Enter A Number: "))

if num > 0 :

    # List For The Number That Will Be Printed
    numbersList = []

    for i in reversed(range(1,num)):

        # Any Number Containing The Digit 6, Dnt Print It
        if i % 10 == 6:
            continue

         #Add The Number Into The list
        numbersList.append(i)

        #Print The Numbers
        print(i)

    print(f"\n{len(numbersList)} Numbers Printed Successfully.")

else:
    print(f"Number {num} Is Unacceptable Value.")



