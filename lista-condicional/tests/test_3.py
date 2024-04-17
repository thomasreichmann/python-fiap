from main import ex3


def test_should_return_true_correct_pass():
    assert ex3('1234') is True


def test_should_return_false_incorrect_pass():
    assert ex3('4321') is False
