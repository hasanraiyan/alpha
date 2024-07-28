import os
import google.generativeai as genai
api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)
import markdown

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
  system_instruction="""You are a large language model, artificial intelligence name Alpha, you are created in hasan industries. 
    use pollination ai for any image needed
![Image](https://image.pollinations.ai/prompt/{description}?width={width}&height={height})
  
where {description} is:
{sceneDetailed}%20{adjective}%20{charactersDetailed}%20{visualStyle}%20{genre}%20{artistReference}
 

add this markdown list to show images in the response
"""
#   tools='code_execution',
)

chat_session = model.start_chat(
  history=[
      
  ]
)
def get_ai_response(query):
    response = chat_session.send_message(query)
    return markdown.markdown(response.text)



if __name__ == "__main__":
    print(get_ai_response("How are you"))
