from groq import Groq

# Replace with your actual Groq API Key
GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

def generate_poetry(mood_description, sentiment_label):
    """Uses Groq and Llama 3.3 to generate unique poetry."""
    try:
        completion = client.chat.completions.create(
            # Using Llama 3.3 70B for high-quality creative output
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional poet. You write short, 4-line poems that are deeply emotional and artistic."
                },
                {
                    "role": "user",
                    "content": f"The user is feeling {sentiment_label}. Their thoughts: '{mood_description}'. Write a 4-line poem reflecting this mood."
                }
            ],
            temperature=0.7, # Adds creativity
            max_tokens=150
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error with Groq API: {e}"
