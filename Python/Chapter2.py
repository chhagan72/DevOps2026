"""
Chapter 2: Variables & Data Types

Variables

Data types

int, float

string

boolean

Type casting

type() function

"""

"""
Python Variables (Beginner → DevOps)
🔹 What is a Variable?

A variable is a container to store data in memory.

👉 Python variables are dynamically typed (no need to declare data type).

🔹 Creating Variables
name = "Chhagan"
age = 24
role = "DevOps Engineer"

🔹 Variable Naming Rules

✅ Must start with a letter or _
✅ Can contain letters, numbers, _
❌ Cannot start with a number
❌ No spaces
❌ No Python keywords

✔️ Good Names
server_name = "web01"
cpu_usage = 75

❌ Bad Names
1server = "web01"   # invalid
server-name = "x"   # invalid

🔹 Multiple Assignment
a, b, c = 10, 20, 30


Same value:

x = y = z = 0

🔹 Variable Types (Auto-detected)
name = "AWS"        # str
count = 5           # int
load = 2.5          # float
status = True       # bool


Check type:

print(type(name))

🔹 Reassigning Variables
env = "dev"
env = "prod"   # value changed

🔹 Constants (By Convention)

Python has no real constants.
Use UPPERCASE to indicate constants:

PORT = 8080
MAX_RETRIES = 5

🔹 Using Variables with print()
f-string (Best Practice ✅)
server = "web01"
status = "running"

print(f"Server {server} is {status}")

🔹 Variables in DevOps Scripts
AWS_REGION = "ap-south-1"
INSTANCE_TYPE = "t2.micro"

🔹 User Input → Variable
env = input("Enter environment: ")
print(f"Deploying to {env}")

🔹 Common Mistakes ❌
❌ Using variable before assignment
print(x)   # NameError

❌ Case sensitivity
Name = "AWS"
print(name)  # Error
"""
"""
# Python Data Types (Core Basics for DevOps)

server=1
port = 8080
retrise = 3

print(server + retrise)
print(port * 2)
print(type(server))


cpu_uses = 1.75
load_avg = 1.00

print(cpu_uses + 10.00)



path = "home/Chhagan/Python/Chapter1.py"
print(path)

print(len(path))

print(path.upper())
print(path.lower())

print(path[1])



is_running = "True"
is_Stopt = "False"
is_failed = "False1"

user = input("Type True(For running server) and False (For server is stop and failed ) : ")
if is_running == user :
    print("Server is Runnning...........")
elif is_Stopt == user :
    print("Server is stoped..........")
elif is_failed == user:
    print("Server is Failed.........")
else:
    print("Error...")

    

server = "Web01"
cpu = 70.00
threshold = 65
is_alert = cpu>threshold

print(f" Server : {server}")
print(f"CPU Uses : {cpu}")
print(f"Alert CPU uses is very High : {is_alert}")



# Python Type Casting (Very Important for DevOps)

port = int(input("Enter Your server port : "))
print(port+1)



cpu = 70.00
uses= float(cpu)
print(uses + 12.75)



flag = input("Enter true/false : ").lower()

is_enabled = flag == "true"
print(is_enabled)



cpu = float(input("Enter your cpu uses : "))
threshold  = 70 

if cpu > threshold :
    print("⚠️ CPU Alert")
else:
    print("CPU is Normal")

  

# Python type() Function

x = 10
y = 10.5
z = "DevOps"
flag = True

print(type(x))     # int
print(type(y))     # float
print(type(z))     # str
print(type(flag))  # bool


  """