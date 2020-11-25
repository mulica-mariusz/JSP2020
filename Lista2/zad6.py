students = ["Kasia", "Basia", "Marek","Darek"]
students.append("Józek")
new_students = ["Ania", "Basia"]
students.extend(new_students)
students.sort()
print(students[3], " ".join(students[:2]), " ".join(students[-2:]))
students.remove("Basia")
students.remove("Basia")
len(students)
tuple(students)
