from google import genai

prompt = "o que é python?"


client = genai.client(
    api_key=""
)

response = client.models.generate_content(
    model="gemini-2.5-flash"
    
)
print(response.text)