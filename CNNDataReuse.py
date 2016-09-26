from math import *

def calIReuse(I_size, F_size, stride):
    I_reuse = 0;
    for y in range(0, I_size, stride):
        y_dis = min(y - 0, I_size -1 - y)
        if y_dis >= (F_size - 1):
            y_reuse = F_size
        else:
            y_reuse = y_dis + 1
        for x in range(0, I_size, stride):
            x_dis = min(x - 0, I_size -1 - x)
            if x_dis >= (F_size - 1):
                x_reuse = F_size
            else:
                x_reuse = x_dis + 1
            I_reuse += x_reuse*y_reuse
    return(I_reuse)

loop_num = int(input("Enter the total iteration:"))

for i in range(0, loop_num):
    F_size = int(input("Enter Filter size:"))
    F_num = int(input("Enter Filter number:"))
    stride = int(input("Enter the Stride:"))
    I_size = int(input("Enter Image size:"))

    output_size = ceil((I_size - F_size)/stride) + 1
    F_reuse = pow(output_size, 2)
    I_reuse_total = calIReuse(I_size, F_size, stride)
    I_reuse = I_reuse_total * F_num / pow(I_size, 2)

    print()
    #print("Output Size is:", output_size)
    #print("Total Reuse of Image is:", I_reuse_total)
    print("Average Reuse of Filter is:", F_reuse)
    print("Average Reuse of Image is: ", I_reuse)
