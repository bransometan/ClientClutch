# ClientClutchBE

An AI-enabled customer service improvisation tool that allows transcription, comprehension, and analysis of customer support interactions. The project combines cutting-edge technologies such as an AI response generator, machine learning-based analytics, and data-driven insights.

## Project Overview

ClientClutch, a 23/24 Sem 1 IS4301 Project by Scrum Master United is designed to enhance customer service interactions by providing real-time transcription, comprehension, and analysis. Leveraging AI response generation and machine learning analytics, it aims to improve customer support quality and provide valuable data-driven insights.

## Table of Contents
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before you start, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (version x.x or higher)
- [Pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

### Installation

```bash
# Clone the repository
git clone https://github.com/bransome/ClientClutch
cd ClientClutch

# Install dependencies
pip install -r requirements.txt
```
### Setting up the .env file
1) Create a .env file in the root of your project.
2) Add the following configurations to the .env file:
```bash
# Example .env file
# API_KEY: A secret key for securing your application. The secret key can be obtained from https://platform.openai.com/api-keys.
API_KEY=your_secret_key
```
3) Replace your_secret_key with appropriate values.

Note: Make sure to add .env to your .gitignore file to avoid pushing sensitive information to your repository.

## Usage
To run the application locally:

```bash
python app.py
Visit http://localhost:3000 in your browser.
```
## Running Test with Pytest
Run the following command below to run the python test suite cases
```bash
python -m pytest
```
## API Endpoints
Demo API Usage: https://client-clutch.vercel.app/
### Sentiment Analysis
Endpoint: https://localhost:3000/api/sentiment <br>
Request:   <br>
```bash
"method": "POST",
"header": [
  {
    "key": "Content-Type",
    "value": "application/json",
    "type": "text",
    "disabled": true
  }
],
"body": {
  "mode": "raw",
  "raw": "{\r\n  \"text\": \"I am breaking the system\"\r\n}",
  "options": {
    "raw": {
      "language": "json"
    }
  }
}
```
Response:   <br>
```bash
{
    "recommended_actions": [
        "Celebrate the positive sentiment!",
        "Take advantage of the positive vibes."
    ],
    "result": "The sentiment of the text is positive."
}
```
### Fraud Detection
Endpoint: https://localhost:3000/api/fraud <br>
Request:   <br>
```bash
"method": "POST",
"header": [
  {
    "key": "Content-Type",
    "value": "application/json",
    "type": "text",
    "disabled": true
  }
],
"body": {
  "mode": "raw",
  "raw": "{\r\n  \"text\": \"I am scammer\"\r\n}",
  "options": {
    "raw": {
      "language": "json"
    }
  }
}
```
Response:   <br>
```bash
{
    "recommended_actions": [
        "Initiate a thorough investigation.",
        "Contact the relevant authorities."
    ],
    "result": "The text 'I am scammer' is likely to be fraudulent, and the fraud level is high."
}
```
### Security Risk Analysis
Endpoint: https://localhost:3000/api/security <br>
Request:   <br>
```bash
"method": "POST",
"header": [
  {
    "key": "Content-Type",
    "value": "application/json",
    "type": "text",
    "disabled": true
  }
],
"body": {
  "mode": "raw",
  "raw": "{\r\n  \"text\": \"I am breaking the system\"\r\n}",
  "options": {
    "raw": {
      "language": "json"
    }
  }
}
```
Response:   <br>
```bash
{
    "recommended_actions": [
        "Review and address moderate security risks.",
        "Consider implementing additional security measures."
    ],
    "result": "The security risk in the text is moderate. The text indicates that the person is trying to break the system, which could lead to data loss or theft."
}
```
### Compliance and Confidentiality Analysis
Endpoint: https://localhost:3000/api/compliconfid <br>
Request:   <br>
```bash
"method": "POST",
"header": [
  {
    "key": "Content-Type",
    "value": "application/json",
    "type": "text",
    "disabled": true
  }
],
"body": {
  "mode": "raw",
  "raw": "{\r\n  \"text\": \"I am hacker\"\r\n}",
  "options": {
    "raw": {
      "language": "json"
    }
  }
}
```
Response:   <br>
```bash
{
    "recommended_actions": [
        "Address the confidentiality breach promptly.",
        "Implement security measures to prevent future breaches."
    ],
    "result": "This is a confidentiality breach as it reveals information that should be kept secret."
}
```
### Predictive Response Analysis
Endpoint: https://localhost:3000/api/generate_reply <br>
Request:   <br>
```bash
"method": "POST",
"header": [
  {
    "key": "Content-Type",
    "value": "application/json",
    "type": "text",
    "disabled": true
  }
],
"body": {
  "mode": "raw",
  "raw": "{\r\n  \"message\": \"Hi\"\r\n}",
  "options": {
    "raw": {
      "language": "json"
    }
  }
}
```
Response:   <br>
```bash
{
    "result": "Hello! How can I assist you today?"
}
```
## Tech Stack
Python with Flask

## Features
- **Machine Learning-Based Analytics (MVP 1)**
- Real-time Transcription (Future MVP)
- AI Response Generator (Future MVP)
- Data-Driven Insights (Future MVP)

## Contributing
We welcome contributions! If you find a bug or have suggestions for improvement, please open an issue or submit a pull request.
