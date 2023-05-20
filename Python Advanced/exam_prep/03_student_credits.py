def students_credits(*args):
    courses = {}
    diyan_result = 0

    for el in args:
        info = el.split("-")
        course_name = info[0]
        course_credits = int(info[1])
        max_result = int(info[2])
        result = int(info[3])

        curr_result = (result/max_result) * course_credits

        courses[course_name] = curr_result
        diyan_result += curr_result

    final_result = ""

    if diyan_result >= 240:
        final_result += f"Diyan gets a diploma with {diyan_result:.1f} credits.\n"
    else:
        final_result += f"Diyan needs {240 - diyan_result:.1f} credits more for a diploma.\n"

    for course in dict(sorted(courses.items(), key=lambda x: -x[1])):
        final_result += f"{course} - {courses[course]:.1f}\n"

    return final_result



print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
