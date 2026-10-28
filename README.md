# Trip planning agent

### What is this?

Planning a trip usually involves jumping between multiple websites, let's use ai to simplify the process

## Multiple agents will be used

- flight search agent (Aviation stack API)
- hotel research agent (Tavily Search)
- weather agent (Custom Weather MCP)
- itinerary planning agent (Tavily Search)
- final response agent (Groq llm(llama3))

## Languages

- python
- html
- css

## Tools

- llms (Large Langauge Models)
- LangGraph
- Langchain
- MCP
- postgreSQL
- FastAPI
- Tavily API
- AviationStack API

## Workflow

1. The user submits a travel request.
2. The flight agent gathers flight-related information.
3. The hotel agent searches for accommodation suggestions.
4. The itinerary agent creates a practical travel plan.
5. The final agent formats the result into a polished response.

## Project Structure

```text
.
├── app.py                # FastAPI app entry point
├── backend.py            # LangGraph travel workflow
├── requirements.txt      # Python dependencies
├── static/               # Static frontend assets
├── templates/            # HTML templates
└── tools/                # Flight and web search integrations
```

## Environment Variables

Create a .env file in the project root with the following variables:
use .example.env as reference

```env
DATABASE_URL=postgresql://user:password@localhost:5432/travel_db
GROQ_API_KEY=your_groq_api_key
AVIATIONSTACK_API_KEY=your_aviationstack_api_key
TAVILY_API_KEY=your_tavily_api_key
DEFAULT_ORIGIN_IATA=DAC
```

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

4. Start the FastAPI server:

```bash
python app.py
```

5. Then open your browser at:

```text
http://127.0.0.1:8000/
```
