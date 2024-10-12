score = float(input("What's the student's grade?"))

if score > 100:
    print("Invaild input")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif 0 >= score < 60:
    print("F")
else:
    print("Invaild Input")
