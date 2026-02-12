# 🚀 Deployment Guide: AI Outreach Tool

Follow these steps to deploy your application to **Render.com** with a Custom Domain.

## 1. Prerequisites (Done ✅)

Your project is ready to go:
- **`requirements.txt`**: Created and up-to-date.
- **`.gitignore`**: Excludes `.env`, `venv`, and `__pycache__`.
- **`render.yaml`**: Created for automated deployment.
- **`main.py`**: Configured to serve correctly.

---

## 2. Push to GitHub

You need to push your code to a new GitHub repository.

1.  **Initialize Git** (if not already done):
    ```bash
    git init
    git add .
    git commit -m "Initial commit for deployment"
    ```

2.  **Create a New Repo on GitHub**:
    *   Go to [github.com/new](https://github.com/new).
    *   Name it `ai-outreach-tool` (or similar).
    *   **Do NOT** initialize with README/gitignore (you already have them).

3.  **Push Code**:
    *   Copy the commands provided by GitHub under "…or push an existing repository from the command line".
    *   They look like this (replace `YOUR_USERNAME`):
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/ai-outreach-tool.git
    git branch -M main
    git push -u origin main
    ```

---

## 3. Deploy on Render.com

1.  **Create Account**: Log in to [dashboard.render.com](https://dashboard.render.com/).
2.  **New Web Service**:
    *   Button: **New +** -> **Web Service**.
    *   Select **Build and deploy from a Git repository**.
    *   Connect your GitHub account and *select your repo*.

3.  **Configure Service**:
    *   **Name**: `ai-outreach-tool` (unique name).
    *   **Region**: Closest to you (e.g., Singapore, Frankfurt).
    *   **Branch**: `main`.
    *   **Runtime**: **Python 3**.
    *   **Build Command**: `pip install -r requirements.txt`
    *   **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
    *   **Plan**: **Free**.

4.  **Environment Variables (CRITICAL)**:
    *   Scroll down to **Environment Variables**.
    *   Click **Add Environment Variable**.
    *   **Key**: `GEMINI_API_KEY` (or `GOOGLE_API_KEY`)
    *   **Value**: Paste your actual key starting with `AIza...`.
    *   *Note: Do NOT include quotes.*

5.  **Deploy**: Click **Create Web Service**.

Render will start building your app. Watch the logs. It usually takes 2-3 minutes.

---

## 4. Custom Domain Setup

Once your site is live (e.g., `ai-outreach-tool.onrender.com`), add your custom domain.

1.  **Render Settings**:
    *   Go to your Web Service dashboard.
    *   Click **Settings** -> **Custom Domains**.
    *   Click **Add Custom Domain**.
    *   Enter your domain (e.g., `www.yourdomain.com`).

2.  **DNS Configuration (at your Domain Registrar)**:
    Render will show you the required DNS records. Typically:

    *   **CNAME Record**:
        *   **Host/Name**: `www`
        *   **Value/Target**: `ai-outreach-tool.onrender.com` (or similar provided by Render).
        *   **TTL**: Automatic or 3600.

    *   **A Record (for root domain `yourdomain.com`)**:
        *   Render will provide an IP address (e.g., `216.24.57.1`).
        *   **Host/Name**: `@` or blank.
        *   **Value**: The IP address provided.

3.  **Verification**:
    *   It might take a few minutes to verify.
    *   Render automatically provisions a **Free SSL Certificate** (HTTPS).

## 5. Verification

Visit your new URL (`https://www.yourdomain.com`).
1.  Enter a test URL.
2.  Generate an email.
3.  Ensure it works as expected! 🚀
