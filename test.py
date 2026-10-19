from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights
from backend import run_travel_agent

# response = tavily_search("Best hotels in London")

# print(response)


# response = search_flights("Plan a 7 days Japan trip from London")

# print(response)

user_input = input("Enter trip idea: ")


response = run_travel_agent(user_input=user_input, thread_id="test_user")

print("\n\nFinal Trip Suggestion:\n\n")

print(response["answer"])
