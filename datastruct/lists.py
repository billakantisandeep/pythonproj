courses = ["Historty", "Math", "physics", "compsci"]
# for item in enumerate(courses, start=1):
#     print(item)
course_str = " - ".join(courses)
print(course_str)
new_list = course_str.split(" - ")
print(new_list)
