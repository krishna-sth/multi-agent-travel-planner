import google.generativeai as genai

class GeminiClient:
    def __init__(self, api_key: str, model_name: str = "gemini-2.0-flash-lite"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def ask(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error calling Gemini API: {e}"
