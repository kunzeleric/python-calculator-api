from flask import request as FlaskRequest
from typing import Dict

class Calculator1:
    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3
        first_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(first_process_result)
        calc_result = first_process_result+  second_process_result + splited_number
        return self.__format_response(calc_result)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Body must contain 'number' field")

        input_data = body["number"]
        return input_data

    def __first_process(self, first_number: float) -> float:
      first_part = (first_number / 4) + 7
      second_part = (first_part ** 2) * 0.257
      return second_part
    
    def __second_process(self, second_number: float) -> float:
      first_part = (second_number ** 2.121)
      second_part = (first_part / 5) + 1
      return second_part
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
          "data": {
            "Calculator": 1,
            "result": round(calc_result, 2)
          }
        }