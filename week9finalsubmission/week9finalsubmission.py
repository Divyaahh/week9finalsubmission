
def calculate_english_grade(test_1, test_2):
    english_test_result = (test_1 + test_2 )/ 2
    print(english_test_result)
    if english_test_result >= 104 and english_test_result <= 120:
        grade = "A"
    elif english_test_result >= 84 and english_test_result <= 103:
        grade = "B"
    elif english_test_result >= 64 and english_test_result <= 83:
        grade ="C"
    else:
        grade ="F"
    return grade
test_score = float(input("enter the test result:"))
test_score_2 = float(input("enter test result 2"))
final_grade = calculate_english_grade(test_score, test_score_2)

print("final grade:", final_grade)

def calculate_maths_grades(paper_1,paper_2,paper_3):
    maths_test_result = (paper_1 + paper_2 + paper_3) / 3
    print(maths_test_result)
    if maths_test_result >= 78 and maths_test_result <= 100:
        return "A"
    if maths_test_result >= 64 and maths_test_result <= 77:
        return "B"
    if maths_test_result >= 56 and maths_test_result <= 63:
        return"C"
    else:
        return "F"
maths_test_score = float(input("enter the test result:"))
maths_test_score_2 = float (input("enter the 2nd test result:"))
maths_test_score_3 = float(input("enter the 3rd test result:"))
final_grade = calculate_maths_grades(maths_test_score,maths_test_score_2,maths_test_score_3)
print("final grade:", final_grade)
def calculate_science_grades(exam_1,exam_2,exam_3):
    science_test_result = (exam_1 +exam_2 + exam_3)/ 3
    print(science_test_result)
    if science_test_result >= 128 and science_test_result <= 150:
        return "A"
    if science_test_result >= 113 and science_test_result <= 127:
        return "B"
    if science_test_result >= 96 and science_test_result <= 112:
        return"C"
    else:
        return"F"
test_score = float(input("enter the 1st test result:"))
test_score_2 = float(input("enter the 2nd test result:"))
test_score_3 = float(input("enter the 3rd test result:"))
final_grade = calculate_science_grades(test_score,test_score_2,test_score_3)
print("final grade:", final_grade)


