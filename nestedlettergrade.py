def letter_grade(grade):
    if grade>=60:
        if grade>=70:
            if grade>=80:
                if grade>=90:
                    letter="A"
                else:
                    letter="B"
            else:
                letter="C"
        else:
            letter="D"
    else:
        letter="F"
    return letter
num_grade=int(input("Enter your numerical grade: "))
letter=letter_grade(num_grade)
print("Your letter grade is ",letter)
