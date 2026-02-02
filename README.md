
# Catch² (Square Catcher)

**Catch²** is a minimalist arcade game designed to be **calming, simple, and oddly satisfying**.
There’s no timer, no stress — just you, a bar, and a few squares.

🔗 **Play it here:** [https://catch2.onrender.com](https://catch2.onrender.com)

---

## How to Play

* You control a horizontal bar
* Catch the red squares with the bar to gain +1 point
* Avoid the yellow squares — touching them ends the game
* If you lose, you can restart instantly
* No time limits. No levels. Just flow.

The game is intentionally built to be **relaxing**, not competitive.

---

## Game Philosophy

Catch² isn’t about winning fast — it’s about:

* Focus
* Rhythm
* Calm reflexes
* Minimal visuals and feedback

Think of it as a **tiny arcade loop you can play to unwind**.

---

## Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask (Python)
* **Deployment:** Render

> Originally prototyped in pygame, then translated into a **web-based JavaScript version** while keeping the core mechanics intact.

---

## Project Structure
```
Catch-Squared/
├── pycode/
│   └── app.py          # Flask server
├── templates/
│   └── index.html      # Game UI
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── game.js     # Core game logic
│   └── audio/
│       └── sound.wav
├── requirements.txt
└── README.md
```
---

## 🚀 Run Locally

```bash
git clone https://github.com/johandavidcoder/Catch-Squared.git
cd Catch-Squared
pip install -r requirements.txt
python pycode/app.py
```

Open:

```
http://localhost:5001
```

---

## Possible Future Ideas

* Difficulty scaling over time
* Subtle visual effects
* Mobile-friendly controls
* High score memory

---

## Author

**Johan David**
GitHub: [https://github.com/johandavidcoder](https://github.com/johandavidcoder)

---
