# Persona Generator

Generate detailed, psychologically grounded user personas from Reddit profiles. This tool scrapes a user's Reddit activity, analyzes it through specialized agents, and produces a complete persona file — including cited Reddit posts and behavioral insights.

---

## 🧠 Introduction

**Persona Generator** is a Python-based framework that takes a Reddit user profile as input and synthesizes a complete user persona, informed by their posts and comments. It leverages multi-agent systems to extract motivations, personality traits, goals, pain points, behaviors, and more — all with source citations from their content.

> This tool is ideal for researchers, marketers, UX designers, and social scientists seeking authentic, data-backed personas.

---

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Output Example](#output-example)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## 💾 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/pesona_generator.git
   cd pesona_generator
````

2. **(Optional) Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

```bash
python main.py https://www.reddit.com/user/kojied/
```

The tool will:

1. Scrape Reddit comments and submissions from the given profile.
2. Run multi-agent analysis on collected data.
3. Generate a cited user persona file under `personas/`.

---

## ✨ Features

* 🧠 **AI Agents**: Modular agents for goals, interests, personality, pain points, and more.
* 🔍 **Reddit Scraping**: Gathers comments and posts using `praw`.
* 📝 **Cited Output**: Every extracted insight includes source references from Reddit.
* 🧩 **Modular Design**: Easy to extend with new traits or data processors.
* 🛠️ **Configurable via `.env`** for secure API and Reddit credentials.

---

## 🧱 Project Structure

```
pesona_generator/
├── main.py                # Entry point
├── config.py              # Loads environment variables
├── schema.py              # Pydantic models for persona structure
├── helper.py              # Utility functions
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── agents/                # Specialized trait extraction agents
│   ├── content_analyzer.py
│   ├── data_extractor.py
│   ├── goal_agent.py
│   ├── interest_agent.py
│   ├── pain_agent.py
│   ├── personality_agent.py
│   └── synthesizer.py
├── personas/              # Generated persona output files
│   ├── kojied_persona.txt
│   └── Hungry-Move-6603_persona.txt
└── tools/                 # Reddit scraping logic
    └── reddit.py
```

---

## 📦 Dependencies

Listed in `requirements.txt`:

```text
crewai==0.141.0
pydantic==2.11.7
pydantic-settings==2.10.1
praw==7.8.1
```

---

## ⚙️ Configuration

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_gemini_key
Client_ID=your_reddit_client_id
Client_Secret=your_reddit_client_secret
User_Agent=your_user_agent_string
```

These settings are loaded using `pydantic-settings`:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str = None
    Client_ID: str = None
    Client_Secret: str = None
    User_Agent: str = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
```

---

## 📄 Output Example

Generated output stored in `/personas/` (e.g. `kojied_persona.txt`).

### Example Excerpt:

#### `personas/emily_minimalist.txt`

```
## Persona Profile: Emily, The Aspiring Minimalist

**Name:** Emily Carter  
**Age:** 28  
**Occupation:** Marketing Assistant  
**Location:** Urban apartment in a mid-sized city  
**Tier:** Beginner Minimalist  
**Archetype:** The Seeker/Idealist  

**Motivations:**  
- Financial freedom  
- Environmental responsibility  
- Reduced stress & clutter  
- Ethical consumption  
*(Cited directly from analyzed Reddit posts)*

**Personality Traits:**  
- High Openness, High Agreeableness  
- Moderate Conscientiousness & Neuroticism  

**Behaviors:**  
- Shops secondhand  
- Follows minimalist creators  
- Tracks spending  
*(Sources: r/minimalism, r/ZeroWaste, r/ethicalfashion)*

**Frustrations:**  
- Decision fatigue  
- Product affordability  
- Lack of support from others  

**Quote:**  
"I want to live a life with less stuff and more meaning."  
```

---

## 🛠️ Troubleshooting

| Problem               | Solution                                                |
| --------------------- | ------------------------------------------------------- |
| Empty output          | Ensure Reddit user has public posts/comments            |
| Reddit API auth error | Check credentials in `.env` and `config.py`             |
| Encoding issues       | Open output `.txt` files using UTF-8 compatible editors |
| No persona generated  | Make sure the profile has enough content for analysis   |

---

## 👤 Contributors

* **Surya Narayana Siddamurthi** – Creator & Developer

Pull requests and community feedback welcome!

---

```

Let me know if you’d like:
- Badges (e.g., Python version, license)
- A `LICENSE` file generated
- Example persona image diagram or rendered HTML version of the output
- Deployment instructions (e.g., Docker or CLI packaging)
```
