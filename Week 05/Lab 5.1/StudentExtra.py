#This program itirates though a loop for how many records is specified at the beginning of the program in 
#the variable record. User inputs name, module, grade. If any of these variables are empty the program ends with an error

#Author: Audrey Allen


record = int(input("Enter the student records need to add :"))


stud_data={}



while stud_data:
    stud_data.pop(0)

for i in range(0,record):
        Name = input("Enter the student name :").split()
        Module = input("Enter the student module :").split()
        Grade = input("Enter the student grade :").split()
        Nam_key =  Name[0]
        Module_Value = Module[0]
        Grade_value = Grade[0]
        stud_data[Nam_key] = {Module_Value,Grade_value}
        

print (stud_data)



