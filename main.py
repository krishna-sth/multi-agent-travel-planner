import streamlit as st
from workflow import travel_planning_workflow


st.set_page_config(page_title="Multi-Agent Travel Planner", layout="wide")
st.title("🌍 Multi-Agent Travel Planner")


st.sidebar.header("🔐 Gemini API Key Setup")
gemini_api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")

if not gemini_api_key:
    st.warning("Please enter your Gemini API key to start.")
    st.stop()

# User inputs
st.header("Travel Preferences")
user_request = st.text_input("Describe your travel preferences", value="Adventure holiday")
season = st.selectbox("Select season", ["Summer", "Winter", "Spring", "Autumn"])
activity = st.selectbox(
    "Select main activity",
    ["Adventure", "Beach", "Chilling", "Cultural", "Romantic", "Historical", "Nature"]
)
origin = st.text_input("Your origin city", value="Kathmandu")


if st.button("Plan My Trip 🌟"):
    with st.spinner("Planning your trip..."):
        try:
            plan = travel_planning_workflow(
                user_request=user_request,
                season=season.lower(),
                activity=activity.lower(),
                origin=origin,
                gemini_api_key=gemini_api_key
            )


            st.success("✅ Travel plan generated!")
            st.code(plan)

        except Exception as e:
            st.error(f"Error generating travel plan: {e}")
