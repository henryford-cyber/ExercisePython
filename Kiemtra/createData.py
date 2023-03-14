# Viết chương trình thực hiện các công việc sau:
# 1 Viết hàm sinh ngẫu nhiên dữ liệu cho tập tin input.txt có cấu trúc sau:

# # Rect hinh vuong
# rong dai
# x y
# # Circle hinh tron
# Bankinh
# x y
# # Triangle tam giac
# a b c
# x y
# ……..
# Lưu ý: Trong đó x, y là toạ độ
import random


def CreateDataRandom(file_name, num_shapes):
    shapes = ['Rectangle', 'Circle', 'Triangle']
    with open(file_name, 'w') as f:
        for i in range(num_shapes):
            shape_type = random.choice(shapes)
            f.write(f" {shape_type} ")
            if shape_type == 'Rectangle':
                chieu_dai = random.randint(1, 10)
                chieu_rong = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                f.write(f" {chieu_dai} {chieu_rong} ")
                f.write(f" {x} {y}")
            elif shape_type == 'Circle':
                ban_kinh = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                f.write(f" {ban_kinh} ")
                f.write(f" {x} {y} ")
            else:
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                c = random.randint(1, 10)
                while (a + b <= c) or (a + c <= b) or (b + c <= a):
                    a = random.randint(1, 10)
                    b = random.randint(1, 10)
                    c = random.randint(1, 10)
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                f.write(f" {a} {b} {c} ")
                f.write(f" {x} {y} ")


CreateDataRandom("input.txt", 10)


# cho hien ra du lieu tren terminal
