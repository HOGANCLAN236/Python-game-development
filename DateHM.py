# Write a program to accept date as an input from user. Add 16 days to it and display the future date.
#Take two date inputs from user, and show the difference between the dates.

# from datetime import datetime, timedelta

# def getDate():
#     while True:
#         userdate = input("Enter the date (DD-MM-YYYY): ")
#         try:
#             userdatemod = datetime.strptime(userdate, "%d-%m-%Y")
#             return userdatemod
#         except ValueError:
#             print("Invalid Date Format")

# userdatemod = getDate()
# futuredate = userdatemod + timedelta(days= 16)
# future_date_str = futuredate.strftime("%d-%m-%Y") 
# # Print the future date 
# print("Input date:", userdatemod.strftime("%d-%m-%Y")) 
# print("Future date (16 days from input date):", future_date_str)

userdate1 = input("\nEnter a date (DD-MM-YYYY): ")
userdate2 = input("Enter a date (DD-MM-YYYY): ")

#16-08-2011

day1 = (userdate1[0:2])
month1 = (userdate1[3:5])
year1 = (userdate1[6:10])

day2 = (userdate2[0:2])
month2 = (userdate2[3:5])
year2 = (userdate2[6:10])

newday = int(day1) - int(day2)
newmonth = int(month1) - int(month2)
newyear = int(year1) - int(year2)

newdate = str(newday) + "-" + str(newmonth) + "-" + str(newyear)
print(newdate)

# NEXT HM: use loop and random for index and then append to different list and then pick 13 random and add to e.g hearts list 