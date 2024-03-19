from typing import *


class SimEvent[T: SimController]:
    def __init__(self, interval: float) -> None:
        assert interval >= 0, "Negative interval"

        self._due: float
        self._controller: T

        self._interval = interval

    @property
    def interval(self) -> float:
        return self._interval

    @property
    def due(self) -> float:
        assert self._due is not None
        return self._due

    @property
    def controller(self) -> T:
        assert self._controller is not None
        return self._controller

    def dispatch(self) -> None:
        raise NotImplementedError()


class SimController:
    def __init__(self, initialEvent: SimEvent, stop: float) -> None:
        assert initialEvent.interval == 0, "Non-zero interval for the initial event"
        assert stop > 0, "Non-positive stop time"

        initialEvent._due = 0
        initialEvent._controller = self

        self._events: List[SimEvent] = [initialEvent]
        self._clock: float = 0
        self._immediateEventIndex: int = 0

        self._stop = stop

    @property
    def pastEvents(self) -> List[SimEvent]:
        return self._events[: self._immediateEventIndex]

    @property
    def futureEvents(self) -> List[SimEvent]:
        return self._events[self._immediateEventIndex :]

    @property
    def clock(self) -> float:
        return self._clock

    @property
    def stop(self) -> float:
        return self._stop

    def enqueueEvent(self, event: SimEvent) -> None:
        event._due = self.clock + event.interval
        event._controller = self

        if not self.pastEvents:
            previousEvent = self.pastEvents[-1]

            assert event.due > previousEvent.due, "Event's due is not in the future"

        futureEvents = self.futureEvents

        futureEvents.append(event)
        futureEvents.sort(key=lambda event: event.due)

        self._events = self.pastEvents + futureEvents

    def simulate(self) -> None:
        while True:
            immediateEvent = self.futureEvents[0]

            self._immediateEventIndex += 1
            self._clock = immediateEvent.due

            if self.clock > self.stop:
                break

            immediateEvent.dispatch()
