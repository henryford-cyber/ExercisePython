# 2.	Xây dựng lớp Shape với 2 phương thức trừu tượng
# chuVi
# dienTich
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass
