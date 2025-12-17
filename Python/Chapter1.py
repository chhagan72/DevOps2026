# Chapter 1:Python Basics
"""
What is Python & why for DevOps

Installing Python (Linux / Windows)

Python interpreter & REPL

Running .py files

Comments & indentation

Print & input functions
"""


print("This is the python 3.0.3 version")

#Run Python File with Arguments
"""
import sys
print(sys.argv)

def deploy():
    # Deploy application to server Used in DevOps automation 
    print("Deploying.....")
deploy()

# To check Status is running or not 

status ="Up"
if status == "Up":
    print("Server is Running............")
else:
    print("Server is Down............")


#checking Helth
servers = ["Web1","Web2"]
for server in servers:
    print(server)
    print("Checking Helth")

#Give back up 

def backup(backup=1, cmpbackup = 2):
    if backup ==1 or cmpbackup ==2:
        print("Backup started..............")
        print("Backup Complate..............")
    else:
        print("Backup Failed..............")
backup()

# Python print() & input() Functions (Beginner → DevOps)

name = "Chhagan kumawat"
role = "DevOps Engineer"
print(name, "is a ", role)

# Using Separator (sep)
print("Skills")
print("AWS","Docker","K8s","Jenkins","Ansible","Git","GitHub","Linux","Shell scripting", "Jira","Gurufana", sep=" | ")

skils=["AWS","Docker","K8s","Jenkins","Ansible","Git","GitHub","Linux","Shell scripting", "Jira","Gurufana"]
print(" | ".join(skils))

# Using End (end)

print("Deploying...........",end =" ")
print("Done")

# f-string (Most Used in DevOps ✅)

server="Web"
status = "Running"
print(f"Server {server} is {status}.............")

# Used to take user input from keyboard.

name = input("Enter your name : ")
print(name)
print(type(name))
print(name + " Kumawat")

# Example: DevOps Script
server = input("Enter your server name : ")
port = input("Enter Your server Ports : ")
status = input("Enter your server status : ")

print(f"Your Server {server} port are {port} and {server} is {status}")



# Input Validation (Best Practice)

port = input("Enter Your port : ")

if port.isdigit():
    port=int(port)
    print(f"port is {port}")
else:
    print("Port Number is invalid")


# Forgetting type conversion
x = input("Enter number: ")
print(x + 10)

"""