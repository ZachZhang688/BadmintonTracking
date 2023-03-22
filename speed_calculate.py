import math

# 打开输入文件
with open('coordinates.txt', 'r') as input_file:
    # 打开输出文件
    #with open('output_speed_in_pixel.txt', 'w') as output_file:
    with open('output_speed_by_physical.txt', 'w') as output_file:
        # 遍历输入文件的每一行
        for line in input_file:
            # 将每一行按空格分割为两个数字字符串
            x_str, y_str = line.strip().split()
            # 将数字字符串转换为浮点数
            x, y = float(x_str), float(y_str)
            # 计算二维几何距离
            distance = 0.01*math.sqrt(x ** 2 + y ** 2)
            # 将距离写入输出文件
            #output_file.write(str(distance) + '\n') # by pixel
            output_file.write(str(4000*distance*0.25/401) + '\n')  # by physical

