from tools.tavily_tool import tavily_search
from tools.flight_tool import search_flights

# response = tavily_search("Best hotels in London")

# print(response)


response = search_flights("Plan a 7 days Japan trip from London")

print(response)
