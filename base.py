import random
from typing import *


class SimEvent[T: SimController]:
    def __init__(self, interval: float) -> None:
        assert interval >= 0, "Negative interval"

        self.due: float
        self.controller: T

        self.interval = interval

    def trigger(self) -> None:
        raise NotImplementedError()


class SimController:
    def __init__(self, initialEvent: SimEvent, stop: float) -> None:
        assert initialEvent.interval == 0, "Non-zero interval for the initial event"
        assert stop > 0, "Non-positive stop time"

        initialEvent.due = 0
        initialEvent.controller = self

        self.futureEvents: List[SimEvent] = [initialEvent]
        self.clock: float = 0

        self.stop = stop

    def dispatchEvent(self, event: SimEvent) -> None:
        event.due = self.clock + event.interval
        event.controller = self

        self.futureEvents.append(event)
        self.futureEvents.sort(key=lambda event: event.due)

    def simulate(self) -> None:
        while self.futureEvents[0].due <= self.stop:
            upcomingEvent = self.futureEvents.pop(0)

            self.clock = upcomingEvent.due

            upcomingEvent.trigger()


class DistributionFunction:
    @staticmethod
    def uniform(min: float, max: float) -> float:
        assert max > min, "max must be greater than min"
        return random.random() * (max - min) + min
