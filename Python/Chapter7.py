# Chapter 7: Conditional Statements

# if, elif, else

# Nested conditions

# Real DevOps examples

# Service status check

# Disk usage alerts 

# Conditional statements allow your script to make decisions.
# In DevOps, they are used for health checks, alerts, deployments, and automation.

# 1. if, elif, else (Basics)
# ✅ Syntax
# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# cpu_usage  = 65
# if cpu_usage  > 80:
#     print("High level CPU usage")
# elif cpu_usage  > 50 :
#     print("Moderate CPU usage ")
# else:
#     print("Cpu Usage is Normal")

# 🔹 2. Comparison & Logical Operators (Reminder)
# Operator	Meaning
# > < >= <=	Compare numbers
# == !=	Equal / Not equal
# and	Both true
# or	Any true
# not	Reverse condition

# Nested Conditions
# Used when multiple checks depend on each other.

# service = "Nginix"
# status = "Running"

# if service == "Nginix":
#     if status == "Running":
#         print(f"{service} Running is fine")
#     else:
#         print(f"{service} is down")

# 🔹 4. Real DevOps Example – Service Status Check

# status = "Running"
# service = {
#     "Nginix":"Running",
#     "Git":"Stopped",
#     "Docker":"Runnning",
#     "Jenkins":"Failed"
# }

# for services, status in service.items():
#     if status == "Running":
#         print(f"{services} is UP")
#     elif status == "Stopped": 
#         print(f"{services} is Down")
#     elif status == "Failed": 
#         print(f"{services} is Failed")
#     else : 
#         print("Server is not Found.....")


# Disk_usage = 85

# if Disk_usage >= 90 :
#     print("CRITICAL: Disk almost full 🚨")
# elif Disk_usage >=70:
#     print("WARNING: Disk usage high ⚠️")
# else:
#     print("Disk usage normal ✅")

# Disk Check Using System (Linux) 
# import shutil

# total, used, free = shutil.disk_usage("/")
# used_per = (used / total) * 100
# if used_per > 80:
#     import shutil

# total, used, free = shutil.disk_usage("/")

# used_percent = (used / total) * 100

# if used_percent > 80:
#     print(f"Alert! Disk usage is {used_percent:.2f}%")
# else:
#     print(f"Disk OK: {used_percent:.2f}%")

# Conditional with User Input

# env = input("Enter environment (prod/dev): ")

# if env == "prod":
#     print("Production deployment started")
# elif env == "dev":
#     print("Development deployment started")
# else:
#     print("Invalid environment")


# DevOps Automation Example (YAML + Condition)

# import yaml
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(BASE_DIR, "config.yml")

# with open(file_path, "r") as file:
#     config = yaml.safe_load(file)

# if config["app"]["environment"] == "production":
#     print("Enable monitoring & alerts")
# else:
#     print("Monitoring disabled")