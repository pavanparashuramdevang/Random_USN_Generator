from colorama import Fore, Back, Style
import insert_usn 
import random
import os

def random_generator(num):
    return random.randint(0,num-1)


def random_usn():
    student=insert_usn.StudentDb()
    usns=student.retrive()
    if usns is None:
        
        print(f"*{20*' '}no more usn exits so I'm  exiting")
        print("*\n*\n*\n*")
        print(f"{70*'#'}")
        student.close()
        exit()

    else:
        rand=random_generator(len(usns))
        usn=usns[rand]
        length=len(usns)
        
        print(f"* {20*' '}The Random Group is :",end=" ")
        print(Fore.RED+f"{usn}",end=" ")
        print(Fore.BLACK+"and team")
        print(f"* {20*' '}remaining {length} studnets ")

        #print("this usn is also removed from the db")
        val=input(f"*{10*' '}enter to continue, absent type no, to delete use del, add student use add : " )
        if val=='':

            student.delete(usn=usn)
            student.close()


        elif val=='del':
            usn=input(f"*{10*' '}enter the usn : ")
            usn=usn.upper()
            student.delete(usn=usn)
            student.close()

        elif val=='add':
            usn=input(f"*{10*' '}enter the usn : ")
            usn=usn.upper()
            usn_list=[usn]
            try:
                student.insert(usn_list)
            except:
                print("usn already exists")
    
        else:
            student.close()

        
while True:
    os.system('clear')
    print(f"{70*'#'}")
    print("*\n*\n*")
    random_usn()
    #input(f"*{20*' '}enter anything to continue : " )
    
    os.system('clear')







