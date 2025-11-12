from agents import DestinationAgent, BudgetAgent, ItineraryAgent,WeatherAgent
from gemini_client import GeminiClient  # your wrapper module
import json

def travel_planning_workflow(user_request, season="summer", activity="beach",
                             origin="Kathmandu", gemini_api_key=None):
    
    gemini = GeminiClient(api_key=gemini_api_key)

    # Initialize agents 
    dest_agent = DestinationAgent(gemini)
    budget_agent = BudgetAgent(gemini)
    itinerary_agent = ItineraryAgent(gemini)

    #  Destination Agent
    destinations, dest_reasoning = dest_agent.run(season, activity, user_request)
    print(f"DestinationFinder → {destinations}\nReasoning: {dest_reasoning}\n")

    # Budget Agent
    costs, budget_reasoning = budget_agent.run(origin, destinations)
    print(f"BudgetAnalyst → {costs}\nReasoning: {budget_reasoning}\n")

    # Itinerary Agent
    best_destination = min(costs, key=lambda k: int(str(costs[k]).replace("$","")))
    itinerary = itinerary_agent.run(best_destination)
    print(f"ItineraryPlanner → {itinerary}\n")

    # Weather Agent
    weather_agent = WeatherAgent(gemini)
    weather_summary = weather_agent.run(best_destination)
    print(f"WeatherSummary → {weather_summary}\n")


    plan_context = {
        "season": season,
        "activity": activity,
        "origin": origin,
        "user_request": user_request,
        "destinations": destinations,
        "estimated_costs": costs,
        "final_itinerary": itinerary,
        "best_destination": best_destination,
        "weather_summary": weather_summary
    }

    
    prompt = f"""
You are a travel expert. The following travel context is given as JSON:

{json.dumps(plan_context, indent=2)}

Using this context, create a detailed, readable travel plan for the user. 
Format it like a travel guide with explanations, recommended activities (with keeping in mind about the weather summary explain weather summary also) and why the destination was chosen. 
Do NOT output JSON, only human-readable text.
"""

    final_plan = gemini.ask(prompt)  

    print(f"Final Travel Plan → {final_plan}\n")

    return final_plan
