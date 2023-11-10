from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
api_key = "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"

# ... (Your sentiment analysis and conversation history code here)

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
def sentiment():
    input_text = request.form['text']
    sentiment_analysis = analyze_sentiment(input_text)

    return render_template('result.html', result=sentiment_analysis)

@app.route('/generate_reply', methods=['POST'])
def generate_reply_endpoint():
    customer_message = request.form['customer_message']
    assistant_reply = generate_reply(customer_message)

    return render_template('result.html', result=assistant_reply)

if __name__ == '__main__':
    app.run(debug=True)
