import yaml
from openai import OpenAI
from typing import List
Message = dict[str,str]

class ModelInterface:
    def __init__(self):
        """Model Interface cass for communicating with the model"""
        with open("config.yaml","r") as f:
            config = yaml.safe_load(f)

        self.model = config.get("LM_STUDIO_MODEL","llama-3.2-3b-instruct")

        LM_STUDIO_URL = config.get("LM_STUDIO_URL","http://localhost:1234/v1")
        LM_STUDIO_API_KEY =config.get("LM_STUDIO_API_KEY","lm-studio")

        self.client = OpenAI(base_url = LM_STUDIO_URL, api_key = LM_STUDIO_API_KEY)

    def chat_completion(
            self,
            messages: List[Message],
            temperature: float = 0.7,
            stream: bool = False
            ):
        """Use a llm to generate txt"""
        resp = self.client.chat.completions.create(
            model = self.model, messages = messages, temperature = temperature
        )

        return resp.choices[0].message.content