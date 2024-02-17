class ConditionType:
    Crosses = 1
    CrossesOver = 2
    CrossesOverOrTouch = 3
    CrossesUnder = 4
    CrossesUnderOrTouch = 5
    Or = 6
    And = 7
    Greater = 8
    Lesser = 9
    GreaterOrEqual = 10
    LesserOrEqual = 11
    Equal = 12
    NotEqual = 13

class ICondition:
    def __init__(self, condition_type):
        self.ConditionType = condition_type
