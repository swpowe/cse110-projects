# Team Activity - Grade Calculator Program
percent_grade = float(input("What's your grade (in percent): "))
letter_grade = ""

if percent_grade >= 90:
    letter_grade = "A"
elif percent_grade >= 80:
    letter_grade = "B"
elif percent_grade >= 70:
    letter_grade = "C"
elif percent_grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

sign = percent_grade % 10
if sign >= 7:
    if letter_grade != "A":
        if letter_grade != "F":
            letter_grade += "+"
elif sign <= 3:
    if letter_grade != "A":
        if letter_grade != "F":
            letter_grade += "-"
            
print(f"Your letter grade is: {letter_grade}")