from typing import List
from Model.JsonModel import FormulaItem
class Condition:
    """
    Base interface for a condition
    """
    def __init__(self):
        """
        Constructor for Condition class
        """
        self.ConditionType: str = ""
        self.Id: str = ""
        self.UserInput: str = ""
        self.Conditions: List[Condition] = []
        self.Arg1: FormulaItem = None
        self.Arg2: FormulaItem = None

    CROSSES: str = "crosses"
    CROSSES_OVER: str = "crossesOver"
    CROSSES_OVER_OR_TOUCH: str = "crossesOverOrTouch"
    CROSSES_UNDER: str = "crossesUnder"
    CROSSES_UNDER_OR_TOUCH: str = "crossesUnderOrTouch"
    OR: str = "or"
    AND: str = "and"
    GT: str = ">"
    LT: str = "<"
    GTE: str = ">="
    LTE: str = "<="
    EQ: str = "=="
    NEQ: str = "~="
