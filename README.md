# 🚀 AI-Powered Personalized Outreach Tool

A professional web application that generates personalized B2B cold emails using AI. Simply enter a company's website URL, and the tool will scrape the content, analyze it using AI, and generate a tailored outreach email.

## ✨ Features

- **🎯 Smart Website Analysis**: Automatically extracts company information from any website
- **🤖 AI-Powered Generation**: Uses Mistral-7B-Instruct via Hugging Face for intelligent email creation
- **💼 B2B Focused**: Specifically designed for professional outreach and cold emails
- **🎨 Modern UI**: Clean, professional dashboard with Tailwind CSS
- **⚡ Fast & Easy**: Generate personalized emails in seconds

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML/Jinja2 Templates + Tailwind CSS
- **AI Model**: Mistral-7B-Instruct (via Hugging Face Inference API)
- **Web Scraping**: Trafilatura
- **Deployment**: Ready for Render.com or Railway

## 📋 Prerequisites

- Python 3.8 or higher
- Hugging Face account and API token (free tier available)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd "Ai Powere Personalization & Outreach tool"
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

1. Get your Hugging Face API token:
   - Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Create a new token (read access is sufficient)
   - Copy the token

2. Configure the `.env` file:
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your token
   HUGGINGFACE_API_TOKEN=your_actual_token_here
   ```

### 5. Run the Application

```bash
# Development mode with auto-reload
uvicorn main:app --reload

# Or use the main.py script
python main.py
```

The application will start at **http://localhost:8000**

## 📖 Usage

1. **Open the Dashboard**: Navigate to http://localhost:8000 in your browser
2. **Enter URL**: Input a company website URL (e.g., `https://example.com` or just `example.com`)
3. **Generate**: Click "Generate Email" and wait a few seconds
4. **Copy & Use**: Copy the generated email and customize as needed

## 📁 Project Structure

```
Ai Powere Personalization & Outreach tool/
├── main.py                 # FastAPI application & routing
├── scraper.py             # Web scraping logic with trafilatura
├── ai_logic.py            # AI email generation with Hugging Face
├── config.py              # Configuration & environment management
├── .env                   # Environment variables (not in git)
├── .env.example           # Environment template
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── templates/            # Jinja2 HTML templates
    ├── base.html         # Base template with Tailwind
    ├── index.html        # Dashboard/home page
    └── result.html       # Email results page
```

## 🎨 UI Features

- **Professional Dashboard**: Modern gradient sidebar with navigation
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Loading States**: Visual feedback during email generation
- **Copy to Clipboard**: One-click email copying
- **Error Handling**: Clear error messages and retry options
- **Glassmorphism Effects**: Modern visual aesthetics

## 🚢 Deployment

### Deploy to Render.com

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Add environment variable:
   - Key: `HUGGINGFACE_API_TOKEN`
   - Value: Your HF token

### Deploy to Railway

1. Create a new project on Railway
2. Connect your GitHub repository
3. Add environment variable:
   - `HUGGINGFACE_API_TOKEN`: Your HF token
4. Railway will auto-detect the Python app and deploy

## 🔧 API Endpoints

- `GET /` - Dashboard home page
- `POST /generate` - Generate personalized email from URL
- `GET /health` - Health check endpoint

## ⚙️ Configuration

Edit `config.py` or set environment variables:

- `HUGGINGFACE_API_TOKEN` - Your Hugging Face API token (required)
- `APP_TITLE` - Application title (optional)
- `APP_DESCRIPTION` - Application description (optional)

## 🐛 Troubleshooting

### Model Loading Error (503)
The Hugging Face model might be loading. Wait 30-60 seconds and try again.

### Invalid URL Error
Ensure the URL is valid and accessible. Try with `https://` prefix.

### API Token Error
Verify your token is correct in the `.env` file and has read access.

### Import Errors
Make sure all dependencies are installed: `pip install -r requirements.txt`

## 📝 Notes

- The free tier of Hugging Face has rate limits. For production use, consider upgrading.
- Generated emails should be reviewed and customized before sending.
- The tool works best with business websites that have clear content.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ using FastAPI, Tailwind CSS, and AI

---

**Happy Outreaching! 🚀**
