import json
import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)

API_KEY = "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"
GPT3_API_URL = "https://api.openai.com/v1/chat/completions"


@app.route("/")
def welcome():
    return "Welcome to shayari generator"

@app.route("/route_with_cors", methods=["GET"])
@cross_origin()  # Apply CORS to this route
def route_with_cors():
    data = {"message": "CORS is enabled for this route"}
    return jsonify(data)


@app.route('/shayari/generate', methods=['GET'])
def generate_shayari():
    keyword = request.args.get('keyword')
    length = request.args.get('length')
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    payload = {
        "messages": [
            {
                "role": "system",
                "content": f"You are a Shayari generator. Please generate a complete Shayari about {keyword} within {length} words only."
            },
            {
                "role": "user",
                "content": f"Generate a complete Shayari about {keyword} within {length} words only."
            }
        ],
        "model": "gpt-3.5-turbo"
    }
    
    response = requests.post(GPT3_API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        response_data = response.json()
        generated_shayari = response_data['choices'][0]['message']['content']
        return  response_data #render_template('shayari.html', shayari=generated_shayari)
    else:
        return jsonify({"error": "Shayari generation failed"})

if __name__ == '__main':
    app.run(host='0.0.0.0', port=8080)
