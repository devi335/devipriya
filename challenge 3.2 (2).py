class student:


  def __init__(self, name, roll_number, cgpa):
     self.name = name
     self.roll_number = roll_number
     self.cgpa = cgpa


def sort_student(student_list):
  # sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list,
                        Key = lambda student:student.cgpa, reverse = True)
  #syntax _ lambda arg:exp
  return sorted_students


#Example usage:
students = [
     student("Stephen”, “A123”, 7.8),
     student("Karthik”, “A124”, 8.9),
     student("Santhosh”, “A125”, 9.1),
     student("Komban”, “A126”, 9.9),
 ]

Sorted_students = sort_student(students)

 # Print the sorted list of students
for students in sorted_students:
  print(“name: {}, Roll Number: {}. CGPA  {}”.format(students.name,
                  students.roll_number,
                      students.cgpa))