def checkLeapYearOrNot(year):
    if((year%400==0)or((year%100!=0)and(year%4==0))):
        print(f"The Given {year} is a Leap Year")
    else:
        print("The given year is not a leap year")
        

yearInput = int(input("Enter the year"))
checkLeapYearOrNot(yearInput)            