# 🌍 Multi-Agent Travel Planner

A Streamlit-based travel planning application powered by multi-agent AI using **Google Gemini**. It helps users plan trips by suggesting destinations, evaluating budget, generating itineraries, and summarizing weather conditions.

---

## Features

- **Destination Suggestion:** Finds destinations based on season and activity.
- **Budget Analysis:** Compares flight costs and finds the most budget-friendly destination.
- **Itinerary Generation:** Generates detailed itineraries with top activities.
- **Weather Summary:** Provides current weather and how it affects travel.
- **Human-Readable Travel Plan:** Combines all information into a complete travel guide.

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/multi-agent-travel-planner.git
cd multi-agent-travel-planner
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
1. Run the Streamlit app:
```bash
streamlit run main.py
```

2. Enter your Gemini API Key in the sidebar.

3. Fill in your travel preferences, season, activity, and origin city.

4. Click Plan My Trip 🌟 to generate your travel plan.

## Project Structure
```text
multi-agent-travel-planner/
│
├─ main.py              # Streamlit frontend
├─ workflow.py          # Orchestrates multi-agent workflow
├─ agents.py            # AI agents (destination, budget, itinerary, weather)
├─ gemini_client.py     # Gemini API wrapper
├─ tools.py             # Helper functions for destinations, flights, weather
├─ requirements.txt
├─ README.md
├─ .gitignore
```


