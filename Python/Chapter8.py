# Chapter 8: Loops

# for loop

# while loop

# break, continue

# Looping files, users, servers

# Loops let you repeat tasks automatically, which is the core of DevOps automation
# (servers, files, logs, services, users, cloud resources).


# Basic Syntax
# for item in sequence:
#     print(item)

# Loop a List (Servers)

# servers = ["Web-01","Web-02","Web-03","Web-04" ]
# for server in servers:
#     print(f"Deploying to {server}")

# Loop with Index

# for i, server in enumerate(servers):
#     print(i, server)

# 2. Looping Dictionaries (Very Important)

# servers = {
#     "Docker": "Running",
#     "Jenkind": "Stopped",
#     "Nginix": "Failed"
# }

# for server, status in servers.items():
#     print(f"{server} -> {status}")


# Loop from YAML (Real DevOps Example)

# import yaml
# import os

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(BASE_DIR, "config.yml")

# with open(file_path, "r") as file:
#     config = yaml.safe_load(file)

# for service in config["services"]:
#     print(f"Checking service {service}")

# Looping Files (Logs / Configs)

# with open("app.log") as file:
#     for line in file:
#         # if "ERROR" in line:
#         #     print(line.strip())

#         if "INFO" in line:
#             print(line.strip())


# Loop Directory Files
# import os

# for file in os.listdir("/var/log"):
#     print(file)


# import os

# for file in os.listdir(r"C:\Users\user\Desktop\Chhagan\DevOps2026\Python"):
#     print(file)

# while Loop (Used for Monitoring)

# count = 1

# while count <= 5:
#     print("Monitoring running.............")
#     count += 1


# break Statement
# Stops the loop immediately.

# services= ["Docker","Jenkins","Nginix","Git"]
# for service in services:
#     if service == "Nginix":
#         break
#     print(service)

# ontinue Statement
# Skips current iteration.

# services= ["Docker","Jenkins","Nginix","Git"]
# for service in services:
#     if service == "Jenkins":
#         continue
#     print(service)

# Looping Users (System Automation)

# users = ["dev", "test", "ops"]

# for user in users:
#     print(f"Creating user :{user}")

# Loop with Condition (Monitoring)
# disk_usages = [45, 72, 88, 93]

# for usage in disk_usages:
#     if usage > 85:
#         print(f"CRITICAL: {usage}%")
#     elif usage > 60:
#         print(f"WARNING : {usage}%")
#     else:
#         print(f"OK : {usage}%")

# Nested Loops (Servers + Services)

# servers = ["Web-01", "Web-02"]
# services = ["Nginix", "Jenkins"]

# for server in servers:
#     for service in services:
#         print(f"Checking service {service} on server {server}")