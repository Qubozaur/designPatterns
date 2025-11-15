class Target:
    def request(self) -> str:
        return "Target default behaviour"

class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA"

class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: {self.specific_request()[::-1]}"
    