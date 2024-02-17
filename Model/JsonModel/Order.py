import warnings

class Order:
    def __init__(self):
        self._value = None
        self._value_stack = []
        self._user_input = None

    @property
    def value(self):
        warnings.warn("Obsolete", DeprecationWarning)
        return self._value

    @value.setter
    def value(self, val):
        self._value = val

    @property
    def value_stack(self):
        return self._value_stack

    @value_stack.setter
    def value_stack(self, stack):
        self._value_stack = stack

    @property
    def user_input(self):
        return self._user_input

    @user_input.setter
    def user_input(self, input_val):
        self._user_input = input_val
