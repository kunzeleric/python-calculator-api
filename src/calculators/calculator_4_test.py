from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def average(self, numbers: List[float]) -> float:
        return 3 # returns a random number
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3 # returns a random number
    def variance(self, numbers: List[float]) -> float:
        return 1568.16 # returns a random number


class MockDriverHandlerError(DriverHandlerInterface):
    def average(self, numbers: List[float]) -> float:
        return 3 # returns a random number
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3 # returns a random number
    def variance(self, numbers: List[float]) -> float:
        return 1568.16 # returns a random number

def test_calculate_with_body_format_error():
    mock_request = MockRequest({"numberss": [1, 2, 3, 4, 5]})

    driver = MockDriverHandlerError()
    calculator4 = Calculator4(driver)
    
    with raises(Exception) as excinfo:
        calculator4.calculate(mock_request)

    assert str(excinfo.value) == "Missing 'numbers' field in request body"

def test_calculate():
    mock_request = MockRequest({"numbers": [2, 5, 9, 10]})

    driver = MockDriverHandler()
    calculator4 = Calculator4(driver)
    response = calculator4.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 4, 'value': 3, 'success': True}}