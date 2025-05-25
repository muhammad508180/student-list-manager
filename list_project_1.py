# Creat a program that manage a list of student names. 
# Implement functionalities to 
# Add a new student
# Remove a student by name
# Display students in alphabetical order
# Count the total number of students
                 # index = 0        1        2
stud_names : list[str] = ["Saad" , "Ali" , "Tariq"]  # list of student names
            # neg_index = -3       -2       -1     
print(stud_names)
stud_names.insert(3,"Salman")    # add a new student
print(stud_names)
stud_names.remove("Tariq")     # remove a student by name
print(stud_names)
stud_names.sort()              # sort students in alphabetical order
print(stud_names)
total = len(stud_names)         # count the total number of students
print("total number of students are:" , total)
