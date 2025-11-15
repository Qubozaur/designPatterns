class WeatherStation:
    def __init__(self):
        self._observers = []
        self._temperature = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._temperature)

    def set_temperature(self, new_temp):
        print(f"[WeatherStation] New temperature: {new_temp}°C")
        self._temperature = new_temp
        self.notify()
