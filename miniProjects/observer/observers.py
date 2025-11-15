class ConsoleDisplay:
    def update(self, temperature):
        print(f"[ConsoleDisplay] Temperature: {temperature}°C")


class FileLogger:
    def __init__(self, filename="log.txt"):
        self.filename = filename
        open(self.filename, "w").close()

    def update(self, temperature):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(f"Temperature registered: {temperature}°C\n")
        print("[FileLogger] Saved to file.")
