# Framework: .NET
# Technology stack: C#

from typing import List
from dataclasses import dataclass
import warnings
from Model.JsonModel.Parameter import StrategyParameter
from Model.JsonModel import FormulaItem
class Side:
    Bid = 1
    Ask = 2

@dataclass
class Source:
    Id: str
    SourceType: str
    Name: str
    IndicatorSourceId: str
    IndicatorSource: FormulaItem
    Timeframe: str
    PriceType: str

    INDICATOR = "indicator"
    INSTRUMENT = "instrument"
    BID = "bid"
    ASK = "ask"

    Parameters: List[StrategyParameter]

    def __init__(self, Id: str, SourceType: str, Name: str, IndicatorSourceId: str, IndicatorSource: FormulaItem, Timeframe: str, PriceType: str, Parameters: List[StrategyParameter]):
        self.Id = Id
        self.SourceType = SourceType
        self.Name = Name
        self.IndicatorSourceId = IndicatorSourceId
        self.IndicatorSource = IndicatorSource
        self.Timeframe = Timeframe
        self.PriceType = PriceType
        self.Parameters = Parameters

    def __setattr__(self, name, value):
        if name == 'IndicatorSourceId':
            warnings.warn("This property is obsolete")
        super().__setattr__(name, value)
