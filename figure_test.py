class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length


print("квадрат, 1")
f1 = Figure("квадрат", 1)


 # f2 = Figure("трапеція", 12)
 f3 = Figure("квадрат", 0)
