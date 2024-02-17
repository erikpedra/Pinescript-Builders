from Model.ParsedModel.IMetaSource import IMetaSource, SourceType
from Model.ParsedModel.Parameters.IParameter import IParameter
from Model.MetaConditionArgument import MetaFormulaItem
from typing import List


class IndicatorSource(IMetaSource):
    def __init__(self):
        self._source_type = SourceType.Indicator
        self.Id = ""
        # Name of the indicator
        self.Name = ""
        # Source of the indicator
        self.Source = MetaFormulaItem()
        # Parameters
        self.Parameters: List[IParameter] = []
