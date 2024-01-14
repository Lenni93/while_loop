name = input()
grade_class = 0
grades_counter = 0
year_counter = 0
failed_years = 0

while year_counter < 12:
    annual_year = float(input())

    if annual_year < 4:
        failed_years += 1
        if failed_years > 1:
            excluded_year = year_counter + 1
            print(f'{name} has been excluded at {excluded_year} grade')
            break
        continue

    grades_counter += annual_year
    year_counter += 1
else:
    average_grade = grades_counter / year_counter
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
