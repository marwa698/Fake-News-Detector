# قاعدة بيانات المصادر الموثوقة وغير الموثوقة

TRUSTED_DOMAINS = {
    # عربية موثوقة
    "aljazeera.net", "aljazeera.com",
    "bbc.com/arabic", "arabic.cnn.com",
    "alarabiya.net", "skynewsarabia.com",
    "ahram.org.eg", "alhurra.com",
    "france24.com/ar",
    # إنجليزية موثوقة
    "bbc.com", "reuters.com",
    "apnews.com", "theguardian.com",
    "nytimes.com", "washingtonpost.com",
    "npr.org", "bloomberg.com",
    "economist.com", "ft.com",
}

UNTRUSTED_DOMAINS = {
    "beforeitsnews.com",
    "infowars.com",
    "naturalnews.com",
    "worldnewsdailyreport.com",
    "empirenews.net",
    "theonion.com",  # ساخر
    "babylonbee.com",  # ساخر
}

def check_domain(domain: str) -> dict:
    """
    يفحص الدومين ويرجع:
    - status: trusted / untrusted / unknown
    - score: 1.0 / 0.0 / 0.5
    """
    domain = domain.lower().replace("www.", "")
    
    for trusted in TRUSTED_DOMAINS:
        if trusted in domain:
            return {"status": "trusted", "score": 1.0}
    
    for untrusted in UNTRUSTED_DOMAINS:
        if untrusted in domain:
            return {"status": "untrusted", "score": 0.0}
    
    return {"status": "unknown", "score": 0.5}