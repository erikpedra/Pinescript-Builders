class ValuesFormatter:
    @staticmethod
    def format_const(val):
        if isinstance(val, int):
            return str(val)
        elif isinstance(val, bool):
            return "true" if val else "false"
        elif isinstance(val, float):
            return f"{val:.4f}"
        elif isinstance(val, str):
            return f'"{val}"'
        else:
            raise ValueError(f"Unsupported type: {type(val)}")
