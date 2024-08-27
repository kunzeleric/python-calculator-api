from typing import Dict, List
from pytest import raises
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3 # returns a random number
    def variance(self, numbers: List[float]) -> float:
        return 5 # returns a random number
    def average(self, numbers: List[float]) -> float:
        return 3 # returns a random number

def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.23, 1.56]})

    driver = NumpyHandler()
    calculator2 = Calculator2(driver)
    response = calculator2.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {"data": {"Calculator": 2, "result": 0.1}}

def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.23, 1.56]})

    driver = MockDriverHandler()
    calculator2 = Calculator2(driver)
    response = calculator2.calculate(mock_request)

    assert isinstance(response, dict)
    assert response == {"data": {"Calculator": 2, "result": 0.33}}