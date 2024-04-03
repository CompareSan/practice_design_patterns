# The Observer pattern is useful for state
# monitoring and event handling situations.

from typing import Protocol, List


class Observer(Protocol):
    def update(self) -> None: ...


class Observable(Protocol):
    def add(self, observer: Observer) -> None: ...

    def remove(self, observer: Observer) -> None: ...

    def notify(self) -> None: ...


class WheatherStation:
    def __init__(self, observable: Observable) -> None:
        self.observable = observable

    def update(self):
        print("A change of state has happened")
        self.observable.get_state()


class IoTTemepratureSensor:
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def add(self, observer: Observer) -> None:
        self._observers.append(observer)

    def remove(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update()

    def get_state(self) -> None:
        print("new temperature is 42 degrees")


iot_temperature_sensor = IoTTemepratureSensor()
wheather_station = WheatherStation(iot_temperature_sensor)
iot_temperature_sensor.add(wheather_station)
iot_temperature_sensor.notify()
