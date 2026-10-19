# Trip planning agent

### Planning a trip usually involves jumping between multiple websites, let's use ai to simplify the process

## Multiple agents will be used

- flight search agent (Aviation stack API)
- hotel research agent (Tavily Search)
- itinerary planning agent (Tavily Search)
- final response agent (Groq llm(llama3))

## Languages

- python

## Tools

- llms (Large Langauge Models)
- LangGraph
- MCP
- postgreSQL

## How to run the app

1. create the virtual env

```bash
conda create -n trip python=3.11 -y
```

2. activate env

```bash
conda activate trip
```

3. install requirements.txt

```bash
pip install -r requirements.txt
```
