# Principles of Simulation
#
# By Hamed Araab & Shahriar Khalvati

import random
from typing import *


class SimEvent[T: SimController]:
    """
    A class representing a simulated event.

    Attributes:
    - interval (float): The time interval until the event triggers.
    - dueTime (float): The time when the event is due to be triggered.
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

        self.dueTime: float
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
    - stopTime (float): The time at which the simulation should stop.
    """

    def __init__(self, stopTime: float, initialEvent: SimEvent | None = None) -> None:
        """
        Initialize the SimController with an initial event and a stop time.

        Args:
        - stopTime (float): The time at which the simulation should stop.
        - initialEvent (SimEvent | None, optional): The initial event to start the simulation.
          Defaults to None.

        Raises:
        - AssertionError: If the initial event's interval is non-zero or if the stop time is non-positive.
        """

        assert stopTime > 0, "Non-positive stop time"

        if initialEvent is not None:
            assert initialEvent.interval == 0, "Non-zero interval for the initial event"

        self.futureEvents: List[SimEvent] = []
        self.clock: float = 0

        self.stopTime = stopTime

        if initialEvent is not None:
            self.dispatchEvent(initialEvent)

    def dispatchEvent(self, event: SimEvent) -> None:
        """
        Dispatch an event to be scheduled in the future.

        Args:
        - event (SimEvent): The event to be dispatched.
        """

        event.dueTime = self.clock + event.interval
        event.controller = self

        self.futureEvents.append(event)
        self.futureEvents.sort(key=lambda event: event.dueTime)

    def simulate(self) -> None:
        """
        Run the simulation until the stop time is reached.
        """

        while self.futureEvents[0].dueTime <= self.stopTime:
            upcomingEvent = self.futureEvents.pop(0)
            self.clock = upcomingEvent.dueTime

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
