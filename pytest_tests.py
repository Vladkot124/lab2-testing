from app import Figure

def test_app_triangle():
    fig = "трикутник"
    triangle = Figure(fig, 4)
    assert triangle.type == fig

def test_get_angles():
    triangle = Figure("трикутник", 4)
    assert triangle.get_angles == 3
