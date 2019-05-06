courses = ['History', 'Math', 'Physics', 'Compsci']
courses1 = [ 'Economics', 'Language', 'Social']
courses.append('Art')
courses.insert(0, 'Science')
print(courses)
courses.extend(courses1)
print(courses)