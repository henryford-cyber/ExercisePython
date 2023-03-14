# 4.	Tạo main.py để thực thi chương trình:
# a)	Đọc dữ liệu các hình từ tập tin input.txt
# b)	Liệt kê hình có chu vi lớn nhât, diện tích lớn nhất
# c)	Kiểm tra số lượng hình nằm chồng lên nhau nhiều nhất


from ChildClasss import Circle, Rectangle, Triangle
from createData import CreateDataRandom


def main():

    with open('input.txt', 'r') as file:
        lines = file.readlines()
    shapes = []
    for line in lines:
        parts = line.strip().split()
        shape_type = parts[0]
        if shape_type == 'Rectangle':
            length = float(parts[1])
            width = float(parts[2])
            shape = Rectangle(length, width)
            shapes.append(shape)
            print(shapes)
        elif shape_type == 'Circle':
            radius = float(parts[1])
            shape = Circle(radius)
            shapes.append(shape)
            print(shapes)
    for shape in shapes:
        if isinstance(shape, Rectangle):
            print(
                f"Rectangle with length {shape.length} and width {shape.width}:")
        elif isinstance(shape, Circle):
            print(f"Circle with radius {shape.radius}:")
        print(f"Perimeter: {shape.perimeter()}")
        print(f"Area: {shape.area()}")


if __name__ == '__main__':
    main()
