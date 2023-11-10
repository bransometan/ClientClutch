from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = "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"

# ... (Your predictive code below here)

# Call the OpenAI
def analyze_sentiment(input_text):
    openai.api_key = api_key

    # You can adjust the temperature and max tokens to control the response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Analyze the sentiment of the following text: '{input_text}'",
        temperature=0.7,
        max_tokens=50,
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()

     # You can add logic here to extract recommended actions based on the sentiment
    recommended_actions = get_sentiments_recommended_actions(generated_text)

    return generated_text, recommended_actions

def get_sentiments_recommended_actions(sentiment_result):
    # Add your logic to generate recommended actions based on sentiment
    # This can include checking if sentiment is positive, negative, or neutral
    # and suggesting appropriate actions accordingly.
    # Replace the following with your actual logic.
    if "positive" in sentiment_result:
        return ["Celebrate the positive sentiment!", "Take advantage of the positive vibes."]
    elif "negative" in sentiment_result:
        return ["Address the concerns raised.", "Take corrective actions."]
    else:
        return ["Continue monitoring the situation.", "Stay vigilant."]
    
def analyze_fraud_potential(text):
    openai.api_key = api_key

    # You can customize the prompt based on your specific use case
    prompt = f"Detect potential fraud in the following text: '{text}'. Moreover, also indicate fraud level: high, medium, low"

    # Adjust parameters as needed
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
    )

    # Extract the generated text from the API response
    analysis_result = response.choices[0].text.strip()

     # You can add logic here to extract recommended actions based on the fraud analysis
    recommended_actions = get_fraud_recommended_actions(analysis_result)

    return analysis_result, recommended_actions

def get_fraud_recommended_actions(fraud_analysis_result):
    # Add your logic to generate recommended actions based on fraud analysis
    # This can include checking if fraud potential is high, medium, or low
    # and suggesting appropriate actions accordingly.
    # Replace the following with your actual logic.
    if "high" in fraud_analysis_result:
        return ["Initiate a thorough investigation.", "Contact the relevant authorities."]
    elif "medium" in fraud_analysis_result:
        return ["Review the case in detail.", "Consider escalating if necessary."]
    else:
        return ["Monitor the situation closely.", "Stay vigilant for any further signs of fraud."]

def analyze_security_risks(input_text):
    openai.api_key = api_key

    # Customize the prompt for security risk analysis
    prompt = f"Detect security risks in the following text: '{input_text}'. Moreover, also indicate security risk level: critical, moderate, low"

    # Adjust parameters as needed
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,  # Adjust based on the desired response length
    )

    # Extract the generated text from the API response
    security_analysis_result = response.choices[0].text.strip()

     # You can add logic here to extract recommended actions based on the security risk analysis
    recommended_actions = get_security_recommended_actions(security_analysis_result)

    return security_analysis_result, recommended_actions

def get_security_recommended_actions(security_analysis_result):
    # Add your logic to generate recommended actions based on security risk analysis
    # This can include checking if security risks are critical, moderate, or low
    # and suggesting appropriate actions accordingly.
    # Replace the following with your actual logic.
    if "critical" in security_analysis_result:
        return ["Take immediate action to address critical security risks.", "Implement emergency security measures."]
    elif "moderate" in security_analysis_result:
        return ["Review and address moderate security risks.", "Consider implementing additional security measures."]
    else:
        return ["Monitor the security situation closely.", "Regularly assess and update security protocols."]

def analyze_compliance_and_confidentiality_risks(input_text):
    openai.api_key = api_key

    # Customize the prompt for combined compliance and confidentiality risk analysis
    prompt = f"Detect compliance and confidentiality risks in the following text: '{input_text}'.Moreover, also indicate whether it is compliance violation, confidentiality breach or none "

    # Adjust parameters as needed
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,  # Adjust based on the desired response length
    )

    # Extract the generated text from the API response
    combined_analysis_result = response.choices[0].text.strip()

     # You can add logic here to extract recommended actions based on the combined analysis
    recommended_actions = get_compliance_and_confidentiality_recommended_actions(combined_analysis_result)

    return combined_analysis_result, recommended_actions

def get_compliance_and_confidentiality_recommended_actions(combined_analysis_result):
    # Add your logic to generate recommended actions based on combined compliance and confidentiality risk analysis
    # This can include checking if risks are related to compliance violations, data breaches, etc.
    # and suggesting appropriate actions accordingly.
    # Replace the following with your actual logic.
    if "compliance violation" in combined_analysis_result:
        return ["Take immediate action to address compliance violations.", "Implement corrective measures."]
    elif "confidentiality breach" in combined_analysis_result:
        return ["Address the confidentiality breach promptly.", "Implement security measures to prevent future breaches."]
    else:
        return ["Monitor compliance and confidentiality closely.", "Regularly assess and update policies and security measures."]

conversation_history = []

def generate_reply(customer_message):
    openai.api_key = api_key

    # Extend the conversation
    conversation_history.append({"role": "system", "content": "You are a helpful assistant."})
    conversation_history.append({"role": "user", "content": customer_message})

    # Generate a reply
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    # Extract the reply from the API response
    generated_reply = response['choices'][0]['message']['content']

    # Append the generated reply to the conversation history
    conversation_history.append({"role": "assistant", "content": generated_reply})

    return generated_reply

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sentiment', methods=['POST'])
def sentiment_endpoint():
    input_text = request.form['sentiment_text']
    sentiment_result, recommended_actions = analyze_sentiment(input_text)

    return render_template('result.html', result=sentiment_result, recommended_actions=recommended_actions)

@app.route('/fraud', methods=['POST'])
def fraud_endpoint():
    input_text = request.form['fraud_text']
    fraud_analysis_result, recommended_actions = analyze_fraud_potential(input_text)

    return render_template('result.html', result=fraud_analysis_result, recommended_actions=recommended_actions)

@app.route('/security', methods=['POST'])
def security_endpoint():
    input_text = request.form['security_text']
    security_analysis_result, recommended_actions = analyze_security_risks(input_text)

    return render_template('result.html', result=security_analysis_result, recommended_actions=recommended_actions)

@app.route('/compliconfid', methods=['POST'])
def compliconfid_endpoint():
    input_text = request.form['compliconfid_text']
    combined_analysis_result, recommended_actions = analyze_compliance_and_confidentiality_risks(input_text)

    return render_template('result.html', result=combined_analysis_result, recommended_actions=recommended_actions)

@app.route('/generate_reply', methods=['POST'])
def generate_reply_endpoint():
    customer_message = request.form['customer_message']
    assistant_reply = generate_reply(customer_message)

    return render_template('result.html', result=assistant_reply)

if __name__ == '__main__':
    app.run(debug=True)
