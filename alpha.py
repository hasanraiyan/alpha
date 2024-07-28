from flask import Flask, render_template
import ai as ai  # Import the ai module

app = Flask(__name__)

@app.route("/")
def alpha_home():
    return render_template('./index.html')

@app.route("/response/<query>")
def ai_res(query):
    response = ai.get_ai_response(query)  # Call the get_ai_response function
    return response  # Return the AI's response

if __name__ == "__main__":
    app.run()
