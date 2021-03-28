import datetime

usertime = int(input("What hour is it? (0-23)"))

now = datetime.datetime.now()
print (now.year, now.month, now.day, now.hour, now.minute, now.second)

if usertime <= 5:
    print("What is wrong with you... GO BACK TO SLEEP.")
elif usertime <= 7:
    print("WAKE UP.")
elif usertime <= 9:
    print("GET TO CLASS.")
elif usertime <= 12:
    print("Lunch, baby-bee.")
elif usertime <= 13:
    print("Nap time. UNLESS WE GOT CLASS.")
elif usertime <= 17:
    print("Time to... do some work honestly.")
elif usertime <= 19:
    print("Go get some good eats.")
elif usertime <= 21:
    print("Go to b e d. What's wrong with you?")

else:
    print("You didn’t type a superb value, bretheren. (0-23)")
