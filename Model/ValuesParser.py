from typing import List

class ValuesParser:
    @staticmethod
    def get_streams(value: str) -> List[str]:
        return ValuesParser.get_templates(value, '[', ']')

    @staticmethod
    def get_params(value: str) -> List[str]:
        return ValuesParser.get_templates(value, '{', '}')

    @staticmethod
    def get_templates(value: str, start_char: str, end_char: str) -> List[str]:
        streams = []
        index = value.find(start_char)
        while index != -1:
            end_index = value.find(end_char, index)
            streams.append(value[index:end_index + 1])
            value = value[end_index + 1:]
            index = value.find(start_char)
        return streams
