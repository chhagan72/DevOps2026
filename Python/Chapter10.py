# Chapter 10: Modules & Packages

# Importing modules

# Built-in modules (os, sys, time)

# Creating custom modules

# Virtual environments

# Modules & Packages (DevOps-Focused)

# Modules & packages help you organize code, reuse logic, and manage dependencies—critical for real DevOps automation, CI/CD, and production scripts.

# What is a Module?
# A module is simply a Python file (.py) that contains code.

# Example:
# utils.py   ← module

# Importing Modules
# import os 
# print(os.getcwd())


# Import specific items
# from os import listdir
# print(listdir("."))
# print(listdir("./"))

# Import with alias

# import time as t
# t.sleep(2)

# Built-in Modules (Very Important for DevOps)
# 📦 os – OS & Filesystem
# Used for:
# Files
# Directories
# Environment variables

# import os

# print(os.getcwd())
# print(os.listdir("."))
# os.mkdir("Logs")

# sys – System & Arguments
# Used for:
# CLI scripts
# Passing arguments to automation

# import sys

# print(sys.argv)
# print(sys.version)

# 📦 time – Sleep & Timestamps
# Used for:
# Retry logic
# Scheduling
# Rate limiting

# import time

# print(time.time())
# time.sleep(4)

# Creating Custom Modules
# 📁 Project Structure
# DevOps2026/
#  ├── main.py
#  └── utils.py

# ///////////////////////
# utils.py



# def get_environment(config):
#     return config.get("app", {}).get("environment", "dev")
# env = get_environment(config)
# print(env)

# def check_environment(config):
#     return config.get("app", {}).get("environment", "dev")
    

# def great():
#     print("Welcome to DevOps automation")
    
# def check_port(config):
#     return config.get("server", {}).get("port")
    

# ///////////////////////
# main.py
# import utils 
# import yaml
# import os
# from utils import check_environment
# from utils import check_port

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(BASE_DIR, "config.yml")

# with open(file_path, "r") as file:
#     config = yaml.safe_load(file)

# utils.great()
# env = utils.check_environment(config)
# print(env)

# print(check_environment(config))

# print(check_port(config))

# //////////////////////////

# Packages (Folder of Modules)
# A package is a directory containing modules.

# automation/
#  ├── __init__.py
#  ├── deploy.py
#  └── monitor.py

# Import from Package
# from automation.deploy import deploy_app

# __name__ == "__main__" (IMPORTANT)
# Prevents code from running on import.
# ✔️ Required for scripts
# ✔️ Safe imports

# def main():
#     print("Running main logic")

# if __name__ == __name__:
#     main()


# Virtual Environments (VERY IMPORTANT)
# Virtual environments isolate dependencies.

#Windows
# python -m venv venv

# Linux
# python3 -m venv venv

# Activate venv
# Windows
# venv\Scripts\activate

# Linux
# source venv/bin/activate

# Install packages
# pip install pyyaml request

# create txt file
# requirements.txt
# pyyaml
# requests

# Install all:
# pip install -r requirements.txt

# Real DevOps CLI Script Example

# import sys 

# if len(sys.argv) !=2:
#     print("Usage Python Deploy.py <env>")
#     sys.exit(1)
# env = sys.argv[1]
# print(f"Deploying to {env}")