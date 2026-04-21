import os
from openai import OpenAI
from tools import get_weather

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# -------------------------------
# Agent 1: Router Agent
# -------------------------------
def router_agent(user_input: str) -> str:
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a router agent. "
                        "Check whether the user is asking about weather. "
                        "Reply with only one word: WEATHER or UNKNOWN."
                    )
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip().upper()
    except Exception:
        return "UNKNOWN"


# -------------------------------
# Agent 2: City Extraction Agent
# -------------------------------
def city_extractor_agent(user_input: str) -> str:
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Extract only the city name from the user's weather question. "
                        "Reply with only the city name and nothing else."
                    )
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return ""


# -------------------------------
# Agent 3: Weather Execution Agent
# -------------------------------
def weather_agent(city: str) -> str:
    if not city:
        return "Sorry, I could not understand the city name."
    return get_weather(city)


# -------------------------------
# Agent 4: Response Agent
# -------------------------------
def response_agent(tool_output: str) -> str:
    # Same output maintain cheyyali kabatti direct ga return chestunnam
    return tool_output


# -------------------------------
# Main Orchestrator
# -------------------------------
def run_agent(user_input: str):
    try:
        route = router_agent(user_input)

        if route != "WEATHER":
            return "Sorry, I can only help with weather questions."

        city = city_extractor_agent(user_input)
        weather_result = weather_agent(city)
        final_response = response_agent(weather_result)

        return final_response

    except Exception as e:
        return f"Error: {str(e)}"
