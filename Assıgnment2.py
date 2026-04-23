class Course:
    def __init__(self, quiz, assignment, midterm, final):
        self.quiz = quiz
        self.assignment = assignment
        self.midterm = midterm
        self.final = final


class Quiz(Course):
    def do_exam(self):
        print("Quiz will be held. Score:", self.quiz)


class Assignment(Course):
    def do_exam(self):
        print("Assignment will be given. Score:", self.assignment)


class Midterm(Course):
    def do_exam(self):
        print("Midterm exam will be held. Score:", self.midterm)


class Final(Course):
    def do_exam(self):
        print("Final exam will be held. Score:", self.final)


quiz_obj = Quiz(10, 15, 20, 30)
assignment_obj = Assignment(10, 15, 20, 30)
midterm_obj = Midterm(10, 15, 20, 30)
final_obj = Final(10, 15, 20, 30)


try:
    number = int(input("Enter number of students: "))

    if number <= 10:
        quiz_obj.do_exam()

    elif number == 20:
        midterm_obj.do_exam()

    elif number == 30:
        final_obj.do_exam()

    else:
        print("No exam scheduled for this number")

except ValueError:
    print("Invalid input. Please enter a number.")