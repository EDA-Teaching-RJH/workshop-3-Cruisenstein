age = int(input("What's your age? "))
student = str(input("Are you a student? Please answer yes or no. "))

if age < 12 or age >= 65:
    print("£5 please")
elif student == "yes":
    print("£8 please")
else:
    print("£10 please")