from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__drive_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        if variance < multiplication:
            raise Exception("Failed to calculate variance, multiplication is larger")
        formatted_response =  self.__verify_result(variance=variance)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Missing 'numbers' field in request body")
        input_data = body.get("numbers")
        return input_data
    
    def __calculate_variance(self, input_data: List[float]) -> float:
        variance = self.__drive_handler.variance(input_data)
        return variance

    def __calculate_multiplication(self, input_data: List[float]) -> float:
        multiplication = 1
        for num in input_data: multiplication *= num
        return multiplication

    def __verify_result(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "success": True
            }
        }