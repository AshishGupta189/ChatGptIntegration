import json
import requests
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)

API_KEY = "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"
GPT3_API_URL = "https://api.openai.com/v1/chat/completions"

@app.route("/route_with_cors", methods=["GET"])
@cross_origin()  # Apply CORS to this route
def route_with_cors():
    data = {"message": "CORS is enabled for this route"}
    return jsonify(data)


@app.route('/codeconverter', methods=['POST'])
def convert_code():
    try:
        data = request.get_json()

        if 'code' not in data or 'language' not in data:
            return jsonify({'error': 'Both code and language are required in the request body.'}), 400

        code = data['code']
        language = data['language']

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": f"You are a Code Converter. Please convert the existing code {code} into this {language}.just give me the code in another language and nothing else"
                },
                {
                    "role": "user",
                    "content": f"Convert the existing code {code} into this {language}."
                }
            ],
            "model": "gpt-3.5-turbo"
        }

        response = requests.post(GPT3_API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            response_data = response.json()
            converted_code = response_data['choices'][0]['message']['content']
            return jsonify({'converted_code': converted_code})
        else:
            return jsonify({"error": "Code conversion failed"}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/codedebugger', methods=['POST'])
def debug_code():
    try:
        data = request.get_json()

        if 'code' not in data :
            return jsonify({'error': 'code is required to debug .'}), 400

        code = data['code']

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": f"You are a skilled code debugger. Please review the following code {code} and identify and fix any issues. Explain each problem and then fix clearly. "
                },
                {
                    "role": "user",
                    "content": f"review the following code {code}  "
                }
            ],
            "model": "gpt-3.5-turbo"
        }

        response = requests.post(GPT3_API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            response_data = response.json()
            debug_code = response_data['choices'][0]['message']['content']
            return jsonify({'debugged_code': debug_code})
        else:
            return jsonify({"error": "Code debug failed"}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/codequality', methods=['POST'])
def qualitycheck_code():
    try:
        data = request.get_json()

        if 'code' not in data:
            return jsonify({'error': 'code is required to check the quality.'}), 400

        code = data['code']
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        # Define the prompt for quality evaluation
        prompt = f"You are a code quality evaluator. Your task is to assess the quality of the following code:\n\n{code}\n\n" \
                "Please review the code and provide feedback based on the following criteria:\n\n" \
                "1. Code Structure: Comment on the organization and structure of the code. Are functions, classes, and " \
                "variables appropriately named and organized?\n" \
                "2. Readability: Assess the readability of the code. Is the code easy to understand and well-documented with " \
                "comments where necessary?\n" \
                "3. Efficiency: Comment on the efficiency of the code. Are there any potential performance issues or " \
                "inefficient algorithms?\n" \
                "4. Best Practices: Check if the code follows best practices for the given programming language.\n" \
                "5. Error Handling: Evaluate how the code handles errors and exceptions.\n" \
                "6. Security: Comment on potential security vulnerabilities in the code.\n" \
                "7. Overall Quality: Provide an overall assessment of the code's quality.\n\n" \
                "Please be specific in your feedback, pointing out any issues or areas for improvement. " \
                "Your feedback will help the user enhance the quality of their code."

        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": f"Please review the following code:\n\n{code}"
                }
            ],
            "model": "gpt-3.5-turbo"
        }

        response = requests.post(GPT3_API_URL, headers=headers, data=json.dumps(payload))
        print(response.json())
        if response.status_code == 200:
            response_data = response.json()
            qualitychecker = response_data['choices'][0]['message']['content']
            return jsonify({'quality_of_code': qualitychecker})
        else:
            print(response)
            return jsonify({"error": "Code quality check failed"}), 500

    except Exception as e:
        
        return jsonify({'error': str(e)}), 500

if __name__ == '__main':
    app.run(host='0.0.0.0', port=8080)
