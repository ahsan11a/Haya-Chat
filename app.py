from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# OpenAI API Key (replace with your actual key)
openai.api_key = "your api key"

@app.route('/')
def haya():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("message", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    
    reply = response["choices"][0]["message"]["content"]
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)