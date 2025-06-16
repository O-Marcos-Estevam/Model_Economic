# Model Economic

This project contains a minimal agent-based economic simulation in Python.

## Structure

- `simulation/agents.py` — base classes for `Agent`, `Consumer`, and `Producer`.
- `simulation/market.py` — `Market` class that matches supply and demand and
  adjusts price dynamically.
- `simulation/run.py` — example script to run the simulation and plot results.

## Running

Install the required libraries (pandas, matplotlib) and run the script:

```bash
python -m simulation.run
```

codex/criar-classe-base-dos-agentes-e-simulação-de-mercado
For an interactive HTML dashboard, install `streamlit` and run:

```bash
streamlit run simulation/dashboard.py
```


 main
A plot showing the market price evolution will be displayed.
