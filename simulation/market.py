"""Simple market implementation"""

from dataclasses import dataclass, field
from typing import List
import pandas as pd

from .agents import Agent

@dataclass
class Market:
    consumers: List[Agent]
    producers: List[Agent]
    price: float = 1.0
    history: List[dict] = field(default_factory=list)

    def step(self):
        demand = 0.0
        supply = 0.0
        # Agents act based on current price
        for c in self.consumers:
            demand += c.step(self.price)
        for p in self.producers:
            supply += -p.step(self.price)  # step returns negative for supply
        # Compute excess demand
        excess_demand = demand - supply
        # Adjust price: simple proportional controller
        self.price *= 1 + 0.05 * (excess_demand / max(supply + demand, 1))
        self.history.append({
            "demand": demand,
            "supply": supply,
            "price": self.price,
            "excess_demand": excess_demand,
        })

    def run(self, steps: int):
        for _ in range(steps):
            self.step()

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame(self.history)
