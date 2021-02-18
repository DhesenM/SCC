# hw_05_ex_06

def grade_mark(grade):
    '''Return the grade based on the mark'''
    if grade >= 75:
        return "First"
    elif grade >= 70 and grade < 75:
        return "Upper Second"
    elif grade >= 60 and grade < 70:
        return "Second"
    elif grade >= 50 and grade < 60:
        return "Third"
    elif grade >= 45 and grade < 50:
        return "F1 Supp"
    elif grade >= 40 and grade < 45:
        return "F2"
    else:
        return "F3"

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
      49.9, 45, 44.9, 40, 39.9, 2, 0]
print("Grade     Mark")     # Print out the header of the table
print("-----------------")
for i in xs:
    print(i,"      ",grade_mark(i))

##Grade     Mark
##-----------------
##83        First
##75        First
##74.9        Upper Second
##70        Upper Second
##69.9        Second
##65        Second
##60        Second
##59.9        Third
##55        Third
##50        Third
##49.9        F1 Supp
##45        F1 Supp
##44.9        F2
##40        F2
##39.9        F3
##2        F3
##0        F3
##>>> 
