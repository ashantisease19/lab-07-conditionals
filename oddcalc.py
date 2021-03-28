firstnum = int(input("Give me a number, dude."))
secondnum = int(input("Thanks. Give me another."))
operation = input("Tell me what operation you want, bro.(mul/div/mod)")

if operation == "mul":
    print(firstnum * secondnum)

elif operation == "div":
    print(firstnum / secondnum)

elif operation == "mod":
    print(firstnum % secondnum)

else:
    print("*** invalid operation! ***")
