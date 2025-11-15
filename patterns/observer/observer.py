from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None

    _observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)


    def buissnes_stuff(self) -> None:
        self._state = 10
        self.notify()

class ConcreteObserver(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state > 0:
            print("Reaction bitch")

if __name__ == "__main__":

    subject = ConcreteSubject()

    observer = ConcreteObserver()

    subject.attach(observer)

    print(subject._state)
    subject.buissnes_stuff()
    print(subject._state)
