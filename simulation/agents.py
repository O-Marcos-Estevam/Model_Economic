"""Agent classes for economic simulation"""

from dataclasses import dataclass
import random

@dataclass
class Agent:
    """Base class for all agents."""
    id: int
    wealth: float = 0.0

    def step(self, price: float) -> float:
        """Run agent's step in the market.

        Parameters
        ----------
        price : float
            Current market price.

        Returns
        -------
        float
            Quantity the agent wants to buy (>0) or sell (<0).
        """
        raise NotImplementedError

@dataclass
class Consumer(Agent):
    income: float = 1.0
    preference: float = 1.0  # quantity desired at price 1

    def step(self, price: float) -> float:
        # Simple demand: q = preference * income / price
        quantity = self.preference * self.income / max(price, 0.01)
        cost = quantity * price
        if cost > self.wealth:
            quantity = self.wealth / max(price, 0.01)
            cost = quantity * price
        self.wealth -= cost
        return quantity  # positive => demand

@dataclass
class Producer(Agent):
    cost: float = 0.5
    capacity: float = 10.0

    def step(self, price: float) -> float:
        # Produce if price above cost
        if price > self.cost:
            quantity = min(self.capacity, (price - self.cost) * 2)
        else:
            quantity = 0
        revenue = quantity * price
        self.wealth += revenue
        return -quantity  # negative => supply
