class MetaAction:
    """
    Add meta information for the action
    """

    def __init__(self):
        """
        Initialize MetaAction object.
        """
        self.name = None  # Name of the action
        self.action_id = None  # Id of the action
        self.action_type = None  # Action type
        self.condition = None  # Condition
        self.entry = None  # Entry rate for the trade action
        self.stop = None  # Stop for the trade action
        self.limit = None  # Limit for the trade action
