from flask import Flask, render_template
import ai as ai
app= Flask(__name__)

@app.route("/")
def alpha_home():
    return render_template('./index.html')

@app.route("/response")
def aires():
    return ai.get_ai_response("Hi")

if __name__ == "__main__":
    app.run()