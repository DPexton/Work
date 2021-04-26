def final_grade(homework, assessment, final_exam):
    homework = float(homework / 25) * 100
    assessment = float(assessment / 50) * 100
    final_exam = float(final_exam / 100) * 100

    return ((homework * 0.25) + (assessment * 0.25) + final_exam)/1.75


homework = int(input("Enter homework score please" ))
assessment = int(input("Enter assessment score please" ))
final_exam = int(input("Enter final exam score please"))


print("Final grade is: " + str(final_grade(homework, assessment, final_exam)))