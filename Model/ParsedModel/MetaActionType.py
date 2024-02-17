
from enum import Enum

class MetaActionType(Enum):
    Customizable = "Customizable"
    Buy = "Buy"
    Sell = "Sell"
    Exit = "Exit"
    ExitBuy = "Exit Buy"
    ExitSell = "Exit Sell"
    EntryBuy = "Entry Buy"
    EntrySell = "Entry Sell"
