import streamlit as st
from .agents import Consumer, Producer
from .market import Market


def run_simulation(n_consumers: int, n_producers: int, steps: int):
    consumers = [Consumer(id=i, wealth=10.0, income=1.0, preference=1.0)
                 for i in range(n_consumers)]
    producers = [Producer(id=i + 100, wealth=0.0, cost=0.5, capacity=5.0)
                 for i in range(n_producers)]
    market = Market(consumers=consumers, producers=producers, price=1.0)
    market.run(steps)
    return market.to_dataframe()


def main():
    st.title("Agent-Based Market Simulation")
    st.markdown("Adjust parameters and press **Run simulation**.")

    n_consumers = st.slider("Number of consumers", 1, 50, 5)
    n_producers = st.slider("Number of producers", 1, 50, 3)
    steps = st.slider("Number of steps", 10, 200, 50)

    if st.button("Run simulation"):
        df = run_simulation(n_consumers, n_producers, steps)
        st.line_chart(df["price"], height=300)
        st.dataframe(df.tail())


if __name__ == "__main__":
    main()

