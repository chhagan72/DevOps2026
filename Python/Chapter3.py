# 📘 Chapter 3: Operators

# Arithmetic operators (+ - * / %)

# Assignment operators

# Comparison operators

# Logical operators (and, or, not)

# 1. Arithmetic Operators

# Used for mathematical calculations.

# Operator	Meaning	Example
# +	Addition	5 + 2 = 7
# -	Subtraction	5 - 2 = 3
# *	Multiplication	5 * 2 = 10
# /	Division	5 / 2 = 2.5
# %	Modulus (remainder)	5 % 2 = 1
# ✅ Example
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# 🔹 2. Assignment Operators

# Used to assign and update values.

# Operator	Example	Meaning
# =	x = 5	Assign
# +=	x += 2	x = x + 2
# -=	x -= 2	x = x - 2
# *=	x *= 2	x = x * 2
# /=	x /= 2	x = x / 2
# %=	x %= 2	x = x % 2
# ✅ Example
x = 10
x += 5
print(x)   # 15

# 🔹 3. Comparison Operators

# Used to compare two values.
# Result is always True or False.

# Operator	Meaning
# ==	Equal
# # !=	Not equal
# >	Greater than
# <	Less than
# >=	Greater than or equal
# <=	Less than or equal
# ✅ Example
cpu = 75

print(cpu > 70)    # True
print(cpu == 80)   # False

# 🔹 4. Logical Operators

# Used to combine conditions.
# 
# Operator	Meaning
# and	Both conditions True
# or	At least one True
# not	Reverse result
# ✅ and Example
cpu = 75
memory = 60

if cpu > 70 and memory > 50:
    print("High load")

# ✅ or Example
if cpu > 70 or memory > 80:
    print("Alert needed")

# ✅ not Example
service_running = False

if not service_running:
    print("Service stopped")

# 🔹 Real DevOps Example
cpu = float(input("Enter CPU usage: "))
memory = float(input("Enter memory usage: "))

if cpu > 70 and memory > 70:
    print("🚨 Critical Alert")
elif cpu > 70 or memory > 70:
    print("⚠️ Warning")
else:
    print("✅ System Normal")

# ❌ Common Mistakes
# ❌ Using = instead of ==
# if cpu = 70:   # Error


# ✔️ Use:

# if cpu == 70:

# ❌ Comparing string with number
# "80" > 70   # Error


# ✔️ Cast first:

# int("80") > 70