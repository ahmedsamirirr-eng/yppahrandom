# How to Share Your Valentine App with Your Fiancée 💕

You can get a **public link** so Alaa (LoLo) can open the app in her browser. Here are two simple options.

---

## Option 1: Streamlit Community Cloud (recommended, free)

This gives you a link like: **`https://your-app-name.streamlit.app`** that works from anywhere.

### Steps

1. **Create a GitHub account** (if you don’t have one): [github.com](https://github.com)

2. **Put your project on GitHub**
   - Create a new repository (e.g. `valentine-app`).
   - Upload your whole project folder:
     - `valentine_app.py`
     - `requirements.txt`
     - The **`images`** folder (with all your photos inside)
   - Commit and push.

3. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io).
   - Sign in with GitHub.
   - Click **“New app”**.
   - **Repository:** choose your repo (e.g. `your-username/valentine-app`).
   - **Branch:** `main` (or your default branch).
   - **Main file path:** `valentine_app.py`.
   - Click **“Deploy!”**.

4. **Get your link**
   - After a few minutes you’ll see a URL like:  
     **`https://valentine-app-xxxxx.streamlit.app`**
   - Send this link to your fiancée. She can open it on her phone or computer.

**Important:** The `images` folder (with all your photos) must be in the same repo so the gallery works online.

---

## Option 2: ngrok (run on your PC, share a temporary link)

Use this if you want to run the app on your own computer and share a link only for a while (e.g. same day).

### Steps

1. **Run your app**
   ```bash
   cd c:\Users\egahm\Downloads\valentine
   streamlit run valentine_app.py
   ```

2. **Install ngrok** (if needed): [ngrok.com/download](https://ngrok.com/download)

3. **Create a public tunnel**
   - Open a **new** terminal (keep Streamlit running in the first one).
   - Run:
     ```bash
     ngrok http 8501
     ```
   - ngrok will show a line like: **`Forwarding https://abc123.ngrok.io -> http://localhost:8501`**

4. **Share that link**
   - Send **`https://abc123.ngrok.io`** (your actual URL will be different) to your fiancée.
   - She can open it in her browser as long as your PC is on and both Streamlit and ngrok are running.

**Note:** The link stops working when you close ngrok or your computer. For a permanent link, use Option 1.

---

## Quick checklist before sharing

- [ ] `images` folder is included (and has the photos you want).
- [ ] You’ve tested the app locally (`streamlit run valentine_app.py`).
- [ ] For Option 1: repo is **public** or you’ve given Streamlit Cloud access to the repo.

Once you have your link, you can send it to Alaa so she can open it and say Yes 💖.
