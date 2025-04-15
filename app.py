class Figure:
    def __init__(self, type, sides):
        self.type = type
        self.sides = sides

    def get_angles(self):
        if self.type == "трикутник":
            return 3
        if self.type == "квадрат":
            return 4
        return 0


class Name:
    def __init__(self, name, hobby):
        if not hobby:
            raise ValueError("Хоббі не може бути порожнім")
        self.name = name
        self.hobby = hobby



if __name__ == "__main__":
    b = Name("Влад", "")