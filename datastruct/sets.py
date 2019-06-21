s1 = set([1, 2, 3, 4, 5])
print(s1)

cs_courses = {"History", "Math", "Science", "Art"}
art_courses = {"History", "Math", "Science", "Design"}

print(cs_courses.union(art_courses))  # To print all the cousers in both the sets.
print(
    cs_courses.difference(art_courses)
)  # To print cousres in cs which are not there in art.

