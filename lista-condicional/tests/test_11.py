from main import ex11


def test_not_a_triangle():
    # Test for sum of angles not equal to 180, should return "Não"
    assert ex11(10, 60, 60) == "Não"


def test_right_triangle():
    # Test for exactly one angle being 90 degrees
    assert ex11(90, 45, 45) == "Retângulo"


def test_obtuse_triangle():
    # Test for at least one angle being greater than 90 degrees
    assert ex11(100, 40, 40) == "Obtuso"


def test_acute_triangle():
    # Test for all angles being less than 90 degrees
    assert ex11(60, 60, 60) == "Agudo"


def test_large_angles():
    # Test for large angles that are valid and form an obtuse triangle
    assert ex11(100, 50, 30) == "Obtuso"
