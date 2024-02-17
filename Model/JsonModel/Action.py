class Action:
    def __init__(self):
        self.Id = None
        self.ActionType = None
        self.Name = None

    BUY = "buy"
    SELL = "sell"
    ENTRY_BUY = "entry_buy"
    ENTRY_SELL = "entry_sell"
    CUSTOM = "*"
    EXIT = "exit"
    EXIT_BUY = "exit_buy"
    EXIT_SELL = "exit_sell"

    Condition = None
    Entry = None
    Stop = None
    Limit = None
