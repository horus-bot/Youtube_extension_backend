# 🎬 Youtube Extension Backend

Welcome to the backend for your favorite YouTube subtitle and translation extension!  
Built with love (and a lot of coffee) by **Harsh Srivastava**.

## 🚀 Live Demo

Check it out in action:  
[https://youtube-extension-backend-hq10.onrender.com](https://youtube-extension-backend-hq10.onrender.com)

## 🧠 What does this do?

- **Summarize** YouTube videos in English (because who has time to watch the whole thing?).
- **Translate** subtitles to **Hindi** and **Tamil** (so your grandma can finally understand those cat videos).
- All powered by FastAPI, OpenAI, and a sprinkle of Python magic.

## 🛠️ Endpoints

| Endpoint         | Description                                 | Example Usage                                      |
|------------------|---------------------------------------------|----------------------------------------------------|
| `/summarize`     | Get a summary of a YouTube video            | `/summarize?url=YOUTUBE_URL`                       |
| `/hindi`         | Translate subtitles to Hindi                 | `/hindi?url=YOUTUBE_URL`                           |
| `/tamil`         | Translate subtitles to Tamil                 | `/tamil?url=YOUTUBE_URL`                           |

> Replace `YOUTUBE_URL` with your favorite (or least favorite) YouTube link.

## 🏗️ Project Structure

```
.
├── main.py                # FastAPI app with endpoints
├── groq_summary.py        # Summarization logic
├── hindi.py               # Hindi translation logic
├── tamil.py               # Tamil translation logic
├── transcription.py       # Subtitle fetching and processing
├── url.py                 # YouTube URL parsing
├── serialize.py           # Serialization helpers
├── requirements.txt       # All the dependencies
├── Procfile               # For deployment (if you like Procfiles)
├── render.yaml            # For Render.com deployment
├── .env                   # Shhh... secrets inside!
└── myvenv/                # Virtual environment (ignore this, seriously)
```

## 🧑‍💻 How to run locally

1. Clone this repo (use `git`, not a pigeon).
2. Create a virtual environment:
    ```sh
    python -m venv myvenv
    ```
3. Activate it:
    - Windows: `myvenv\Scripts\activate`
    - Mac/Linux: `source myvenv/bin/activate`
4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
5. Add your `GROQ_API_KEY` to a `.env` file:
    ```
    GROQ_API_KEY=your_secret_key_here
    ```
6. Run the server:
    ```sh
    uvicorn main:app --reload
    ```
7. Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API docs.

## 🤪 Fun Facts

- This backend is so fast, it might finish summarizing before you even paste the link. (Okay, maybe not, but it's pretty quick!)
- If you find a bug, it's not a bug—it's an undocumented feature.
- The codebase contains **0** lines of JavaScript. You're welcome.

## 📬 Contact

Made with ❤️ by **Harsh Srivastava**.  
If you like this project, buy me a coffee. If you don't, buy me two—I'll need the energy to