import whois
import requests
from datetime import datetime
from app.credibility.domain_database import check_domain

def extract_domain(url: str) -> str:
    """استخرج الدومين من الرابط"""
    import re
    pattern = r'(?:https?://)?(?:www\.)?([^/\s]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else url

def check_domain_age(domain: str) -> dict:
    """فحص عمر الدومين عبر whois"""
    try:
        w = whois.whois(domain)
        creation_date = w.creation_date
        
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        
        if creation_date:
            age_days = (datetime.now() - creation_date).days
            age_years = age_days / 365
            return {
                "age_days": age_days,
                "age_years": round(age_years, 1),
                "score": min(age_years / 5, 1.0)  # 5 سنين = score كامل
            }
    except Exception:
        pass
    
    return {"age_days": None, "age_years": None, "score": 0.5}

def check_source(url: str) -> dict:
    """الفحص الشامل للمصدر"""
    domain = extract_domain(url)
    
    domain_info  = check_domain(domain)
    age_info     = check_domain_age(domain)
    
    # حساب الـ score النهائي
    final_score = (
        domain_info["score"] * 0.6 +
        age_info["score"]   * 0.4
    )
    
    return {
        "domain": domain,
        "domain_status": domain_info["status"],
        "domain_score": domain_info["score"],
        "age_years": age_info["age_years"],
        "age_score": age_info["score"],
        "final_score": round(final_score, 3)
    }