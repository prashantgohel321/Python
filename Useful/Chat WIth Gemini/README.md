# Gemini Chatbot with Google Generative AI

This Python script allows you to interact with **Google Gemini** models using the `google-generativeai` library.  
You can have a simple chat with the Gemini model right in your terminal.

---

## 📜 Script Overview

**Python Script:**
```python
import google.generativeai as genai

API_KEY = "API_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with gemini! Type exit to quit!")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini", response.text)
```

### What it does:

- Configures the Gemini API with your API key.

- Creates a chat session with the gemini-2.0-flash model.

- Allows you to send messages and get responses until you type exit.

---

<br>

### 🔑 Getting Your API Key from Google AI Studio
Follow these steps to obtain an API key:

- Go to Google AI Studio
https://aistudio.google.com/

- Sign in with your Google account
Make sure you use the account you want to link with your API usage.

- Create a new API key

- In the "Get API key" section, click "Create API key".

- Choose "Create API key in new project" or select an existing Google Cloud project.

- Copy your API key

- After creation, you'll see a key string — copy it somewhere safe.
- > ⚠️ Never share your API key publicly.

- Replace API_KEY in the script

Edit the script and replace:
```python
API_KEY = "API_KEY"
```
with:
```python
API_KEY = "your_actual_api_key_here"
```

---

<br>

## How to Run the Script
Install the required library
```bash
pip install google-generativeai
```
Save the script (e.g., gemini_chat.py).

Run it

```bash
python gemini_chat.py
```

Chat with Gemini

- Type any message and press Enter.

- Type exit to quit.

---

<br>

## Notes & Safety
- Your API key is sensitive. Do not upload scripts containing it to GitHub or share them online.

- Usage may incur costs depending on your API plan — check the Google AI pricing page.

