# Chapter 4: Strings (Important for DevOps)

# String methods (upper, lower, split, replace)

# String formatting (f-strings)

# Slicing

# # Handling logs & file content

# upper() / lower()

# Name = "Chhagan ram Ramesh Kumawat"
# print(Name.upper())
# print(Name.lower())


# split()
# parts = Name.split(" ")
# print(parts)


# replace()
# print(Name.replace("Chhagan ram", "Durgesh"))


# test = " Nginix Running "
# print(test.strip())
# print(test.startswith("Nginix"))
# print(test.endswith("Running"))


# String Formatting (f-strings) ⭐ BEST PRACTICE

# server="Web01"
# status = "Running"
# cpu = 74.09
# print(f"Server {server} is {status} (CPU={cpu}%)")


# String Slicing

# log = "2025-09-10 10:45:30 ERROR nginx failed"
# print(log[0:10])
# print(log[11:19])
# print(log[-6:])
# print(log[::-1])

# with open(r"c:\Users\user\Desktop\Chhagan\DevOps2026\Python\test.log", "r") as file:
#     for line in file:
#         if "ERROR" in line:
#             print(line.strip())

# log = "ERROR 500 /api/login"

# level, code, path = log.split(" ")
# print(f"Level={level}, Code={code}, Path={path}")

# log = "User password=secret123"
# safe_log = log.replace("secret123", "******")
# print(safe_log)

# count = 0
# with open(r"c:\Users\user\Desktop\Chhagan\DevOps2026\Python\test.log", "r") as file:
#     for line in file:
#         if "ERROR" in line.upper():
#             count += 1
# print(f"Total Error : {count}")