def letter_grade(grade):
    if grade<60:
        letter="F"
    elif grade<=70:
        letter="D"
    elif grade<=80:
        letter="C"
    elif grade<=90:
        letter="B"
    elif grade<=100:
        letter="A"
    return letter
grade=int(input("Enter your grade: "))
letter=letter_grade(grade)
print("Your letter grade is ", letter)
