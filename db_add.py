import insert_usn



student_list=[]

for i in range(1,41):
    usn=f"4HG19CS0{i:02d}"
    print(i)
    student_list.append(usn)



lateral_list=[]
for i in range(17):
    usn=f"4HG20CS4{i:02d}"
    print(i)
    lateral_list.append(usn)

print(student_list)
print(lateral_list)



student=insert_usn.StudentDb()

student.insert(student_list)

student.insert(lateral_list)



#deleting some students 

unavilable=['4HG19CS031','4HG19CS039','4HG20CS414']
for i in unavilable:
    student.delete(i)

print(student.retrive(),"\n\n",len(student.retrive()))
student.close()
# student_tp=student.retrive()
# print(student_tp)

# student.delete('4HG19CS028')
# student.retrive()
# student.close()

# print(random_generator(6))