import trafilatura
from urllib.parse import urlparse
import requests
from typing import Optional, Dict

class WebScraper:
    def __init__(self):
        self.timeout = 10
        
    def validate_url(self, url: str) -> str:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        parsed = urlparse(url)
        if not parsed.netloc:
            raise ValueError("Invalid URL format")
        
        return url
    
    def scrape_website(self, url: str) -> Dict[str, Optional[str]]:
        try:
            validated_url = self.validate_url(url)
            
            # Add a User-Agent to mimic a real browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            # Using urllib/requests to fetch with headers first (trafilatura fetch_url doesn't easily support custom headers in some versions)
            # Or use trafilatura directly if it supports it. It's safer to use requests then pass HTML to extract.
            response = requests.get(validated_url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            downloaded = response.text
            
            if not downloaded:
                raise Exception("Failed to fetch website content")
            
            content = trafilatura.extract(
                downloaded,
                include_links=False,
                include_images=False,
                include_tables=False
            )
            
            metadata = trafilatura.extract_metadata(downloaded)
            
            company_name = None
            if metadata:
                company_name = metadata.sitename or metadata.title or parsed.netloc.replace('www.', '')
            else:
                parsed = urlparse(validated_url)
                company_name = parsed.netloc.replace('www.', '').split('.')[0].title()
            
            description = None
            if metadata and metadata.description:
                description = metadata.description
            elif content:
                description = content[:200] + "..." if len(content) > 200 else content
            
            return {
                'url': validated_url,
                'company_name': company_name,
                'content': content or "No content extracted",
                'description': description or "No description available"
            }
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error while fetching URL: {str(e)}")
        except Exception as e:
            raise Exception(f"Error scraping website: {str(e)}")

def scrape_url(url: str) -> Dict[str, Optional[str]]:
    scraper = WebScraper()
    return scraper.scrape_website(url)
