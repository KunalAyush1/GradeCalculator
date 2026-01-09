from grading_engine import assign_grade
from grading_policy import get_relative_grading_policy

policy = get_relative_grading_policy()

mean = 65.89

std_dev = 10.57

test_marks = [74, 62, 82, 84, 76, 71, 65]

for m in test_marks:
    grade, points = assign_grade(m, mean, std_dev, policy)
    print(m, "->", grade)