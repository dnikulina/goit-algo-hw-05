import re
from typing import Callable

def generator_numbers(text):
    pattern = r"\d+\.\d+"
    pattern_result = re.findall(pattern, text)
    for digit in pattern_result:
        yield float(digit)

def sum_profit(text: str, func: Callable):
    total = 0
    for profit in func(text):
         total += profit
    return total

