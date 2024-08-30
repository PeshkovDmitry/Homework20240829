class Matrix:
    """Класс, реализующий базовые операции с матрицами"""

    def __init__(self, size_x, size_y=None):
        self.__size_x = size_x
        if size_y is not None:
            self.__size_y = size_y
        else:
            self.__size_y = size_x
        self.__data = []

    def __str__(self):
        res = ""
        for row in self.__data:
            for column in row:
                res += f"{column:^6}"
            res += "\n\r"
        return res

    def __add__(self, other):
        if self.size_x != other.size_x or self.size_y != other.size_y:
            return None
        res = Matrix(self.size_x, self.size_y)
        for y in range(self.size_y):
            res.data.append([self.data[y][x] + other.data[y][x] for x in range(self.size_x)])
        return res

    def __sub__(self, other):
        if self.size_x != other.size_x or self.size_y != other.size_y:
            return None
        res = Matrix(self.size_x, self.size_y)
        for y in range(self.size_y):
            res.data.append([self.data[y][x] - other.data[y][x] for x in range(self.size_x)])
        return res

    def __mul__(self, other):
        if self.size_x != other.size_y:
            return None
        res = Matrix(other.size_x, other.size_y)
        for _ in range(other.size_y):
            res.data.append([0 for x in range(other.size_x)])
        for s_y in range(self.size_y):
            list_1 = self.data[s_y]
            for o_x in range(other.size_x):
                list_2 = [other.data[o_y][o_x] for o_y in range(other.size_y)]
                res.data[s_y][o_x] = sum([list_1[i] * list_2[i] for i in range(len(list_1))])
        return res

    def __invert__(self):
        res = Matrix(self.size_y, self.size_x)
        for y in range(res.size_y):
            res.data.append([self.data[x][y] for x in range(res.size_x)])
        return res

    @property
    def size_x(self):
        return self.__size_x

    @size_x.setter
    def size_x(self, value):
        self.__size_x = value

    @property
    def size_y(self):
        return self.__size_y

    @size_y.setter
    def size_y(self, value):
        self.__size_y = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


if __name__ == "__main__":
    # m_1 = Matrix(2, 3)
    # m_1.data = [[1, 2], [3, 4], [5, 6]]
    # print(m_1)
    # m_2 = Matrix(2, 3)
    # m_2.data = [[7, 8], [9, 10], [11, 12]]
    # print(m_2)
    # print("Сложение")
    # print( m_1 + m_2)
    # print("Вычитание")
    # print(m_2 - m_1)
    # m_3 = Matrix(3, 3)
    # m_3.data = [[3, -1, 2], [4, 2, 0], [-5, 6, 1]]
    # print(m_3)
    # m_4 = Matrix(2, 3)
    # m_4.data = [[8, 1], [7, 2], [2, -3]]
    # print(m_4)
    # print("Умножение")
    # print(m_3 * m_4)
    m_5 = Matrix(2, 3)
    m_5.data = [[0, 3], [1, 4], [2, 5]]
    print(m_5)
    print("Транспонирование")
    print(~m_5)


