from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from config import get_settings
from scraper import scrape_url
from ai_logic import generate_personalized_email

app = FastAPI(
    title=get_settings().app_title,
    description=get_settings().app_description
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")

class URLInput(BaseModel):
    url: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": get_settings().app_title}
    )

@app.post("/generate", response_class=HTMLResponse)
async def generate_email(request: Request, url: str = Form(...)):
    try:
        scraped_data = scrape_url(url)
        
        ai_response = generate_personalized_email(scraped_data)
        
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "title": "Generated Result",
                "email_body": ai_response.get('email_body'),
                "linkedin_note": ai_response.get('linkedin_note'),
                "company_name": scraped_data.get('company_name'),
                "url": scraped_data.get('url'),
                "description": scraped_data.get('description')
            }
        )
    
    except Exception as e:
        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "title": "Error",
                "error": str(e),
                "url": url
            }
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "AI Outreach Tool"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
