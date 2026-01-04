# Chapter 11: File Handling (Very Important)

# Read files
# Write files
# Append files
# Working with:
# Logs
# Config files
# Reports

# File Handling (Python)
# File handling is very important in DevOps because we work with logs, config files, reports, backups, and automation scripts.

# Opening a File in Python

# file = open("example.txt", "mode")
# Common Modes:
# Mode ->	Meaning
# r ->	Read
# w ->	Write (overwrite)
# a ->	Append
# r+ ->	Read + Write
# w+ ->	Write + Read
# a+ ->	Append + Read

# Reading Files 📖
# 🔹 Read Entire File

# import os

# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, "requirements.txt")

# with open(file_path, "r") as f:
#     print(f.read())


# Debug Tip (Remember this forever)
# Show your current folder
# import os
# print("Current folder", os.getcwd())


# Interview-ready Explanation

# ❓ Why error occurred?
# ✔ Python searches files in current working directory, not where file exists.

# Read Line by Line (Best for logs) 

# import os

# base_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(base_dir, "requirements.txt")

# with open(file_path, "r") as f:
#     # print(f.read())
#     for line in f:
#         print(line.strip())

# Read Only One Line

# import os

# base_dire = os.path.dirname(os.path.abspath(__file__))
# file_path  = os.path.join(base_dire, "test.log")

# with open(file_path, "r") as file:
#     print(file.readline())

# Writing Files ✍️ (Overwrite)
# ⚠️ Existing data will be deleted

# import os

# basedire = os.path.dirname(os.path.abspath(__file__))
# filepath = os.path.join(basedire, "test.log")
# with open(filepath, "w") as file:
#     file.write("\nServer started successfully\n")

# Write Multiple Lines

# import os 

# lines =["ERROR\n","FILE\n", "This is the write file with multiple lines"]
# with open("test.log", "w") as file:
#     file.writelines(lines)

# ppending Files ➕
# Used to add new data without deleting old data (very useful for logs)
# import os 

# with open("test.log", "a") as file :
#     file.write("\nSuccess : New user logged in successfully...\n")

# Working with LOG FILES 🪵 (Very Important for DevOps)
# Example: Reading Error Logs

# import os 
# with open("test.log", "r") as file:
#     for line in file:
#         if "ERROR" in line:
#             print(line)

# Example: Writing Logs
# from datetime import datetime

# with open("test.log", "a") as file:
#     file.write(f"{datetime.now()} ERROR User Application closed succesfully.......\n")

# Working with CONFIG FILES ⚙️
# Example: Simple .conf file

# app.conf
# env=production
# debug=false
# port=8080

# import os 

# config ={}

# with open("app.conf", "r") as file:
#     for line in file:
#         key, value = line.strip().split("=")
#         config[key] = value
# print(config)

# Working with REPORT FILES 📊
# Example: Generate a Report

# users = ["Chhagan", "Rishi", "Vaibhav"]

# with open("report.txt", "w") as file:
#     file.write("User report...\n")
#     file.write("Available users are...\n")
#     for user in users:
#         file.write(user + "\n")

# import os 

# with open("report.txt","r") as file:
#     data = file.read()
#     print(data)

# File Existence Check (DevOps use)
# import os

# if os.path.exists("report.txt"):
#     print("The file is exist......")
# else:
#     print("File is not exist......")


# Real DevOps Use Cases 🚀

# ✔ Read application logs
# ✔ Update configuration files
# ✔ Generate deployment reports
# ✔ Store backup data
# ✔ Automation scripts

# Interview Questions (Important)

# Difference between w and a mode?
# Why is with open() better?
# How do you read large log files?
# How to handle file not found error?