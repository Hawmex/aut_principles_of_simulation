import random
from typing import *


class SimEvent[T: SimController]:
    """
    A class representing a simulated event.

    Attributes:
    - interval (float): The time interval until the event triggers.
    - due (float): The time when the event is due to be triggered.
    - controller (SimController): The controller associated with the event.
    """

    def __init__(self, interval: float) -> None:
        """
        Initialize the SimEvent with a given interval.

        Args:
        - interval (float): The time interval until the event triggers.

        Raises:
        - AssertionError: If interval is negative.
        """

        assert interval >= 0, "Negative interval"

        self.due: float
        self.controller: T

        self.interval = interval

    def trigger(self) -> None:
        """
        Trigger the event.

        This method should be implemented by subclasses.
        """

        raise NotImplementedError()


class SimController:
    """
    A class representing a simulated controller.

    Attributes:
    - futureEvents (List[SimEvent]): A list of future events.
    - clock (float): The current simulation time.
    - stop (float): The time at which the simulation should stop.
    """

    def __init__(self, initialEvent: SimEvent, stop: float) -> None:
        """
        Initialize the SimController with an initial event and a stop time.

        Args:
        - initialEvent (SimEvent): The initial event to start the simulation.
        - stop (float): The time at which the simulation should stop.

        Raises:
        - AssertionError: If the initial event's interval is non-zero or if the stop time is non-positive.
        """

        assert initialEvent.interval == 0, "Non-zero interval for the initial event"
        assert stop > 0, "Non-positive stop time"

        initialEvent.due = 0
        initialEvent.controller = self

        self.futureEvents: List[SimEvent] = [initialEvent]
        self.clock: float = 0

        self.stop = stop

    def dispatchEvent(self, event: SimEvent) -> None:
        """
        Dispatch an event to be scheduled in the future.

        Args:
        - event (SimEvent): The event to be dispatched.
        """
        event.due = self.clock + event.interval
        event.controller = self

        self.futureEvents.append(event)
        self.futureEvents.sort(key=lambda event: event.due)

    def simulate(self) -> None:
        """
        Run the simulation until the stop time is reached.
        """

        while self.futureEvents[0].due <= self.stop:
            upcomingEvent = self.futureEvents.pop(0)
            self.clock = upcomingEvent.due

            upcomingEvent.trigger()


class DistributionFunction:
    """
    A class providing various distribution functions for simulation.
    """

    @staticmethod
    def uniform(min: float, max: float) -> float:
        """
        Generate a random number from a uniform distribution between min and max.

        Args:
        - min (float): The minimum value of the distribution.
        - max (float): The maximum value of the distribution.

        Returns:
        - float: A random number from the uniform distribution between min and max.

        Raises:
        - AssertionError: If max is not greater than min.
        """

        assert max > min, "max must be greater than min"

        return random.random() * (max - min) + min
