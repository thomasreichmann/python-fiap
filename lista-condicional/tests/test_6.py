from main import ex6


def test_should_return_correct_weight_male():
    height = 1.92
    sex = "masculino"

    expected_weight = (62.1 * height) - 44.7

    assert ex6(height, sex) == expected_weight


def test_should_return_correct_weight_female():
    height = 1.56
    sex = "feminino"

    expected_weight = (72.7 * height) - 58

    assert ex6(height, sex) == expected_weight

