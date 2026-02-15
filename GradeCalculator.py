#Q: Grade students based on marks, marks>=90, grade= "A"
#   90 > marks >= 80, grade= "B"
#   80 > marks >= 70, grade= "C"
#   70 > marks, grade = "D"

marks= input(" Enter your marks here: ")

if (marks>= "90"):
    grade= "A"
    
elif(marks<"90" and marks>= "80"):
    grade= "B"
    
elif(marks<"80" and marks>= "70"):
    grade= "C"
    
elif(marks<"70" ):
    grade= "D"
    
print("You have got grade = ", grade)
