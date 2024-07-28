from flask import Flask, render_template, request
import ai as ai  

app = Flask(__name__)

# Render the index.html template at the root URL.
@app.route("/")
def alpha_home():
    return render_template('./index.html')

# Get a response from the AI model for a given query.
@app.route("/search")
def ai_res():
    query = request.args.get('q')
    if query:
        response = ai.get_ai_response(query)
        return response
    else:
        return "Please provide a query."

if __name__ == "__main__":
    app.run()
