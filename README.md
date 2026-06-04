# ✦ TASKS — Minimal Task Manager

A sleek, dark-themed productivity app built with **Streamlit**. Manage your to-do list with priority levels, live stats, and persistent storage — all wrapped in a sharp cyberpunk-inspired UI.

---

## ✨ Features

- ✅ **Add tasks** with High / Medium / Low priority
- ☑️ **Mark tasks done** or undo them with one click
- 🗑️ **Delete individual tasks** or bulk-clear all completed ones
- 📊 **Live stats** — Total, Pending, Done, and % Complete
- 📈 **Progress bar** that fills as you complete tasks
- 🔍 **Filter view** — show All, Pending, or Done tasks
- 🕐 **Timestamps** — every task shows when it was added
- 💾 **Persistent storage** — tasks are saved to disk and survive page refreshes
- 🎨 **Custom cyberpunk UI** — dark theme, neon green accents, Syne + Space Mono fonts

---

## 🖥️ Preview

```
✦ TASKS ✦ Command Center ✦
Thursday, June 04 · 14:32

[ 5 Total ]  [ 3 Pending ]  [ 2 Done ]  [ 40% Complete ]
████████░░░░░░░░░░░░░░░░░░░░░░

// Add New Task
[ What needs to be done? ] [ High ▾ ] [ + ADD ]
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | App UI and interactivity |
| `json` | Saving and loading tasks from disk |
| `os` | Checking if the save file exists |
| `datetime` | Timestamps and live clock display |
| HTML/CSS (inline) | Custom dark cyberpunk theme |

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/tasks-app.git
cd tasks-app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
streamlit run tasks.py
```

The app will open at `http://localhost:8501`

> **No API key required!** This app runs entirely on local Python — no external services needed.

---

## 📁 Project Structure

```
tasks-app/
│
├── tasks.py             # Main application file
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📦 requirements.txt

```
streamlit
```

---

## 💾 How Data is Saved

Tasks are saved to `/tmp/fancy_tasks.json` as a JSON file. This means:

- ✅ Tasks **persist across page refreshes** within the same session
- ⚠️ On **Streamlit Cloud**, `/tmp` is cleared when the app restarts or goes to sleep — tasks will be lost
- 💡 For permanent cloud storage, consider replacing the file save with a database like [Supabase](https://supabase.com) or [Firebase](https://firebase.google.com)

---

## 🚀 Deploy Online for Free

1. Push this project to a **GitHub repository**
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo and select `tasks.py` as the main file
4. Click **Deploy** — you'll get a shareable link like `yourapp.streamlit.app`

No secrets or environment variables needed.

---

## ⚠️ Known Limitations

- Task data is stored in `/tmp` — it will be lost if the Streamlit Cloud app restarts
- No user accounts — everyone who visits the deployed app shares the same task list
- No due dates or reminders (yet!)

---

## 🙋 About the Developer

Built by **Shreyan** — Grade 10 student at Chirec International School, passionate about Physics, Economics, and building cool things with Python.

- 📧 Email: Shreyan.rao.gv@gmail.com
- 🐙 GitHub: [@shreyanraogv-cmyk](https://github.com/shreyanraogv-cmyk)

---
