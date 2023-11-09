#!/usr/bin/env python
# coding: utf-8

# This page consists of both (A)sentiment analysis and (B) Generation of responses based on customer queries. 

# In[2]:


import openai


# In[3]:


api_key = "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"


# In[16]:


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

# Perform sentiment analysis
while True:
    input_phrase = input("The Customer's comments: ")
    
    if input_phrase.lower() == 'x':
        break

    sentiment_analysis = analyze_sentiment(input_phrase)

    # Interpret sentiment and provide a simple message
    if "positive" in sentiment_analysis.lower():
        sentiment_message = "The customer's sentiment is: Positive :)"
    elif "negative" in sentiment_analysis.lower():
        sentiment_message = "The customer's sentiment is: Negative :("
    else:
        sentiment_message = "The customer's sentiment is: Neutral :|"

    print(sentiment_message)


# In[17]:


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

while True:
    customer_message = input("Customer: ")
    if customer_message.lower() == 'x':
        break

    assistant_reply = generate_reply(customer_message)
    print(f"Assistant: {assistant_reply}")

