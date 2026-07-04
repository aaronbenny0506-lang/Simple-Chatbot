# Simple Rule-Based Chatbot 🤖

A beginner-friendly chatbot that can hold basic conversations with users,
built with Python and a Streamlit web interface.

## 🎯 Approach

This chatbot uses a **rule-based system**: it scans each user message for
keywords and patterns (using regular expressions) and returns a matching
pre-written response, picked at random from a small pool of options for
variety. It doesn't call any external AI API, so it:

- Runs completely offline, with no API key or cost
- Responds instantly
- Is easy to understand and extend — new topics can be added by adding
  a new pattern + response list in `chatbot.py`

## ✨ What it can do

- Respond to greetings and farewells
- Tell simple jokes
- Answer "how are you", "what's your name", "what time/date is it"
- React supportively to mood-related messages (happy/sad)
- Fall back gracefully with a friendly message when it doesn't understand

## 🗂️ Project Structure

```
├── app.py            # Streamlit web interface
├── chatbot.py         # Chatbot logic (rule matching + responses)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## 🚀 Setup & Run Locally

1. **Install Python** (3.8 or newer) if you don't already have it:
   https://www.python.org/downloads/

2. **Download or clone this repository**, then open a terminal in the
   project folder.

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```

5. A browser tab will open automatically at `http://localhost:8501`
   where you can chat with the bot.

## 🌐 Live Demo

This app is also deployed on Streamlit Community Cloud:
`<ADD YOUR DEPLOYED LINK HERE AFTER DEPLOYING>`

## 🧩 Challenges & How They Were Solved

- **Keeping conversation history across interactions:** Streamlit reruns
  the entire script on every user action, so a naive approach would lose
  the chat history each time. This was solved using Streamlit's
  `st.session_state` to persist messages across reruns.
- **Avoiding repetitive-feeling replies:** Each rule maps to a *list* of
  possible responses, and one is chosen at random each time, so the bot
  feels a little more natural even with simple logic.
- **Matching flexible phrasing:** Instead of exact string matching,
  regex word-boundary patterns (e.g. `\bjoke\b`) are used so the bot
  recognizes keywords even inside longer sentences.

## 🔮 Possible Future Improvements

- Swap the rule-based engine for an LLM API (e.g. the Anthropic API) for
  more natural, open-ended conversation
- Add more rules/topics
- Add persistent chat history saved to a file or database
