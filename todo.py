import sys
from datetime import datetime
import os.path
x=str(datetime.utcnow())
x=x.split()
argno = len(sys.argv)
arg =sys.argv
if os.path.isfile('todo.txt'):
    file = open("todo.txt","r")
    content = file.readlines()
    file.close()

if os.path.isfile('done.txt'):
    file = open("done.txt","r")
    temp = file.readlines()
    file.close()

def help():
    s = "Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics"
    sys.stdout.buffer.write(s.encode('utf8'))
def listall():
    file = open("todo.txt","r")
    content = file.readlines()
    file.close()
    count = len(content)
    list=""
    for i in range(count-1,-1,-1):
        list += "[{}] ".format(i+1)+content[i]
    sys.stdout.buffer.write(list.encode('utf8'))

def add(s):
    file = open("todo.txt","a+")
    file.write(s + "\n")
    file.close()

def delete(number):
    content.pop(number-1)
    file = open("todo.txt","w")
    file.writelines(content)
    file.close()

def done(number):
    done1 = content[number-1]
    done1 = "x "+x[0]+" "+done1
    delete(number)
    file = open("done.txt","a+")
    file.write(done1)
    file.close()

def report():
    rep = x[0]+" Pending : "+str(len(content))+" Completed : "+str(len(temp))
    print(rep)

if(argno == 1 or arg[1]=="help"):
    help()

if(argno > 1 and arg[1]=="add"):
    if(argno == 2):
        print("Error: Missing todo string. Nothing added!")
    else:
        for i in range(2,argno,1):
            add(arg[i])
            print("Added todo: \"{}\"".format(arg[i]))

if(argno == 2 and arg[1] == "ls"):
    if os.path.isfile('todo.txt'):
        listall()
    else:
        print("There are no pending todos!")

if(argno >= 2 and arg[1] == "del"):
    if(argno < 3):
        print("Error: Missing NUMBER for deleting todo.")
    elif(len(content)>=int(arg[2]) and int(arg[2])>0):
        delete(int(arg[2]))
        print("Deleted todo #{}".format(arg[2]))
    else:
        print("Error: todo #{} does not exist. Nothing deleted.".format(arg[2]))


if(argno >=2 and arg[1] == "done"):
    if(argno < 3):
        print("Error: Missing NUMBER for marking todo as done.")
    elif(len(content)>=int(arg[2]) and  int(arg[2])>0):
        done(int(arg[2]))
        print("Marked todo #{} as done.".format(arg[2]))
    else:
        print("Error: todo #{} does not exist.".format(arg[2]))


if(argno == 2 and arg[1] == "report"):
    report()
