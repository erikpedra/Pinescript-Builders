from typing import List
from Model.JsonModel.Parameter import StrategyParameter

class Module:
    """
    Strategy module
    """
    def __init__(self):
        """
        Constructor for Module class
        """
        self.Name: str = ""
        self.Parameters: List[StrategyParameter] = []
