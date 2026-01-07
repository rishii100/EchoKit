# EchoKit-Agent

A real-time **voice-based AI agent** built using **LiveKit Agents**, supporting **speech-to-text**, **LLM reasoning**, **function calling**, and **text-to-speech**.
The assistant greets users, listens via microphone, responds intelligently, and can call tools (e.g., weather lookup) when required.

---

## 🚀 Features

* 🎧 **Voice Activity Detection (VAD)** using Silero
* 🗣️ **Speech-to-Text (STT)** using Cartesia Ink-Whisper
* 🧠 **LLM Reasoning** using Google Gemini 2.5 Flash
* 🔊 **Text-to-Speech (TTS)** using Cartesia Sonic-3
* 🛠️ **Function Calling** (Tool usage for weather lookup)
* 🔄 **Real-time streaming** via LiveKit rooms

---

## 🏗️ Architecture Diagram

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/715af5fa-3320-46fa-a8e9-fd5f75867b51" />


---

## 📦 Tech Stack

| Component       | Technology              |
| --------------- | ----------------------- |
| Real-time infra | LiveKit                 |
| VAD             | Silero                  |
| STT             | Cartesia Ink-Whisper    |
| LLM             | Google Gemini 2.5 Flash |
| TTS             | Cartesia Sonic-3        |
| Language        | Python        |

---

## 📁 Project Structure

```
.
├── main.py              # Entry point for LiveKit agent
├── .env.local           # Environment variables
├── README.md            # Project documentation
```

---

## 🧠 Tool: Weather Lookup

The agent includes a **function tool**:

```python
@function_tool
async def lookup_weather(context, location: str):
    return {"weather": "sunny", "temperature": 70}
```

### Tool Usage Rules

* The LLM **only calls this tool if the user asks about weather**
* Demonstrates **LLM + function calling orchestration**

---

## 🧑‍💻 How It Works (Step-by-Step)

1. **LiveKit Worker starts**
2. Agent connects to a LiveKit room
3. User speaks → VAD detects speech
4. Audio → STT converts speech to text
5. LLM processes intent
6. Tool is called *only if required*
7. Response → TTS converts text to speech
8. Audio streamed back to user in real-time

---

## ▶️ Running the Project

### 1️⃣ Install Dependencies

```bash
pip install livekit-agents livekit-plugins-silero python-dotenv
```

### 2️⃣ Run the Agent

```bash
python assistant.py console
```

---

## 🧪 Default Agent Behavior

* Greets the user at the start
* Asks how their day is going
* Waits for voice input
* Responds conversationally
* Uses tools **only when necessary**

---

## 📜 License

MIT License © 2026
