# # 1. Input entry
# # 2. Name total details student
# # 3. Check pass fail subject : name
# # 4. Total marks student name : marks
 
def student_details(Student):
    print("name:" , Student["name"])
    print("calss:" , Student["class"])
    print("rollnumber:" , Student["rollnumber"])
    print("age:" , Student["age"])
    student_details(Student)
# StUDENT1 = { "name" : "nav"}
# STUDENT2 = {"name" : "ARJUN"}
Student_db_dict = {
} #creating dictionary of student database
# # Student_db_list = [StUDENT1 , STUDENT2]
print(" Hi Welcome to Student Database Please enter your valid options in numeric value between 1 -4  ")
    
while(True):    
    print(  "\n1 Input Student Information\n"
            "2. Retrive Details for Student ( Search by Name) \n"
            "3. print all students info \n"
            )
    
    opt =int(input(" You Choose : "  ))
    
    if opt == 1 :  
    
        name = input( "Enter name of Student :  ")
    
        classs = int(input("Enter Class :  "))
    
        age = int(input("Enter age of Student :  "))
    
        rollnumber = int(input("Enter Roll Number :  "))
        Student = {
        
        "name" : name,
        "class": classs,
        "rollnumber" : rollnumber,
        "age"  : age,
    }
        Student_db_dict[name] = Student
    elif opt == 2 :
        name = input("Enter name of Student :  ")
        student_details(Student_db_dict[name])
    
#     #Search by Name
    
#     #  Student_name = input("Enter Student Name to Find the Student :    ")
    
#     # if Student_name == Student_db["name"]:
    
    
    
#     #     break
    
    
    elif opt == 3 :
#         # Student_db_dict iterate
        for key, value in Student_db_dict.items():
            student_details(value)
# print("Name :" ,{value['name']}," Class :", {value['class']})
        # break
    
    
#     # elif opt == 4 :
#     #     break
# n = int(input("no of values"))
# l=[]
# v = input("list values , seprated")
# l = v.split(',')
# # for i in range(n):
# #     value = input("value")
# #     # l[i] = value
# #     l.append(value)
   
# print(l)
# l.insert(1 ,'d' )
# print(l)
## DICtnary
# n = int(input("no of  values: "))
# d= {}
# for i in range(n):
#     key = input("key: ")
#     value = input("value: ")
#     d[key] = value
# print(d)
        # subjects = str(input("Enter Subject Names (comma-seperated) : ")).split(",")
        # marks = {}
    
        # for subject in subjects :
        #     marks[subject]= int(input(f"Enter Marks for {subject} :  "))


    