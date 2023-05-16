scores = {
    "A": {"music": 80, "history": 70, "grammer": 75},
    "B": {"music": 81, "history": 78, "grammer": 83},
    "C": {"music": 85, "history": 81, "grammer": 81},
    "D": {"music": 83, "history": 90, "grammer": 82},
}


def show_course_average(course_name):
    s = 0
    for student in scores:
        d = scores[student][course_name]
        s += d
    a = s / len(scores)
    print("%s : %s" %(course_name, a))


show_course_average("music")
show_course_average("history")
show_course_average("grammer")

def show_course_average(course_name):
    s = 0
    for student in scores:
        d = scores[student][course_name]
        s = s + d
    a = s / len(scores)
    print("%s: %s" %(course_name, a))

show_course_average("music")
