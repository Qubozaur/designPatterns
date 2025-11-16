from __future__ import annotations
import csv
import json
from typing import Any, Dict
from parser import Parser
import xml.etree.ElementTree as ET

class JSONParser(Parser):
    def parse(self, data: str) -> str:
        items = data.split(",")
        obj = {}
        for item in items:
            key, value = item.split(":",1)
            obj[key] = value

        return json.dumps(obj)


class CSVParser(Parser):
    def parse(self, data: Any) -> Dict:
        reader = csv.reader([data])
        result = {}
        for row in reader:
            for item in row:
                key, value = item.split(":", 1)
                result[key] = value
        return result


class XMLParser(Parser):
    def parse(self, data: Any) -> Dict:
        root = ET.fromstring(data)
        result = {}
        for item in root.findall('item'):
            key = item.get('key')
            value = item.text
            result[key] = value
        return result