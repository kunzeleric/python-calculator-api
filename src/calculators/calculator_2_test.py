from typing import Dict
from pytest import raises
from .calculator_2 import Calculator2


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.23, 1.56]})

    calculator2 = Calculator2()
    response = calculator2.calculate(mock_request)
    print()
    print(response)
    assert isinstance(response, dict)
    assert response == {"data": {"Calculator": 2, "result": 0.1}}
