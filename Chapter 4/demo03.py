scores = {
    "A": {"music": 80, "history": 70, "grammer": 75},
    "B": {"music": 81, "history": 78, "grammer": 83},
    "C": {"music": 85, "history": 81, "grammer": 81},
    "D": {"music": 83, "history": 90, "grammer": 82},
}


course_name = "music"
s = 0
for student in scores:
    d = scores[student][course_name]
    s += d
a = s / len(scores)
print("%s : %s" %(course_name, a))

course_name = "history"
s = 0
for student in scores:
    d = scores[student][course_name]
    s += d
a = s / len(scores)
print("%s : %s" %(course_name, a))

course_name = "grammer"
s = 0
for student in scores:
    d = scores[student][course_name]
    s += d
a = s / len(scores)
print("%s : %s" %(course_name, a))
