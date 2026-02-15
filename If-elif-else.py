#Conditional Statements
#if-elif-else

"""age=21

if(age>=18):
    print("Can apply for license")
elif(age<18):
    print("you cannot apply for license")
    """
#Q1- Ask the user about their age and if user's age is more than 18 print "you are eligible to get 
# license, if user age is 18 ask him to enter the month he is born in, if he born in or after may
# print "you are eligible to get license" if he is below may print "you are not eligible to get license"
# if user is below 18 print "you are not eligible to get license"

age= input("what is your age: ")

if (age>"18"):
    print("you are eligible to get license")
elif(age=="18"):
    month= input("what month were you born in: ")
    if(month>="05"):
        print("you are eligible to get license")
    else:
        print("you are not eligible to get license")
else:
    print("you are not eligible to get license")

