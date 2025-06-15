"""Run a simple economic simulation"""

from .agents import Consumer, Producer
from .market import Market
import matplotlib.pyplot as plt


def main():
    consumers = [Consumer(id=i, wealth=10.0, income=1.0, preference=1.0) for i in range(5)]
    producers = [Producer(id=i+100, wealth=0.0, cost=0.5, capacity=5.0) for i in range(3)]

    market = Market(consumers=consumers, producers=producers, price=1.0)
    market.run(steps=50)

    df = market.to_dataframe()
    print(df.tail())

    df[['price']].plot(title='Market Price')
    plt.xlabel('Step')
    plt.ylabel('Price')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
