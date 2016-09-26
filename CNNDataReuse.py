import math

def calIReuse(I_size, F_size):
    I_reuse = 0;
    for y in range(1, I_size):
        y_dis = min(y - 1, I_size - y)
        if (y_dis >= (F_size - 1)) 
            y_reuse = F_size
        else
            y_reuse = y_dis + 1
        for x in range(1, I_size):
            x_dis = min(x - 1, I_size - x)
            if (x_dis >= (F_size - 1))
                x_reuse = F_size
            else
                x_reuse = x_dis + 1
            I_reuse += x_reuse*y_reuse

    return(I_reuse)

F_size = int(input("Enter Filter size:"))
F_num = int(input("Enter Filter number:"))
I_size = int(input("Enter Image size:"))

F_reuse = pow((I_size - F_size + 1), 2)
#I_reuse = pow(F_size, 2)*F_num
I_reuse = calIReuse(I_size, F_size)

print("Average Reuse of Filter is: ", F_reuse)
print("Average Reuse of Image is: ", I_reuse)
