from main import ex2


def test_should_false_when_under_16():
    assert ex2(2009) is False


def test_should_true_when_over_16():
    assert ex2(2005) is True


def test_should_true_when_16():
    assert ex2(2008) is True
