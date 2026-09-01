# 🚀 AI Learning Roadmap Generator

An AI-powered application that generates personalized learning roadmaps based on a user's domain, skill level, and available learning time.

## 📌 Project Overview

The AI Learning Roadmap Generator helps learners create a structured and practical learning plan for any domain or field.

The user provides:

* 📚 Domain / Field
* 🎯 Skill Level
* ⏱️ Available Learning Time

The application uses a Large Language Model (LLM) through the Groq API to generate a personalized roadmap.

## ✨ Features

* Personalized learning roadmaps
* Beginner, Intermediate, and Advanced skill levels
* Multiple learning durations
* Structured learning phases
* Weekly learning timeline
* Topics and skills to learn
* Practice activities
* Practical project recommendations
* Tools and technologies to learn
* Expected learning outcomes
* Next steps

## 🛠️ Technologies Used

* Python
* Gradio
* Groq API
* OpenAI Python SDK
* Google Colab
* Large Language Model (LLM)

## 🔄 How It Works

```text
User
  ↓
Gradio Interface
  ↓
Python Function
  ↓
Groq API
  ↓
LLM
  ↓
Personalized Learning Roadmap
  ↓
Gradio Output
```

## 📂 Project Structure

```text
ai-learning-roadmap-generator/
│
├── AI_Learning_Roadmap_Generator.ipynb
├── README.md
└── requirements.txt
```

## 🚀 How to Run

### 1. Open the notebook

Open `AI_Learning_Roadmap_Generator.ipynb` using Google Colab.

### 2. Install dependencies

Run the installation cell:

```python
!pip install -q openai gradio
```

### 3. Configure the Groq API key

The application uses Google Colab Secrets to keep the API key secure.

Create a secret named:

```text
GROQ_API_KEY
```

Then enable notebook access.

The notebook retrieves the key using:

```python
from google.colab import userdata

GROQ_API_KEY = userdata.get("GROQ_API_KEY")
```

### 4. Run the notebook

Run the cells from top to bottom.

### 5. Launch the application

The final cell launches the Gradio interface and provides a shareable link.

## 💡 Example

### User Input

```text
Domain: Data Analysis
Skill Level: Beginner
Learning Time: 3 Months
```

### Generated Output

The application generates a structured learning roadmap containing:

* Learning phases
* Weekly timeline
* Topics
* Practice activities
* Projects
* Tools
* Expected outcomes
* Next steps

## 🔐 API Key Security

The API key is **not stored in the source code**.

Google Colab Secrets is used to securely access the `GROQ_API_KEY`.

Never commit an API key such as:

```text
gsk_...
```

to GitHub.

## 🔮 Future Improvements

Planned features include:

* ⏰ Hours per week
* 🎯 Learning goals
* 📅 Detailed weekly schedules
* 💻 Personalized project generation
* 🧠 Quiz generation
* 📈 Progress tracking
* 📥 PDF roadmap export
* 🔄 Roadmap regeneration
* 🎨 Improved user interface
* 🌐 Deployment as a public web application

## 👩‍💻 Author

Built as an AI learning and portfolio project using Python, Gradio, and Groq.
