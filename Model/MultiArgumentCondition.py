from typing import List
from ICondition import ICondition  # Pastikan untuk mengimpor ICondition dengan benar

class MultiArgumentCondition:
    def __init__(self):
        self.ConditionType = None  # Type of the condition
        self.Subconditions: List[ICondition] = []  # List of subconditions
