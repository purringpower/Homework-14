class Teacher:
    def __init__(self, work_done, subject):
        self.work_done = work_done
        self.subject = subject
        self.student = Student

    def teach(self, student):
        self.work_done += 1
        student.knowledge = self.subject
        return student.knowledge


class Student:
    def __init__(self, teacher):
        self.knowledge = []
        self.teacher = Teacher


teacher1 = Teacher(0, 'python')
student1 = Student(teacher1)
teaching = Teacher.teach(teacher1, student1)
print(teacher1.work_done)
print(student1.knowledge)


