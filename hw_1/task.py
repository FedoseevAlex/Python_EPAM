print('Homework 1.1 Grades')

# Enter number of students
stud_count = ''
while not stud_count.isdecimal():
    stud_count = input('How many students in the course? \n>> ')
stud_count = int(stud_count)

# Enter task number
task_count = ''
while not task_count.isdecimal():
    task_count = input('How many tasks?  \n>> ')
task_count = int(task_count)

# Enter names
print('Type students names')
stud_names = []
for i in range(stud_count):
    name = input('Enter student name ({} left) >> '.format(stud_count - i))
    stud_names.append(name)

# Enter grades
stud_grades = dict() # Keys - student names : values - grade lists
for name in stud_names:
    print('Enter grades for {}'.format(name))
    grades = list()
    k = 0
    while k < task_count:
        grade = input('Task {}: '.format(k+1))
        if not grade.isdecimal():
            print('Entered data is not numeric! Try again.')
            continue
        elif not (0 <= int(grade) <= 10):
            print('Entered value is out of range! Try again.')
            continue
        grades.append(int(grade))
        k += 1
    stud_grades[name] = grades
#print(stud_grades)

# Students rating
rating = dict() # Keys - student names : values - sum of grades
for stud in stud_grades:
    rating[stud] = sum(stud_grades[stud])

print('Top 3 students:')
rating = sorted(rating, reverse=True, key=rating.get)[:3]
for j in rating:
    print('Student {} - {}'.format(j, sum(stud_grades.get(j))))

# Task rating
# Keys - Task number : values - sum of grades
hard_task = dict().fromkeys(range(task_count), 0)
grade_list = []
for grade_list_key in stud_grades:
    for ind in range(task_count):
        hard_task[ind] += stud_grades.get(grade_list_key)[ind]
hard_task = sorted(hard_task, key=hard_task.get)[:3]
print('Top 3 of hardest tasks:')
for hrdtsk in hard_task:
    print('Task {}'.format(hrdtsk+1))
