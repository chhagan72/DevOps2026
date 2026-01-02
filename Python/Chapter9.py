# 📘 Chapter 9: Functions

# Creating functions

# Arguments & return

# Default arguments

# Reusable automation logic

# Functions let you reuse automation logic, avoid repetition, and keep scripts clean, readable, and scalable—very important in DevOps.

# Creating Functions (Basics)
# def Function_name():
#     print("This is Devops with python chapter 9.")
# Function_name()

# Functions with Arguments
# Arguments allow passing data into a function.

# def deploy_app(server):
#     print(f"Application Deploying on the {server}")
# deploy_app("Web-01")
# deploy_app("Web-02")

# Multiple Arguments

# def restart_Services(server, service):
#     print(f"Restarting {service} on {server}")
# restart_Services("Web-01", "Nginix")

# def check_disk(usage):
#     if usage > 85:
#         return "ALERT"
#     else:
#         return "OK"
# status = check_disk(86)
# print(status)

# Default Arguments
# Used when most values are common.

# def deploy(server, env="dev"):
#     print(f"Deploying to {server} on {env} environment")
# deploy("Web-01")
# deploy("Web-02", "Production")

# Reusable Automation Logic (Real DevOps)
# def service_status(service, status):
#     if status == "running":
#         return f"{service} is UP ✅"
#     else:
#         return f"{service} is DOWN ❌"

# print(service_status("nginx", "running"))


# Keyword Arguments
# deploy(env="production", server="web3")

# services = {
#     "Nginix":"runniong",
#     'Docker':"Failed",
#     "Jenkins":"Stoped"
# }
# def check_status(services):
#     for service, status in services.items():
#         print(service_status(service, status))
# check_status(services)


# Function + YAML Config

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

# def get_environment(config):
#     return config.get("app", {}).get("environment", "dev")
# env = get_environment(config)
# print(env)


# Function for Log Monitoring

# def find_error(log_file):
#     with open(log_file) as file:
#         for line in file:
#             if "ERROR" in line:
#                 print(line.strip())
# find_error("app.log")

# Error Handling (try/except)
# ✔️ Logging (logging module)
# ✔️ Monitoring script
# ✔️ Real production-ready automation