from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3 # returns a random number
    def variance(self, numbers: List[float]) -> float:
        return 1568.16 # returns a random number

class MockDriverHandlerError(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3 # returns a random number
    def variance(self, numbers: List[float]) -> float:
        return 5 # returns a random number

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})

    driver = MockDriverHandlerError()
    calculator3 = Calculator3(driver)
    
    with raises(Exception) as excinfo:
        calculator3.calculate(mock_request)

    assert str(excinfo.value) == "Failed to calculate variance, multiplication is larger"

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})

    driver = MockDriverHandler()
    calculator3 = Calculator3(driver)
    response = calculator3.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 3, 'value': 1568.16, 'success': True}}