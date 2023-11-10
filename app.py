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

    return generated_text

def analyze_fraud_potential(text):
    openai.api_key = api_key

    # You can customize the prompt based on your specific use case
    prompt = f"Detect potential fraud in the following text: '{text}'"

    # Adjust parameters as needed
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
    )

    # Extract the generated text from the API response
    analysis_result = response.choices[0].text.strip()

    return analysis_result

def analyze_security_risks(input_text):
    openai.api_key = api_key

    # Customize the prompt for security risk analysis
    prompt = f"Detect security risks in the following text: '{input_text}'"

    # Adjust parameters as needed
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,  # Adjust based on the desired response length
    )

    # Extract the generated text from the API response
    security_analysis_result = response.choices[0].text.strip()

    return security_analysis_result

def analyze_compliance_and_confidentiality_risks(input_text):
    openai.api_key = api_key

    # Customize the prompt for combined compliance and confidentiality risk analysis
    prompt = f"Detect compliance and confidentiality risks in the following text: '{input_text}'"

    # Adjust parameters as needed
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,  # Adjust based on the desired response length
    )

    # Extract the generated text from the API response
    combined_analysis_result = response.choices[0].text.strip()

    return combined_analysis_result

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
    sentiment_analysis = analyze_sentiment(input_text)

    return render_template('result.html', result=sentiment_analysis)

@app.route('/fraud', methods=['POST'])
def fraud_endpoint():
    input_text = request.form['fraud_text']
    fraud_analysis = analyze_fraud_potential(input_text)

    return render_template('result.html', result=fraud_analysis)

@app.route('/security', methods=['POST'])
def security_endpoint():
    input_text = request.form['security_text']
    security_analysis = analyze_security_risks(input_text)

    return render_template('result.html', result=security_analysis)

@app.route('/compliconfid', methods=['POST'])
def compliconfid_endpoint():
    input_text = request.form['compliconfid_text']
    compliconfid_analysis = analyze_compliance_and_confidentiality_risks(input_text)

    return render_template('result.html', result=compliconfid_analysis)

@app.route('/generate_reply', methods=['POST'])
def generate_reply_endpoint():
    customer_message = request.form['customer_message']
    assistant_reply = generate_reply(customer_message)

    return render_template('result.html', result=assistant_reply)

if __name__ == '__main__':
    app.run(debug=True)
