# If the marks obtained by a student in five different subjects are input through the keyboard,
# find out the aggregate marks and percentage marks obtained by the student. Assume that the
# maximum marks that can be obtained by a student in each subject is 100.

subject_1=int(input("Enter The Mark of Subject 1: "))
subject_2=int(input("Enter The Mark of Subject 2: "))
subject_3=int(input("Enter The Mark of Subject 3: "))
subject_4=int(input("Enter The Mark of Subject 4: "))
subject_5=int(input("Enter The Mark of Subject 5: "))
# if(subject_1 <= 100 and subject_2 <=100 and subject_3 <=100 and subject_4 <=100 and subject_5 <=100):
   
# else:
#     print("Invalid marks")
total_marks=subject_1+subject_2+subject_3+subject_4+subject_5
aggregate_marks=total_marks/5;
percentage_marks=(total_marks * 100) /500;
print("Aggregate marks obtained by the student",aggregate_marks)
print("percentage obtained by the student",percentage_marks)