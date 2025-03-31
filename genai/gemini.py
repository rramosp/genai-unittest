from google import genai
from google.genai import types
from loguru import logger

class GeminiModel:

    def __init__(self, 
                 model_id = "gemini-2.0-pro-exp-02-05",
                 project="gemma-test-deployment", 
                 location="us-central1",
                 temperature = 1.,
                 top_p = 1,
                 max_output_tokens=2048):

        self.project = project
        self.location = location
        self.top_p = top_p
        self.max_output_tokens = max_output_tokens
        self.model_id = model_id
        self.temperature = temperature

        logger.info(f'using {model_id}, temp {temperature}, top_p {top_p}, max_output_tokens {max_output_tokens}')
        
        self.client = genai.Client(
            vertexai=True,
            project=project,
            location=location,
        )

        self.generate_content_config = types.GenerateContentConfig(
            temperature = temperature,
            top_p = top_p,
            seed = 0,
            max_output_tokens = max_output_tokens,
            response_modalities = ["TEXT"],
            safety_settings = [types.SafetySetting(
              category="HARM_CATEGORY_HATE_SPEECH",
              threshold="OFF"
            ),types.SafetySetting(
              category="HARM_CATEGORY_DANGEROUS_CONTENT",
              threshold="OFF"
            ),types.SafetySetting(
              category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
              threshold="OFF"
            ),types.SafetySetting(
              category="HARM_CATEGORY_HARASSMENT",
              threshold="OFF"
            )],
        )  

    def generate_text(self, prompt):

        response = self.client.models.generate_content(
            #model='gemini-2.0-flash',
            model = self.model_id,
            config = self.generate_content_config,
            contents=prompt
        )

        answer = response.candidates[0].content.parts[0].text
        return answer
        
        