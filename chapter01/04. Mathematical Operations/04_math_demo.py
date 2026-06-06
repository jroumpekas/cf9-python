import math
name = "Alice"
age = 20

print("CF9")

print("PI =", math.pi)

print(name + " is " + str(age) + " years old. ")

print("PI = %6.2f"%math.pi)

print("%s is %d years old" %(name, age))

print("Python 3 style using string format")
print("Age is {0:2d}".format(age))
print("PI is {:.3f}".format(math.pi))

print("{1} is {0} years old".format(name, age))