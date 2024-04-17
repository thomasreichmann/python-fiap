from main import ex5


def test_should_order():
    assert ex5(1, 2, 3) == "123"


def test_should_order_2():
    assert ex5(100, 300, 90) == "90100300"


def test_should_order_3():
    assert ex5(10, 789, 200) == "10200789"


# Testes extra criados pelo GPT-4
def test_should_order_with_zero():
    # Test including zero, which could affect string ordering especially if it comes first or last
    assert ex5(0, 50, 5) == "0550"


def test_should_handle_duplicates():
    # Test with two numbers being the same to ensure duplicates are handled correctly
    assert ex5(33, 33, 100) == "3333100"


def test_should_order_large_numbers():
    # Test with very large numbers to ensure there's no issue handling them
    assert ex5(999999999, 88888888, 7777777) == "777777788888888999999999"
