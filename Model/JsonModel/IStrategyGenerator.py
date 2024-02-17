class IStrategyGenerator:
    """
    Generates strategy code.
    """

    def Generate(self, model):
        """
        Generates strategy code based on strategy model
        :param model: Strategy model
        :return: Strategy code
        """
        pass

    def GenerateFileName(self, strategyName):
        """
        Generates strategy name based on the strategy name.
        :param strategyName: Strategy name
        :return: File name with the proper extension.
        """
        pass
