from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def student_number():
    return {'studentnumber': 200610320}

@app.route('/webhook', methods=['POST'])
def weather():
    req = request.get_json(silent=True, force=True)  # Get the request payload
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    if intent_name == "Check Weather":
        location = req.get("queryResult", {}).get("parameters", {}).get("geo-city", "").strip()
        if location in ["London", "New York"]:
            fulfillment_text = f"Let me provide the current weather information for {location}."
        else:
            fulfillment_text = "Could you please specify the city or location you'd like the weather information for?"
    else:
        fulfillment_text = "This intent is not integrated with the webhook."

    # Return the response as JSON
    return jsonify({"fulfillmentText": fulfillment_text})

if __name__ == '__main__':
    app.run(debug=True)
