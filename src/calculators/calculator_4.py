from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__drive_handler = driver_handler
    
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        average = self.__calculate_average(input_data)
        formatted_response =  self.__verify_result(average=average)
        return formatted_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Missing 'numbers' field in request body")
        input_data = body.get("numbers")
        return input_data
    
    def __calculate_average(self, input_data: List[float]) -> float:
        average = self.__drive_handler.average(input_data)
        return average

    def __verify_result(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": average,
                "success": True
            }
        }