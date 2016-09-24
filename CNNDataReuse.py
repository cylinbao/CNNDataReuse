import math

F_size = int(input("Enter Filter size:"))
F_num = int(input("Enter Filter number:"))
I_size = int(input("Enter Image size:"))

F_reuse = pow((I_size - F_size + 1), 2)
I_reuse = pow(F_size, 2)*F_num

print("Average Reuse of Filter is: ", F_reuse)
print("Average Reuse of Image is: ", I_reuse)
