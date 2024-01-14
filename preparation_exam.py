count_failed_grade = int(input())
average_score = 0
total_grade = 0
all_grade = 0
last_task = " "
has_failed = False
problem_name = input()
while problem_name != 'Enough':
    grade = int(input())
    if grade <= 4:
        all_grade += 1
        # how many are over the all grade or less then 4
        if all_grade == count_failed_grade:
            has_failed = True
            break

    average_score += grade
    # how many are in total and greater then 3 (count failed grade)
    total_grade += 1
    # how many times is of checking total_grade
    last_task = problem_name
    # the last name checked
    problem_name = input()
if has_failed:
    print(f'You need a break, {all_grade} poor grades.')
else:
    diff = average_score / total_grade
    print(f'Average score: {diff:.2f}')
    print(f'Number of problems: {total_grade}')
    print(f'Last problem: {last_task}')
