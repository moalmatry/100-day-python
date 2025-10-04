student_scores = [
    150,
    142,
    185,
    120,
    171,
    184,
    149,
    24,
    59,
    68,
    199,
    78,
    65,
    89,
    86,
    55,
    91,
    64,
    89,
]

# total_exams_scores = sum(student_scores)
# total_exams_scores = 0

# for score in student_scores:
# total_exams_scores += score


# print(total_exams_scores)


# max_exam_score = max(student_scores)
max_exam_score = 0
for score in student_scores:
    if score > max_exam_score:
        max_exam_score = score
print(max_exam_score)
