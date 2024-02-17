from Model.ParsedModel.IMetaSource import SourceType

class MainInstrumentSource:
    def __init__(self, id):
        self._id = id
    
    @property
    def source_type(self):
        return SourceType.MainInstrument

    @property
    def id(self):
        return self._id
