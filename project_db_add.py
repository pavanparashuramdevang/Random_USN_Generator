import insert_usn


student_list=["1-KEERTHANA M P","2-BINDU M K","3-ANKITHA","4-KEERTHANA S","5-DEEPASHREE B M","6-DHANUSHGOWDA C","7-MURULI S","8-NAYANA G K","9-CHETANKUMAR C K","10-BHOOMIKA P","11-PRAGATHI S M","12-MADHU K S","13-PRIYANKA K S","14-SHWETHA C"]

student=insert_usn.StudentDb()

student.insert(student_list)

unavilable=['7-MURULI S','13-PRIYANKA K S']
for i in unavilable:
    student.delete(i)

print(student.retrive(),"\n\n",len(student.retrive()))
student.close()