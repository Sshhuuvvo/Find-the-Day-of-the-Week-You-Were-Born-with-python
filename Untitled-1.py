def main():
    DD = 32
    MM = 13
    YYYY = -1
    flag = 0

    month = ["January", "February", "March", "April", "May", "June", "July",
             "August", "September", "October", "November", "December"]

    DD, MM, YYYY = map(int, input("Please enter your birthday in this format (including spaces): DD MM YYYY\n").split())

    if DD == 32 and MM == 13 and YYYY == -1:
        print("Please enter your birthday in this format (including spaces):\nDD MM YYYY\n22 01 1997")
        return

    if DD <= 0:
        if MM <= 0:
            print("We don't have negative or null days and months. Try again!")
            return
        print("We don't have negative or null days. Try again!")
        return

    if MM <= 0:
        print("We don't have negative or null months. Try again!")
        return

    if DD > 31 or MM > 12 or YYYY <= 0:
        if DD > 31 and MM > 12:
            if YYYY <= 0:
                print("We have 12 months, the days of a month are up to 31, and a year should be a positive number. Try again!")
            else:
                print("We have 12 months and the days of a month are up to 31. Try again!")
        elif DD > 31 and MM <= 12:
            if YYYY <= 0:
                print("The days of a month are up to 31 and a year should be a positive number. Try again!")
            else:
                print("The days of a month are up to 31. Try again!")
        elif DD <= 31 and MM > 12:
            if YYYY <= 0:
                print("We have 12 months and a year should be a positive number. Try again!")
            else:
                print("We have 12 months. Try again!")
        elif DD <= 31 and MM <= 12 and YYYY <= 0:
            print("A year should be a positive number. Try again!")
        return

    if MM == 2:
        if YYYY % 400 == 0 or (YYYY % 4 == 0 and YYYY % 100 != 0):
            if DD > 29:
                print(f"The year {YYYY} is a leap year. So, February has up to 29 days. Try again!")
                return
        else:
            if DD > 28:
                print(f"The year {YYYY} isn't a leap year. So, February has up to 28 days. Try again!")
                return

    if MM == 4 and DD > 30:
        print("April has up to 30 days. Try again!")
        return

    if MM == 6 and DD > 30:
        print("June has up to 30 days. Try again!")
        return

    if MM == 9 and DD > 30:
        print("September has up to 30 days. Try again!")
        return

    if MM == 11 and DD > 30:
        print("November has up to 30 days. Try again!")
        return

    if MM <= 2:
        NYYYY = YYYY - 1
        NMM = 0
    else:
        NYYYY = YYYY
        NMM = (4 * MM + 23) // 10

    IDAY = 365 * YYYY + DD + 31 * (MM - 1) - NMM + (NYYYY // 4) - (3 * ((NYYYY // 100) + 1) // 4)
    day = IDAY % 7

    if DD != 11 and DD != 12 and DD != 13:
        flag = DD % 10

    days_of_week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    print("You were born on", days_of_week[day] + ",", end=" ")

    if flag == 1:
        print(f"{DD}st of", end=" ")
    elif flag == 2:
        print(f"{DD}nd of", end=" ")
    elif flag == 3:
        print(f"{DD}rd of", end=" ")
    else:
        print(f"{DD}th of", end=" ")

    print(month[MM - 1], "of", YYYY, "!")

    print("\nAnd if you liked it,")
    print("don't forget to give a (+1) like!")
    print("Thank you!")


if __name__ == "__main__":
    main()
