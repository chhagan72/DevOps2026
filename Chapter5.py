# Chapter 5: Lists, Tuples, Sets

# Lists (most used)

# List methods (append, remove, pop)

# Tuples

# Sets

# # Use cases in automation

# list
# server = ["Web-o1", "web-02", "web-03","web-4"]
# print(server)

# server.append("db-0")
# print(server)

# server.remove("web-02")
# print(server)

# server.pop()
# print(server)

# server.pop(0)
# print(server)

# server = ["Web-o4", "web-03", "web-01","web-2"]
# server.sort()
# print(server)

# server.reverse()
# print(server)

# for servers in server:
#     print(f"checkimg {servers}")

# for servers in server:
#     print(f"Deploying app on {servers}")

# Tuples

# ports = (8080, 80, 22, 404, 443)
# print(ports)

# print(ports[0])

# Not allowed:
# ports.append(8080)  # Error

# Sets

# envs = {"Dev", "Test", "Prod"}
# print(envs)

# envs.add("Staging")
# print(envs)

# envs.remove("Test")
# print(envs)

# 🔧 Set Operations (VERY Useful)

# linux = {"Docker", "K8s", "Git"}
# cloud = {"AWS", "Docker", "Terraform"}

# print(linux & cloud)   # common
# print(linux | cloud)   # all
# print(linux - cloud)   # difference

# Automation Use Cases (Real DevOps)

# 1. List Use Case – Multiple Servers
# servers = ["web1", "web2", "web3"]

# for server in servers:
#     print(f"Restarting service on {server}")

# Set Use Case – Remove Duplicates
# ips = ["10.0.0.1", "10.0.0.2", "10.0.0.1"]

# unique_ips = set(ips)
# print(unique_ips)

# for server, ip in zip(servers, ips):
#     print(f"My Server {server} ip address is {ip}")

