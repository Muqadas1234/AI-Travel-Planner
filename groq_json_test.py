from dotenv import load_dotenv
import os
import requests
import json
import re

# 🔹 Load .env file
load_dotenv()

# 🔹 Get API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

# 🔒 Check if key is missing
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found in .env file!")

# 🔹 Groq API setup
url = "https://api.groq.com/openai/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}"
}

# 🔹 Prompt with example JSON format
prompt = """
You are a professional travel agent.
Plan a 3-day budget trip to Istanbul under $400.
Return the result in **valid JSON** format like this:

{
  "flights": ["Flight from XYZ to IST on 5 July"],
  "hotels": ["Budget Stay Hotel in Istanbul"],
  "daily_itinerary": {
    "Day 1": "Visit Blue Mosque and Hagia Sophia",
    "Day 2": "Take Bosphorus cruise and explore local food",
    "Day 3": "Shopping at Grand Bazaar and relax at a Turkish Hammam"
  }
}
"""

# 🔹 Request body
data = {
    "model": "llama3-8b-8192",
    "messages": [{"role": "user", "content": prompt}]
}

# 🔹 Make API call
response = requests.post(url, headers=headers, json=data)

# 🔹 Show full response (optional debug)
print("🔍 Status Code:", response.status_code)
print("🔍 Full Response from Groq:")

try:
    # 🔹 Extract content from response
    raw_output = response.json()['choices'][0]['message']['content']

    # 🔹 Extract JSON from response using regex
    json_match = re.search(r"\{.*\}", raw_output, re.DOTALL)

    if json_match:
        json_text = json_match.group()
        parsed = json.loads(json_text)

        # ✅ Final output
        print("\n✅ Flights:", parsed['flights'])
        print("✅ Hotels:", parsed['hotels'])
        print("✅ Day-wise Itinerary:")
        for day, plan in parsed['daily_itinerary'].items():
            print(f"  {day}: {plan}")
    else:
        print("❌ JSON block not found in the response.")
        print("Full Response Text:\n", raw_output)

except Exception as e:
    print("❌ Error occurred while processing the response.")
    print("Exception:", e)
