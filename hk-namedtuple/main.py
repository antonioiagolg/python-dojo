from collections import namedtuple
size = int(input())
Student = namedtuple('Student', input().split())
sum_marks = 0
for i in range(size):
    a_student = Student(*input().split())
    sum_marks += int(a_student.MARKS)

print(sum_marks/size)
