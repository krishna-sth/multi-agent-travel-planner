import os
import time
import requests
import random


OPENTRIPMAP_API_KEY ='5ae2e3f221c38a28845f05b642174c0ba49e884eb6614eaf37741d02'
WEATHER_API_KEY='4d20eda3d2a9433d9fb172911251408'



def get_destinations(season=None, activity=None):

    fallback_destinations = {
    "adventure": ["Tokyo", "Queenstown", "Vancouver", "Cape Town", "Cusco", "Reykjavik", "Banff"],
    "beach": ["Bali", "Maldives", "Phuket", "Santorini", "Maui", "Boracay", "Barbados"],
    "cultural": ["Rome", "Kyoto", "Istanbul", "Athens", "Paris", "Marrakech", "Lisbon"],
    "nature": ["Yellowstone", "Patagonia", "Serengeti", "Amazon Rainforest", "Swiss Alps", "Norwegian Fjords"],
    "romantic": ["Venice", "Paris", "Prague", "Bruges", "Florence", "Kyoto", "Santorini"],
    "historical": ["Cairo", "Jerusalem", "Petra", "Beijing", "Rome", "Athens", "Istanbul"]
}

    if activity:
        return fallback_destinations.get(activity.lower(), ["Paris", "Tokyo", "Barcelona"])
    else:
        return ["Paris", "Tokyo", "Barcelona"]


def get_flight_costs(origin: str, destinations: list):
    costs = {}
    for dest in destinations:
        # Base price
        base_price = random.randint(200, 900)
        # Add some random variation per destination
        variation = random.randint(-50, 200)
        total_cost = max(100, base_price + variation)  # Ensure cost is never below $100
        costs[dest] = total_cost
    return costs

def get_itinerary(destination: str):
    if not OPENTRIPMAP_API_KEY:
        return f"Top activities for {destination}: Visit museums, city tour, try local cuisine."

    try:
        geo = requests.get(
            "https://api.opentripmap.com/0.1/en/places/geoname",
            params={"name": destination, "apikey": OPENTRIPMAP_API_KEY},
            timeout=10
        ).json()
        lat, lon = geo.get("lat"), geo.get("lon")
    except:
        lat, lon = None, None

    pois = []
    if lat and lon:
        try:
            resp = requests.get(
                "https://api.opentripmap.com/0.1/en/places/radius",
                params={"lat": lat, "lon": lon, "radius": 4000, "limit": 5, "apikey": OPENTRIPMAP_API_KEY},
                timeout=10
            ).json()
            pois = [p.get("name") for p in resp]
        except:
            pois = []

    if not pois:
        pois = ["Visit museums", "City tour", "Try local cuisine"]

    return f"Top activities for {destination}: " + ", ".join(pois)


def get_weather(city):
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        params = {"key": WEATHER_API_KEY, "q": city}
        resp = requests.get(url, params=params, timeout=10).json()
        if "current" in resp:
            temp = resp["current"]["temp_c"]
            cond = resp["current"]["condition"]["text"]
            return f"{temp}°C, {cond}"
    except:
        pass
    return "Weather data unavailable."