

import os

import google.generativeai as genai

genai.configure(api_key="YOUR api key")


generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="you are jarvis a large langugae model",
  tools='code_execution',
)

chat_session = model.start_chat(
  history=[
  ]
)
def get_ai_response(query):
    response = chat_session.send_message(query)
    return response.text



if __name__ == "__main__":
    print(get_ai_response("How are you"))
