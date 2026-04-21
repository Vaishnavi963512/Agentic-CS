from openai import OpenAI
from tools import get_weather

# OpenRouter configuration
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

def run_agent(user_input: str):
    try:
        # Ask LLM to extract city
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct",
            messages=[
                {
                    "role": "user",
                    "content": f"""
                    Extract only the city name from this weather question:
                    {user_input}

                    Reply with ONLY the city name.
                    """
                }
            ]
        )

        city = response.choices[0].message.content.strip()
        return get_weather(city)

    except Exception as e:
        return f"Error: {str(e)}"