from __future__ import annotations
from typing import Any, Dict
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def parse(self, data: Any) -> Dict:
        pass
