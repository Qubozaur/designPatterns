from parser import Parser
from concrete import JSONParser, CSVParser, XMLParser

class ParserFactory:

    @staticmethod
    def get_parser(_format: str) -> Parser:
        _format = _format.lower()

        if _format == "json":
            return JSONParser()
        elif _format == "csv":
            return CSVParser()
        elif _format == "XML":
            return XMLParser()
        else:
            raise ValueError(f"Unsupported format {_format}")
