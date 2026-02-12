# 🚀 Vercel Deployment Guide: AI Outreach Tool

Follow these steps to deploy your FastAPI application to **Vercel** as Serverless Functions.

## 1. Prerequisites (Done ✅)

Your project is now Vercel-ready:
- **`vercel.json`**: Created to configure Python runtime and routing.
- **`requirements.txt`**: Confirmed compatible.
- **`main.py`**: Exports `app` correctly.

---

## 2. Push Changes to GitHub

Push the new `vercel.json` and other changes to your existing repository.

```bash
git add .
git commit -m "Configure for Vercel deployment"
git push origin main
```

---

## 3. Deploy on Vercel

1.  **Create Account**: Log in to [vercel.com](https://vercel.com/).
2.  **Add New Project**:
    *   Click **Add New...** -> **Project**.
    *   **Import Git Repository**: Select your `Ai-Powered-Personalized-Outreach-Tool` repo.
    *   Click **Import**.

3.  **Configure Project**:
    *   **Framework Preset**: Select **Other**.
    *   **Root Directory**: leave as `./`.
    *   **Build Command**: leave empty (Vercel handles Python automatically).
    *   **Output Directory**: leave empty.
    *   **Install Command**: leave empty (defaults to `pip install -r requirements.txt`).

4.  **Environment Variables (CRITICAL)**:
    *   Expand the **Environment Variables** section.
    *   Add your API Key:
        *   **Key**: `GEMINI_API_KEY` (or `GOOGLE_API_KEY`)
        *   **Value**: Paste your actual key starting with `AIza...`.
    *   Click **Add**.

5.  **Deploy**: Click **Deploy**.

Vercel will build your project. It usually takes < 1 minute.

---

## 4. Custom Domain Setup

Once deployed (e.g., `ai-outreach-tool.vercel.app`), add your domain.

1.  **Vercel Settings**:
    *   Go to your Project Dashboard.
    *   Click **Settings** -> **Domains**.
    *   Enter your domain (e.g., `www.yourdomain.com`) and click **Add**.

2.  **DNS Configuration (at your Domain Registrar)**:
    Vercel will show the required DNS records (usually `CNAME` or `A`).

    *   **CNAME Record (Recommended for subdomains like `www`)**:
        *   **Name**: `www`
        *   **Value**: `cname.vercel-dns.com`

    *   **A Record (for root domain `yourdomain.com`)**:
        *   **Name**: `@`
        *   **Value**: `76.76.21.21`

3.  **Verification**:
    *   Vercel verifies quickly (usually seconds to minutes).
    *   SSL is automatic and free.

## 5. Important Note on Timeouts ⚠️

**Vercel Hobby (Free) Tier** has a **10-second serverless function timeout**.
*   If the AI generation takes longer than 10 seconds, the request might fail with a "504 Gateway Timeout".
*   Gemini 1.5 Flash is usually fast enough, but keep this in mind.
*   **Pro Plan** increases timeout to 60s.
