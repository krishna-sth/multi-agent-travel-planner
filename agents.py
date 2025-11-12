from gemini_client import GeminiClient
from tools import get_destinations, get_flight_costs, get_itinerary,get_weather

class DestinationAgent:
    def __init__(self, gemini: GeminiClient):
        self.gemini = gemini

    def run(self, season, activity, user_request):
        destinations = get_destinations(season, activity)
        prompt = (
            f"User request: {user_request}\n"
            f"Suggested destinations: {', '.join(destinations)}.\n"
            "Pick the most suitable destination and explain why."
        )
        reasoning = self.gemini.ask(prompt)
        return destinations, reasoning

class BudgetAgent:
    def __init__(self, gemini: GeminiClient):
        self.gemini = gemini

    def run(self, origin, destinations):
        costs = get_flight_costs(origin, destinations)
        prompt = (
            f"Destinations: {destinations}\n"
            f"Flight costs from {origin}: {costs}\n"
            "Which destination is most budget-friendly and why?"
        )
        reasoning = self.gemini.ask(prompt)
        return costs, reasoning

class ItineraryAgent:
    def __init__(self, gemini: GeminiClient):
        self.gemini = gemini

    def run(self, destination):
        itinerary_text = get_itinerary(destination)
        prompt = (
            f"Destination: {destination}\n"
            f"Generate a short travel itinerary including top activities and travel tips based on: {itinerary_text}"
        )
        final_itinerary = self.gemini.ask(prompt)
        return final_itinerary,itinerary_text
    
class WeatherAgent:
    def __init__(self, gemini: GeminiClient):
        self.gemini = gemini

    def run(self, city):
        weather_info = get_weather(city)
        prompt = (
            f"City: {city}\n"
            f"Current weather: {weather_info}\n"
            "Provide a brief summary of the weather and how it affects travel plans."
        )
        weather_summary = self.gemini.ask(prompt)
        return weather_summary
