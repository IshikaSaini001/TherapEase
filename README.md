# TharapEase: Your Mental Wellness Ally

TharapEase is a Streamlit-based chatbot application designed to provide mental wellness support. The application leverages Google Gemini Pro's generative AI capabilities to respond to user queries.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Environment Variables](#environment-variables)

## Introduction
TharapEase is a chatbot designed to assist users with mental wellness by providing insightful and supportive responses to their questions. The bot uses Google Gemini Pro, a powerful generative AI model, to generate its responses.

## Features
- User-friendly interface built with Streamlit.
- Real-time chat interaction.
- Persistent chat history within a session.
- Responses generated using Google Gemini Pro model.

## Requirements
- Python 3.x
- Streamlit
- `python-dotenv`
- `google-generativeai` (or the appropriate library to interface with Google Gemini Pro)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/IshikaSaini001/TherapEase.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TherapEase
   ```
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Set up your environment variables by creating a `.env` file in the project root and adding your Google API key:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```
2. Run the Streamlit application:
   ```bash
   streamlit run main.py
   ```
3. Open the provided local URL in your web browser to interact with the chatbot.

## Environment Variables
This project uses the `python-dotenv` library to manage environment variables. Ensure you have a `.env` file in your project root with the following variable:
- `GOOGLE_API_KEY`: Your API key for accessing Google Gemini Pro.

## Example `.env` file:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### Example Commit Message

When making the initial commit for this project, you might use:

```plaintext
Initial commit with Streamlit chatbot application for mental wellness support
```
