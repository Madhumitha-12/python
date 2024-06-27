class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.avg = sum(marks) / len(marks)

def getdata(n):
    students = []
    for i in range(n):
        name = input("Enter student's name: ")
        marks = list(map(int, input("Enter student's marks (separated by space): ").split()))
        students.append(Student(name, marks))
    return students

def print_min_max_avg(students):
    min_avg = min(students, key=lambda x: x.avg)
    max_avg = max(students, key=lambda x: x.avg)
    print("Student with minimum average: ", min_avg.name, "with average: ", min_avg.avg)
    print("Student with maximum average: ", max_avg.name, "with average: ", max_avg.avg)

def print_rankwise(students):
    students.sort(key=lambda x: x.avg, reverse=True)
    for i, student in enumerate(students, 1):
        print("Rank ", i, ": ", student.name, "with average: ", student.avg)

def main():
    n = int(input("Enter the number of students: "))
    students = getdata(n)
    print_min_max_avg(students)
    print_rankwise(students)

if __name__ == "__main__":
    main()
