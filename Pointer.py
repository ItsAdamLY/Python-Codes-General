# This is a comment #

# Each grades' Pointer Distributions : #
A = 4.00
Am = 3.67
Bp = 3.33
B = 3.00
Bm = 2.67
Cp = 2.33
C = 2.00
F = 1.00

to_continue = 'y'

while to_continue == 'Y' or to_continue == 'y':
    total_subjects = int(input("How many subjects : "))
    # Input in Python can be expressed as input("What to display before input")

    subject_no = 1
    Ac = Amc = Bpc = Bc = Bmc = Cpc = Cc = Fc = 0

    while total_subjects < 1:
        print("Error!")
        total_subjects = int(input("How many subjects : "))

    else:
        while subject_no <= total_subjects:
            marks = float(input("Input subject {:}".format(subject_no) + " score:"))

            if 85 <= marks <= 100:  # There IS such thing as <= x <= b in Python
                print("Grade is A : Exceptional")
                Ac = Ac + 1

            elif 75 <= marks <= 84:  # Else if in Python is elif #
                print("Grade is A- : Excellent")
                Amc = Amc + 1

            elif 70 <= marks <= 74:
                print("Grade is B+ : Very Good")
                Bpc = Bpc + 1

            elif 65 <= marks <= 69:
                print("Grade is B : Good")
                Bc = Bc + 1

            elif 60 <= marks <= 64:
                print("Grade is B- : Fairly Good")
                Bmc = Bmc + 1

            elif 55 <= marks <= 59:
                print("Grade is C+ : Satisfactory")
                Cpc = Cpc + 1

            elif 50 <= marks <= 54:
                print("Grade is C : Quite Satisfactory")
                Cc = Cc + 1

            else:
                print("Grade is F : Poor")
                Fc = Fc + 1

            subject_no = subject_no + 1

        pointer = A * Ac + Am * Amc + Bp * Bpc + B * Bc + Bm * Bmc + Cp * Cpc + C * Cc + F * Fc

        print("The sum of grade points is {:.2f}".format(pointer))  # {:.precision}.format(var_name)
        print("Your GPA is {:.2f}".format(pointer / total_subjects))

    to_continue = str(input("Do you want to continue? YES - Y or NO - N :"))

    while to_continue != 'Y' and to_continue != 'y' and to_continue != 'N' and to_continue != 'n':
        print("Error!")
        to_continue = str(input("Do you want to continue? YES - Y or NO - N :"))

    if to_continue == 'Y' or to_continue == 'y':
        continue

    else:
        break
