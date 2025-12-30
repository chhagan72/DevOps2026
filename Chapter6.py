# Chapter 6: Dictionaries (Very Important)

# Key-value pairs

# Dictionary methods

# Nested dictionaries

# Used in:

# JSON

# API responses

# YAML parsing

# 1 Key–Value Pairs (Dictionary Basics)

# A dictionary stores data as:
# key : value

# server = {
#     "name": "web1",
#     "ip": "10.0.0.1",
#     "status": "running",
#     "port": 80
# }

# print(server)
# print(server["name"])
# print(server.get("name"))

# 2 Dictionary Methods (Most Used)
# ✅ keys()
# print(server.keys())

# values()
# print(server.values())

# for key,value in server.items():
#     print(key, "=>", value)

# server.update({"Status" : "Stoped"})
# print(server)

# server.pop("port")
# print(server)

# print(server.get("env", "not-defined"))

# 3. Nested Dictionaries
# Used in cloud, Kubernetes, API responses

# server = {
#     "web-01":{
#         "ip": "10.0.0.1",
#         "status": "running"
#     },
#     "web-02":{
#         "ip": "10.0.0.2",
#         "status": "stopped"
#     }
# }

# print(server)
# print(server["web-01"]["ip"])

# for server, details in server.items():
#     print(f"{server} - > {details['ip']}({details['status']})")


# 4. Dictionaries in JSON (API Responses)
# import json

# data = '{"name":"web1","ip":"10.0.0.1"}'
# server = json.loads(data)

# # print(server['ip'])

# json_data = json.dumps(server, indent=2)
# print(json_data)


# 5. Dictionaries in API Responses (Real DevOps)

# response ={
#     "status":200,
#     "data":{
#         "instance_id":"i_123",
#         "state":"running",
#         "region":"ap-south-1"
#     }
# }
# print(response)
# print(response["data"]["state"])

# 6. Dictionaries in YAML Parsing

import yaml

with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

print(config["app"]["name"])
print(config["database"]["host"])
print(config["services"])