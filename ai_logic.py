import requests
import time
import json
from typing import Dict, Optional
from config import get_settings

class AIEmailGenerator:
    def __init__(self):
        self.settings = get_settings()
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        self._cached_model_name: Optional[str] = None
        
    def _get_best_model(self, api_key: str) -> str:
        """Dynamically find a supported model available to the user."""
        # Clear cache if it's a problematic model (gemini-3-pro has stricter quotas)
        if self._cached_model_name and ("gemini-3" in self._cached_model_name.lower()):
            cleared_model = self._cached_model_name
            self._cached_model_name = None
            try:
                log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
                with open(log_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps({"id":f"log_{int(time.time()*1000)}_cache_cleared_proactive","timestamp":int(time.time()*1000),"location":"ai_logic.py:_get_best_model","message":"Cleared problematic cached model","data":{"cleared_model":cleared_model},"runId":"debug","hypothesisId":"A"}) + "\n")
            except:
                pass
        
        if self._cached_model_name:
            try:
                log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
                with open(log_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps({"id":f"log_{int(time.time()*1000)}_model_cached","timestamp":int(time.time()*1000),"location":"ai_logic.py:_get_best_model","message":"Using cached model","data":{"model":self._cached_model_name},"runId":"debug","hypothesisId":"A"}) + "\n")
            except:
                pass
            return self._cached_model_name
            
        try:
            url = f"{self.base_url}/models?key={api_key}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                models = response.json().get('models', [])
                
                # Preferred order of models to try (updated to match available models)
                preferred = [
                    "gemini-2.5-flash",
                    "gemini-2.0-flash",
                    "gemini-2.5-pro",
                    "gemini-1.5-flash",
                    "gemini-1.5-pro",
                    "gemini-1.0-pro",
                    "gemini-pro"
                ]
                
                # Filter out models with stricter quota limits (like gemini-3-pro)
                excluded_models = ["gemini-3-pro", "gemini-3"]
                available_names = [
                    m['name'].replace('models/', '') 
                    for m in models 
                    if 'generateContent' in m.get('supportedGenerationMethods', [])
                    and not any(excluded in m['name'].replace('models/', '') for excluded in excluded_models)
                ]
                
                try:
                    log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
                    with open(log_path, "a", encoding="utf-8") as f:
                        f.write(json.dumps({"id":f"log_{int(time.time()*1000)}_models_filtered","timestamp":int(time.time()*1000),"location":"ai_logic.py:_get_best_model","message":"Models filtered","data":{"available_count":len(available_names),"available_models":available_names[:5]},"runId":"debug","hypothesisId":"A"}) + "\n")
                except:
                    pass
                
                # Check preferred first
                for p in preferred:
                    for a in available_names:
                        if p in a: # Partial match allows version suffixes
                             self._cached_model_name = a
                             try:
                                 log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
                                 with open(log_path, "a", encoding="utf-8") as f:
                                     f.write(json.dumps({"id":f"log_{int(time.time()*1000)}_model_selected","timestamp":int(time.time()*1000),"location":"ai_logic.py:_get_best_model","message":"Model selected from preferred list","data":{"model":a,"preferred":p,"available_count":len(available_names)},"runId":"debug","hypothesisId":"A"}) + "\n")
                             except:
                                 pass
                             return a
                
                # Fallback to ANY available generation model if no preferences match
                if available_names:
                    self._cached_model_name = available_names[0]
                    try:
                        log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
                        with open(log_path, "a", encoding="utf-8") as f:
                            f.write(json.dumps({"id":f"log_{int(time.time()*1000)}_model_fallback","timestamp":int(time.time()*1000),"location":"ai_logic.py:_get_best_model","message":"Using fallback model","data":{"model":available_names[0]},"runId":"debug","hypothesisId":"A"}) + "\n")
                    except:
                        pass
                    return available_names[0]
                    
        except Exception as e:
            print(f"Model discovery failed: {e}")
            try:
                log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
                with open(log_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps({"id":f"log_{int(time.time()*1000)}_model_discovery_error","timestamp":int(time.time()*1000),"location":"ai_logic.py:_get_best_model","message":"Model discovery failed","data":{"error":str(e)},"runId":"debug","hypothesisId":"A"}) + "\n")
            except:
                pass
            
        # Hard fallback if discovery fails entirely
        try:
            log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps({"id":f"log_{int(time.time()*1000)}_model_hard_fallback","timestamp":int(time.time()*1000),"location":"ai_logic.py:_get_best_model","message":"Using hard fallback model","data":{"model":"gemini-1.5-flash"},"runId":"debug","hypothesisId":"A"}) + "\n")
        except:
            pass
        return "gemini-1.5-flash"

    def _log_debug(self, message: str, data: dict, hypothesis_id: str = "A"):
        """Helper to safely write debug logs without breaking execution."""
        try:
            log_path = r"d:\projects\Ai Powere Personalization & Outreach tool\.cursor\debug.log"
            log_entry = {
                "id": f"log_{int(time.time()*1000)}_{message}",
                "timestamp": int(time.time()*1000),
                "location": "ai_logic.py:generate_email",
                "message": message,
                "data": data,
                "runId": "debug",
                "hypothesisId": hypothesis_id
            }
            with open(log_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(log_entry) + "\n")
        except Exception:
            pass  # Silently fail to not break execution
    
    def generate_email(self, company_info: Dict[str, str]) -> Dict[str, str]:
        """
        Generate email using AI API ONLY. This method MANDATORILY requires API access.
        No rule-based or template-based fallbacks are used - API is required.
        Returns a dictionary with 'email_body' and 'linkedin_note'.
        """
        self._log_debug("generate_email_started", {"company": company_info.get('company_name', 'Unknown')}, "A")
        api_key = self.settings.google_api_key
        
        # Validate API key is present - API is mandatory
        if not api_key or api_key == "YOUR_GEMINI_KEY" or api_key.strip() == "":
            self._log_debug("api_key_missing", {"has_key": bool(api_key)}, "A")
            raise Exception("API key is required. Please configure your Google Gemini API key in the .env file. Email generation requires API access and cannot proceed without it.")
        
        # Determine model dynamically
        model_name = self._get_best_model(api_key)
        self._log_debug("model_selected", {"model": model_name}, "A")
        
        url = f"{self.base_url}/models/{model_name}:generateContent?key={api_key}"
        
        prompt = f"""You are a B2B sales expert. Analyze the following company and generate two things:
1. A personalized cold email (under 150 words).
2. A LinkedIn connection note (under 300 characters).

Company Name: {company_info.get('company_name', 'Unknown')}
Website: {company_info.get('url', '')}
Description: {company_info.get('description', 'No description')}

Email Requirements:
- Tone: Engineer-to-engineer (technical, direct, no fluff).
- Avoid jargon like 'resonate deeply' or 'transformative'.
- Mention specific tech/service from their description.
- Professional greeting/signature.

LinkedIn Note Requirements:
- Friendly and professional.
- Mention their company or specific work.
- Under 300 characters (strict limit).

Output strictly valid JSON in the following format:
{{
  "email_body": "Subject: ... (email content)",
  "linkedin_note": "Hi [Name], ..."
}}
"""
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
        
        try:
            response = requests.post(
                url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            self._log_debug("api_response_received", {"status_code": response.status_code, "model": model_name}, "B")
            
            if response.status_code != 200:
                error_msg = response.text
                self._log_debug("api_error_detected", {"status_code": response.status_code, "error_preview": error_msg[:500], "is_429": response.status_code == 429}, "B")
                
                if response.status_code == 429:
                    # Clear cached model so we don't keep using the problematic one
                    if self._cached_model_name == model_name:
                        self._cached_model_name = None
                        self._log_debug("cache_cleared", {"cleared_model": model_name}, "C")
                    
                    # Parse error response to extract retry delay
                    try:
                        error_json = response.json()
                        retry_delay = 60  # Default 60 seconds
                        retry_info = error_json.get('error', {}).get('details', [])
                        for detail in retry_info:
                            if detail.get('@type') == 'type.googleapis.com/google.rpc.RetryInfo':
                                retry_delay_str = detail.get('retryDelay', '')
                                if 's' in retry_delay_str:
                                    try:
                                        retry_delay = float(retry_delay_str.replace('s', ''))
                                    except:
                                        pass
                        
                        self._log_debug("quota_error_parsed", {"model": model_name, "retry_delay": retry_delay, "error_details": str(error_json.get('error', {}))[:300]}, "C")
                        
                        # Try alternative models if current one is quota-exceeded
                        # Get available models dynamically and exclude problematic ones
                        try:
                            models_url = f"{self.base_url}/models?key={api_key}"
                            models_response = requests.get(models_url, timeout=10)
                            if models_response.status_code == 200:
                                available_models_data = models_response.json().get('models', [])
                                available_model_names = [
                                    m['name'].replace('models/', '') 
                                    for m in available_models_data 
                                    if 'generateContent' in m.get('supportedGenerationMethods', [])
                                    and "gemini-3" not in m['name'].lower()
                                ]
                                # Filter out the current model and prioritize flash models (usually have better quotas)
                                alternative_models = [m for m in available_model_names if m != model_name]
                                # Prioritize flash models
                                flash_models = [m for m in alternative_models if "flash" in m.lower()]
                                other_models = [m for m in alternative_models if "flash" not in m.lower()]
                                alternative_models = flash_models + other_models
                            else:
                                # Fallback to hardcoded list if API call fails
                                alternative_models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.5-pro", "gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro", "gemini-pro"]
                                alternative_models = [m for m in alternative_models if m != model_name and "gemini-3" not in m]
                        except Exception as e:
                            # Fallback to hardcoded list if there's an error
                            alternative_models = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-2.5-pro", "gemini-1.5-flash", "gemini-1.5-pro", "gemini-1.0-pro", "gemini-pro"]
                            alternative_models = [m for m in alternative_models if m != model_name and "gemini-3" not in m]
                            self._log_debug("alt_models_fallback", {"error": str(e), "using_fallback": True}, "D")
                        
                        self._log_debug("alt_models_list", {"original_model": model_name, "alternatives": alternative_models}, "D")
                        
                        for alt_model in alternative_models:
                            self._log_debug("trying_alt_model", {"original_model": model_name, "alternative_model": alt_model}, "D")
                            
                            alt_url = f"{self.base_url}/models/{alt_model}:generateContent?key={api_key}"
                            alt_response = requests.post(
                                alt_url,
                                json=payload,
                                headers={"Content-Type": "application/json"},
                                timeout=30
                            )
                            
                            self._log_debug("alt_model_response", {"model": alt_model, "status_code": alt_response.status_code, "is_429": alt_response.status_code == 429}, "D")
                            
                            if alt_response.status_code == 200:
                                self._log_debug("alt_model_success", {"model": alt_model}, "D")
                                
                                result = alt_response.json()
                                email_content = result['candidates'][0]['content']['parts'][0]['text']
                                return email_content.strip()
                            elif alt_response.status_code == 429:
                                # Continue to next alternative model
                                self._log_debug("alt_model_quota", {"model": alt_model, "continuing_to_next": True}, "D")
                                continue
                            else:
                                # If it's not a quota error, break and raise
                                self._log_debug("alt_model_other_error", {"model": alt_model, "status_code": alt_response.status_code, "error": alt_response.text[:200]}, "D")
                                break
                        
                        # All models exhausted or still quota error
                        self._log_debug("all_models_exhausted", {"original_model": model_name, "tried_alternatives": alternative_models}, "D")
                        raise Exception(f"Quota exceeded for Gemini API. Please check your plan and billing details. The API suggests retrying in {int(retry_delay)} seconds. For more information: https://ai.google.dev/gemini-api/docs/rate-limits")
                    except Exception as parse_error:
                        # If parsing fails, provide generic message
                        raise Exception(f"Quota exceeded for Gemini API (429). Please check your plan and billing details. Error: {error_msg[:200]}")
                
                if "API_KEY_INVALID" in error_msg or "key" in error_msg:
                    raise Exception("Invalid API Key. Please check your .env file.")
                raise Exception(f"Google API Error ({response.status_code}): {error_msg}")
                
            result = response.json()
            
            try:
                content_text = result['candidates'][0]['content']['parts'][0]['text']
                
                # Clean up markdown code blocks if present
                clean_text = content_text.replace('```json', '').replace('```', '').strip()
                
                # Parse JSON
                try:
                    generated_data = json.loads(clean_text)
                    return generated_data
                except json.JSONDecodeError:
                    # Fallback if AI fails to return valid JSON - try to salvage or return error
                    self._log_debug("json_parse_error", {"raw_text": content_text[:500]}, "B")
                    # If strictly text, assume it's just the email (legacy fallback)
                    return {
                        "email_body": clean_text,
                        "linkedin_note": "Could not generate LinkedIn note due to formatting error."
                    }
                    
            except (KeyError, IndexError):
                # Check for safety blocks
                if result.get('promptFeedback', {}).get('blockReason'):
                    raise Exception("AI blocked the content for safety reasons.")
                raise Exception("Unexpected response format from Google AI")
            
        except requests.exceptions.RequestException as e:
            # Network errors - API is mandatory, cannot proceed without API
            self._log_debug("network_error", {"error": str(e)}, "E")
            raise Exception(f"Network error connecting to AI API: {str(e)}. API access is required for email generation.")
        except Exception as e:
            # Any other exception - API is mandatory, re-raise to ensure no fallback
            self._log_debug("api_generation_failed", {"error": str(e)}, "E")
            # Re-raise the exception to ensure API is mandatory - no rule-based fallback
            raise

def generate_personalized_email(company_info: Dict[str, str]) -> Dict[str, str]:
    generator = AIEmailGenerator()
    return generator.generate_email(company_info)
