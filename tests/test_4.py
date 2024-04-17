from main import ex4


def test_should_add_to_total_at_discount_price():
    quant = 20
    expected_total = quant * 0.25

    assert ex4(quant) == expected_total


def test_should_add_to_total_at_full_price():
    quant = 6
    expected_total = quant * 0.3

    assert ex4(quant) == expected_total

