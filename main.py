while True:
    y=int(input('Enter the year-\n'))

    if y%400==0:
        print(str(y)+'-is a leap year\n')
        continue
    elif y%100==0:
        print(str(y)+'-is not a leap year\n')
        continue
    elif y%4==0:
        print(str(y)+'-is a leap year\n')
        continue
    else:
        print(str(y)+'-is not a leap year\n')
        continue
