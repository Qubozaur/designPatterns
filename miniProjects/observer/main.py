from weatherStation import WeatherStation
from observers import ConsoleDisplay, FileLogger
import random

def main():
    station = WeatherStation()

    display = ConsoleDisplay()
    logger = FileLogger()

    station.attach(display)
    station.attach(logger)

    for _ in range(10):
        new_temp = random.randint(-10,20)
        station.set_temperature(new_temp)

if __name__ == "__main__":
    main()